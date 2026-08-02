from __future__ import annotations

import json
import os
from collections import Counter
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import yaml

from ocr_resources.discovery.arxiv import ArxivCollector
from ocr_resources.discovery.base import Collector, DiscoveryWindow, RawCandidate
from ocr_resources.discovery.github import GitHubCollector
from ocr_resources.discovery.huggingface import HuggingFaceCollector
from ocr_resources.discovery.scoring import candidate_fingerprint, load_rejected, score_candidate
from ocr_resources.identity import canonical_key, slugify
from ocr_resources.models import (
    CodeResource,
    Curation,
    CurationStatus,
    DatasetResource,
    DatePrecision,
    LicenseInfo,
    ModelResource,
    PaperResource,
    PartialDate,
    PlatformResource,
    Provenance,
    Resource,
    ResourceKind,
    ResourceLinks,
    SkillCapabilities,
    SkillResource,
)
from ocr_resources.rendering import render_repository, write_daily_update
from ocr_resources.repository import load_resources, write_resource


def _load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected mapping in {path}")
    return value


def build_collectors(root: Path, selected: set[str] | None = None) -> list[Collector]:
    sources = _load_yaml(root / "config" / "sources.yaml")
    queries = _load_yaml(root / "config" / "discovery_queries.yaml")
    selected = selected or {"arxiv", "huggingface", "github"}
    collectors: list[Collector] = []
    arxiv = dict(sources["arxiv"])
    huggingface = dict(sources["huggingface"])
    github = dict(sources["github"])
    if "arxiv" in selected and arxiv["enabled"]:
        collectors.append(ArxivCollector(str(arxiv["endpoint"]), list(queries["paper_queries"])))
    if "huggingface" in selected and huggingface["enabled"]:
        collectors.append(
            HuggingFaceCollector(
                str(huggingface["endpoint"]),
                list(queries["hub_queries"]),
                token=os.environ.get("HF_TOKEN"),
            )
        )
    if "github" in selected and github["enabled"]:
        collectors.append(
            GitHubCollector(
                str(github["endpoint"]),
                list(queries["github_code_queries"]),
                list(queries["github_skill_queries"]),
                minimum_stars=int(github["minimum_stars"]),
                token=os.environ.get("GITHUB_TOKEN"),
            )
        )
    return collectors


def _infer_tasks(candidate: RawCandidate) -> list[str]:
    text = " ".join([candidate.name, candidate.summary, *candidate.tags]).casefold()
    rules = [
        ("document-vqa", ("document question", "docvqa", "textvqa", "visual question")),
        ("table-recognition", ("table recognition", "table structure", "table extraction")),
        ("formula-recognition", ("formula", "mathematical expression")),
        ("document-layout-analysis", ("layout analysis", "layout detection")),
        ("document-parsing", ("document parsing", "document parser", "document understanding")),
        ("handwriting-recognition", ("handwriting", "handwritten")),
        ("text-spotting", ("text spotting", "text spotter")),
        ("text-detection", ("text detection", "text detector")),
        ("text-recognition", ("ocr", "optical character recognition", "text recognition")),
    ]
    tasks = [task for task, terms in rules if any(term in text for term in terms)]
    return tasks or ["other"]


def _partial_date(value: date | None) -> PartialDate:
    if value is None:
        return PartialDate(value="unknown", precision=DatePrecision.UNKNOWN)
    return PartialDate(value=value.isoformat(), precision=DatePrecision.DAY)


def _common_fields(candidate: RawCandidate, added_at: date) -> dict[str, object]:
    return {
        "name": candidate.name,
        "released_at": _partial_date(candidate.released_at),
        "added_at": added_at,
        "last_verified_at": added_at,
        "summary": candidate.summary,
        "tasks": _infer_tasks(candidate),
        "modalities": ["unspecified"],
        "languages": ["unspecified"],
        "links": ResourceLinks.model_validate({"canonical": candidate.canonical_url}),
        "license": LicenseInfo(),
        "provenance": Provenance.model_validate(
            {
                "canonical_source": candidate.canonical_url,
                "discovered_via": candidate.source,
                "discovered_at": added_at,
                "source_id": candidate.source_id,
                "source_metadata": candidate.metadata,
            }
        ),
        "curation": Curation(status=CurationStatus.CANDIDATE),
    }


