from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class Taxonomy:
    tasks: frozenset[str]
    modalities: frozenset[str]
    languages: frozenset[str]
    legacy_task_map: dict[str, str]

    def map_legacy_task(self, value: str) -> str | None:
        return self.legacy_task_map.get(value)


def load_taxonomy(root: Path) -> Taxonomy:
    path = root / "config" / "taxonomy.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return Taxonomy(
        tasks=frozenset(data["tasks"]),
        modalities=frozenset(data["modalities"]),
        languages=frozenset(data["languages"]),
        legacy_task_map=dict(data["legacy_task_map"]),
    )
