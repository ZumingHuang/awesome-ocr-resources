from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from ocr_resources.discovery.base import RawCandidate
from ocr_resources.identity import normalize_title


@dataclass(frozen=True)
class Score:
    total: int
    breakdown: dict[str, int]
    eligible: bool


def score_candidate(candidate: RawCandidate, rules: dict[str, object]) -> Score:
    weights = rules["weights"]
    assert isinstance(weights, dict)
    terms = rules["required_terms"]
    assert isinstance(terms, list)
    text = " ".join([candidate.name, candidate.summary, *candidate.tags]).casefold()
    is_relevant = any(str(term).casefold() in text for term in terms)
    relevance = int(weights["relevance"]) if is_relevant else 0
    authority = int(weights["authority"])
    completeness_weight = int(weights["completeness"])
    completeness = completeness_weight if candidate.summary else completeness_weight // 2
    usability = int(weights["usability"]) if candidate.canonical_url else 0
    impact = 0
    if candidate.metadata.get("stars", 0) or candidate.metadata.get("downloads", 0):
        impact = int(weights["impact"])
    freshness = int(weights["freshness"])
    breakdown = {
        "relevance": relevance,
        "authority": authority,
        "completeness": completeness,
        "usability": usability,
        "impact": impact,
        "freshness": freshness,
    }
    thresholds = rules["thresholds"]
    assert isinstance(thresholds, dict)
    threshold = int(thresholds["draft_pr"])
    total = sum(breakdown.values())
    return Score(total=total, breakdown=breakdown, eligible=relevance > 0 and total >= threshold)


def candidate_fingerprint(candidate: RawCandidate) -> str:
    title = normalize_title(candidate.name)
    return f"{candidate.kind.value}:{candidate.source}:{candidate.source_id}:{title}"


def load_rejected(root: Path) -> set[str]:
    path = root / "state" / "rejected-fingerprints.jsonl"
    if not path.exists():
        return set()
    values: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            values.add(json.loads(line)["fingerprint"])
    return values
