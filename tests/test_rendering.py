from __future__ import annotations

from pathlib import Path

from ocr_resources.migration.legacy_markdown import migrate_legacy
from ocr_resources.rendering import render_repository

ROOT = Path(__file__).parents[1]


def _copy_inputs(tmp_path: Path) -> None:
    for directory in ("legacy", "config", "templates"):
        source = ROOT / directory
        for path in source.rglob("*"):
            if path.is_file():
                destination = tmp_path / path.relative_to(ROOT)
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(path.read_bytes())


def test_render_is_idempotent_and_keeps_legacy_paths(tmp_path: Path) -> None:
    _copy_inputs(tmp_path)
    migrate_legacy(tmp_path)
    first = render_repository(tmp_path)
    second = render_repository(tmp_path)
    assert first
    assert second == []
    assert (tmp_path / "papers/papers_by_year/2023-present.md").exists()
    assert (tmp_path / "datasets/README.md").exists()
    assert (tmp_path / "README.zh-CN.md").exists()
    assert "Generated from data/*.yaml" in (tmp_path / "README.md").read_text()
