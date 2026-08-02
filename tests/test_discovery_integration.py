from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from ocr_resources.discovery.base import DiscoveryWindow, RawCandidate
from ocr_resources.discovery.runner import discover_resources
from ocr_resources.models import ResourceKind

ROOT = Path(__file__).parents[1]


class FailingCollector:
    name = "failing"

    def collect(self, window: DiscoveryWindow) -> list[RawCandidate]:
        raise RuntimeError("temporary source failure")


class FixtureCollector:
    name = "fixture"

    def collect(self, window: DiscoveryWindow) -> list[RawCandidate]:
        return [
            RawCandidate(
                source="fixture",
                source_id="2607.99999",
                kind=ResourceKind.PAPER,
                name="A New OCR Document Parsing Method",
                canonical_url="https://arxiv.org/abs/2607.99999",
                released_at=window.until,
                summary="Optical character recognition and document parsing.",
                authors=["Test Author"],
                tags=["ocr"],
                metadata={"arxiv_id": "2607.99999"},
            )
        ]


def _minimal_root(tmp_path: Path) -> None:
    for relative in (
        "config/quality_rules.yaml",
        "config/taxonomy.yaml",
        "templates",
    ):
        source = ROOT / relative
        destination = tmp_path / relative
        if source.is_dir():
            for file in source.rglob("*"):
                if file.is_file():
                    target = destination / file.relative_to(source)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(file.read_bytes())
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(source.read_bytes())
    for directory in ("papers", "models", "datasets", "codes", "skills", "platforms"):
        (tmp_path / "data" / directory).mkdir(parents=True, exist_ok=True)


def test_source_failure_prevents_partial_writes(tmp_path: Path) -> None:
    _minimal_root(tmp_path)
    report = discover_resources(
        tmp_path,
        until=date(2026, 7, 26),
        collectors=[FixtureCollector(), FailingCollector()],
    )
    assert report["matched"] == 1
    assert report["added"] == 0
    assert report["source_errors"] == [{"source": "failing", "error": "temporary source failure"}]
    assert not list((tmp_path / "data/papers").glob("**/*.yaml"))


def test_fixture_discovery_is_idempotent(tmp_path: Path) -> None:
    _minimal_root(tmp_path)
    run_date = date(2026, 7, 26)
    first = discover_resources(
        tmp_path,
        until=run_date,
        collectors=[FixtureCollector()],
    )
    second = discover_resources(
        tmp_path,
        until=run_date,
        collectors=[FixtureCollector()],
    )
    assert first["added"] == 1
    assert second["added"] == 0
    assert second["skipped"]["duplicate"] == 1
    report = json.loads(
        (tmp_path / "reports/discovery-2026-07-26.json").read_text(encoding="utf-8")
    )
    assert report["added"] == 0
