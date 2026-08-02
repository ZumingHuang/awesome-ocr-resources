from __future__ import annotations

import json
from pathlib import Path

from pydantic import TypeAdapter

from ocr_resources.models import (
    BaseResource,
    CodeResource,
    DatasetResource,
    ModelResource,
    PaperResource,
    PlatformResource,
    Resource,
    SkillResource,
)

SCHEMA_MODELS: dict[str, type[BaseResource]] = {
    "common.schema.json": BaseResource,
    "paper.schema.json": PaperResource,
    "model.schema.json": ModelResource,
    "dataset.schema.json": DatasetResource,
    "code.schema.json": CodeResource,
    "skill.schema.json": SkillResource,
    "platform.schema.json": PlatformResource,
}


def build_schemas() -> dict[str, str]:
    schemas = {
        filename: json.dumps(model.model_json_schema(), ensure_ascii=False, indent=2) + "\n"
        for filename, model in SCHEMA_MODELS.items()
    }
    schemas["resource.schema.json"] = (
        json.dumps(TypeAdapter(Resource).json_schema(), ensure_ascii=False, indent=2) + "\n"
    )
    return schemas


def generate_schemas(root: Path, *, check: bool = False) -> list[Path]:
    changed: list[Path] = []
    for filename, content in build_schemas().items():
        path = root / "schemas" / filename
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old != content:
            changed.append(path.relative_to(root))
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
    return changed