def candidate_to_resource(candidate: RawCandidate, added_at: date) -> Resource:
    data = _common_fields(candidate, added_at)
    if candidate.kind == ResourceKind.PAPER:
        arxiv_id = str(candidate.metadata.get("arxiv_id") or candidate.source_id)
        data.update(
            id=f"paper:arxiv:{arxiv_id}",
            kind=ResourceKind.PAPER,
            authors=candidate.authors,
            year=(candidate.released_at or added_at).year,
            venue="arXiv",
            publication_status="preprint",
            arxiv_id=arxiv_id,
            doi=candidate.metadata.get("doi"),
        )
        return PaperResource.model_validate(data)
    if candidate.kind == ResourceKind.MODEL:
        repository_id = str(candidate.metadata["repository_id"])
        data.update(
            id=f"model:huggingface:{repository_id}",
            kind=ResourceKind.MODEL,
            provider=repository_id.split("/", 1)[0] if "/" in repository_id else "unknown",
            repository_id=repository_id,
            open_weights=None,
        )
        return ModelResource.model_validate(data)
    if candidate.kind == ResourceKind.DATASET:
        repository_id = str(candidate.metadata["repository_id"])
        data.update(
            id=f"dataset:huggingface:{repository_id}",
            kind=ResourceKind.DATASET,
            provider=repository_id.split("/", 1)[0] if "/" in repository_id else None,
            repository_id=repository_id,
            usage=[],
            access="unknown",
        )
        return DatasetResource.model_validate(data)
    if candidate.kind == ResourceKind.CODE:
        repository = str(candidate.metadata["repository"])
        language = candidate.metadata.get("language")
        data.update(
            id=f"code:github:{repository}",
            kind=ResourceKind.CODE,
            repository=repository,
            programming_languages=[str(language)] if language else [],
            maintenance_status=("archived" if candidate.metadata.get("archived") else "active"),
        )
        return CodeResource.model_validate(data)
    if candidate.kind == ResourceKind.SKILL:
        repository = str(candidate.metadata["repository"])
        manifest_path = str(candidate.metadata["manifest_path"])
        data.update(
            id=f"skill:github:{repository}:{slugify(manifest_path)}",
            kind=ResourceKind.SKILL,
            ecosystem=str(candidate.metadata.get("ecosystem", "agent-skills")),
            repository=repository,
            manifest_path=manifest_path,
            capabilities=SkillCapabilities(),
        )
        return SkillResource.model_validate(data)
    if candidate.kind == ResourceKind.PLATFORM:
        data.update(
            id=f"platform:{slugify(candidate.source_id)}",
            kind=ResourceKind.PLATFORM,
            provider=str(candidate.metadata["provider"]),
            regions=[],
            delivery_modes=[],
        )
        return PlatformResource.model_validate(data)
    raise ValueError(f"unsupported candidate kind: {candidate.kind}")


def discover_resources(
    root: Path,
    *,
    lookback_days: int = 7,
    selected_sources: set[str] | None = None,
    dry_run: bool = False,
    until: date | None = None,
    collectors: list[Collector] | None = None,
) -> dict[str, Any]:
    until = until or date.today()
    window = DiscoveryWindow(
        since=until - timedelta(days=max(lookback_days - 1, 0)),
        until=until,
    )
    collectors = collectors if collectors is not None else build_collectors(root, selected_sources)
    rules = _load_yaml(root / "config" / "quality_rules.yaml")
    existing_keys = {canonical_key(resource) for resource in load_resources(root)}
    rejected = load_rejected(root)
    source_counts: Counter[str] = Counter()
    skip_counts: Counter[str] = Counter()
    additions: list[Resource] = []
    candidate_rows: list[dict[str, Any]] = []
    source_errors: list[dict[str, str]] = []
    seen_candidate_keys: set[str] = set()
    for collector in collectors:
        try:
            collected = collector.collect(window)
        except Exception as exc:
            source_errors.append({"source": collector.name, "error": str(exc)})
            continue
        for candidate in collected:
            source_counts[candidate.source] += 1
            fingerprint = candidate_fingerprint(candidate)
            score = score_candidate(candidate, rules)
            row: dict[str, Any] = {
                "source": candidate.source,
                "source_id": candidate.source_id,
                "kind": candidate.kind.value,
                "name": candidate.name,
                "url": candidate.canonical_url,
                "score": score.total,
                "breakdown": score.breakdown,
            }
            if fingerprint in rejected:
                row["decision"] = "previously-rejected"
                skip_counts["previously-rejected"] += 1
            elif not score.eligible:
                row["decision"] = "below-threshold"
                skip_counts["below-threshold"] += 1
            else:
                resource = candidate_to_resource(candidate, until)
                key = canonical_key(resource)
                if key in existing_keys or key in seen_candidate_keys:
                    row["decision"] = "duplicate"
                    skip_counts["duplicate"] += 1
                else:
                    row["decision"] = "add"
                    resource.curation.relevance_score = score.total
                    additions.append(resource)
                    seen_candidate_keys.add(key)
            candidate_rows.append(row)
    added_count = 0
    if not dry_run and not source_errors:
        for resource in additions:
            write_resource(root, resource)
        added_count = len(additions)
        if additions:
            write_daily_update(root, additions, until, source_summary=dict(source_counts))
            render_repository(root)
    report: dict[str, Any] = {
        "date": until.isoformat(),
        "window": {"since": window.since.isoformat(), "until": window.until.isoformat()},
        "dry_run": dry_run,
        "sources": dict(source_counts),
        "source_errors": source_errors,
        "matched": len(additions),
        "added": added_count,
        "skipped": dict(skip_counts),
        "candidates": candidate_rows,
    }
    reports = root / "reports"
    reports.mkdir(exist_ok=True)
    (reports / f"discovery-{until.isoformat()}.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report
