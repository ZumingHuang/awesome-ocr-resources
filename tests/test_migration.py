from __future__ import annotations

from pathlib import Path

from ocr_resources.migration.legacy_markdown import migrate_legacy, parse_paper_file
from ocr_resources.repository import load_resources, validate_repository

ROOT = Path(__file__).parents[1]


def test_legacy_parser_handles_known_format_variants() -> None:
    modern = parse_paper_file(ROOT / "legacy/papers/papers_by_year/2019-2022.md")
    assert len(modern) == 75
    selfdoc = next(item for item in modern if item.title.startswith("SelfDoc:"))
    assert "title was not bold" in selfdoc.warnings[0]
    psenet = next(item for item in modern if item.title.startswith("Shape Robust Text Detection"))
    assert psenet.year == 2019
    assert "CVPR" in psenet.tags

    classic = parse_paper_file(ROOT / "legacy/papers/papers_by_year/before-2010.md")
    assert [item.year for item in classic] == [2010, 2002]


def test_migration_preserves_occurrences_and_merges_exact_duplicate(tmp_path: Path) -> None:
    for directory in ("legacy", "config"):
        source = ROOT / directory
        target = tmp_path / directory
        target.mkdir(parents=True)
        for path in source.rglob("*"):
            if path.is_file():
                destination = target / path.relative_to(source)
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(path.read_bytes())

    report = migrate_legacy(tmp_path)
    resources = load_resources(tmp_path)
    papers = [resource for resource in resources if resource.kind.value == "paper"]
    datasets = [resource for resource in resources if resource.kind.value == "dataset"]

    assert report.paper_input == 233
    assert report.paper_output == 233
    assert report.paper_unique == 232
    assert report.dataset_input == report.dataset_output == 27
    assert len(papers) == 232
    assert len(datasets) == 27
    psenet = next(resource for resource in papers if resource.arxiv_id == "1806.02559")
    assert len(psenet.provenance.legacy_duplicates) == 1
    assert not validate_repository(tmp_path)
