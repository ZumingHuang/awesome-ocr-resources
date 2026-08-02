from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path
from typing import Any

import yaml
from pydantic import TypeAdapter

from ocr_resources.identity import canonical_key
from ocr_resources.models import BaseResource, PaperResource, Resource, ResourceKind

RESOURCE_ADAPTER: TypeAdapter[Resource] = TypeAdapter(Resource)
KIND_TO_DIRECTORY = {
    ResourceKind.PAPER: "papers",
    ResourceKind.MODEL: "models",
    ResourceKind.DATASET: "datasets",
    ResourceKind.CODE: "codes",
    ResourceKind.SKILL: "skills",
    ResourceKind.PLATFORM: "platforms",
}


def dump_resource(resource: BaseResource) -> str:
    data = resource.model_dump(mode="json", exclude_none=True)
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100)


def write_resource(root: Path, resource: BaseResource, relative_path: Path | None = None) -> Path:
    if relative_path is None:
        relative_path = default_resource_path(resource)
    destination = root / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(dump_resource(resource), encoding="utf-8")
    return destination


def default_resource_path(resource: BaseResource) -> Path:
    directory = KIND_TO_DIRECTORY[resource.kind]
    identifier = resource.id.removeprefix(f"{resource.kind.value}:")
    identifier = identifier.replace(":", "--").replace("/", "--")
    if isinstance(resource, PaperResource):
        return Path("data") / directory / str(resource.year) / f"{identifier}.yaml"
    return Path("data") / directory / f"{identifier}.yaml"


def iter_resource_paths(root: Path) -> Iterable[Path]:
    data_root = root / "data"
    if not data_root.exists():
        return []
    return sorted(path for path in data_root.glob("**/*.yaml") if path.is_file())


def load_resource(path: Path) -> Resource:
    raw: Any = yaml.safe_load(path.read_text(encoding="utf-8"))
    return RESOURCE_ADAPTER.validate_python(raw)


def load_resources(root: Path) -> list[Resource]:
    return [load_resource(path) for path in iter_resource_paths(root)]


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    resources: list[tuple[Path, Resource]] = []
    for path in iter_resource_paths(root):
        try:
            resources.append((path, load_resource(path)))
        except Exception as exc:  # Pydantic supplies actionable nested diagnostics.
            errors.append(f"{path.relative_to(root)}: {exc}")
    seen_ids: dict[str, Path] = {}
    seen_keys: dict[str, Path] = {}
    all_ids = {resource.id for _, resource in resources}
    for path, resource in resources:
        if resource.id in seen_ids:
            errors.append(
                f"duplicate id {resource.id}: {seen_ids[resource.id].relative_to(root)} and "
                f"{path.relative_to(root)}"
            )
        seen_ids[resource.id] = path
        key = canonical_key(resource)
        if key in seen_keys:
            errors.append(
                f"duplicate canonical key {key}: {seen_keys[key].relative_to(root)} and "
                f"{path.relative_to(root)}"
            )
        seen_keys[key] = path
        for relation in resource.relations:
            if relation.id not in all_ids:
                errors.append(f"{path.relative_to(root)}: unknown relation target {relation.id}")
        if resource.added_at > resource.last_verified_at:
            errors.append(f"{path.relative_to(root)}: added_at is after last_verified_at")
    return errors
