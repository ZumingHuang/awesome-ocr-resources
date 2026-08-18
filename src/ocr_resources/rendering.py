from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from ocr_resources.models import PaperResource, Resource, ResourceKind
from ocr_resources.repository import load_resources

GENERATED_NOTICE = "<!-- Generated from data/*.yaml. Do not edit directly. -->"
LEGACY_PAPER_PATHS = {
    "before-2010": "papers/papers_by_year/before-2010.md",
    "2011-2014": "papers/papers_by_year/2011-2014.md",
    "2015-2018": "papers/papers_by_year/2015-2018.md",
    "2019-2022": "papers/papers_by_year/2019-2022.md",
    "2023-present": "papers/papers_by_year/2023-present.md",
}


@dataclass(frozen=True)
class RenderedFile:
    relative_path: Path
    content: str


def _environment(root: Path) -> Environment:
    environment = Environment(
        loader=FileSystemLoader(root / "templates"),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    environment.globals["generated_notice"] = GENERATED_NOTICE
    return environment


def _year_group(year: int) -> str:
    if year <= 2010:
        return "before-2010"
    if year <= 2014:
        return "2011-2014"
    if year <= 2018:
        return "2015-2018"
    if year <= 2022:
        return "2019-2022"
    return "2023-present"


def _resource_sort_key(resource: Resource) -> tuple[str, str]:
    released = resource.released_at.value if resource.released_at.value != "unknown" else "0000"
    return released, resource.name.casefold()


def _paper_view(resource: PaperResource) -> dict[str, Any]:
    legacy = resource.provenance.legacy
    links: list[dict[str, str]] = []
    if legacy:
        links = legacy.links
    else:
        for label in ("paper", "code", "homepage"):
            value = getattr(resource.links, label)
            if value:
                links.append({"label": label, "url": str(value)})
    return {
        "name": resource.name,
        "authors": ", ".join(resource.authors),
        "metadata": "".join(
            [f"\\[[{link['label']}]({link['url']})\\]" for link in links]
            + [f"\\[{task}\\]" for task in resource.tasks]
        ),
        "year": resource.year,
    }


def _resource_view(resource: Resource) -> dict[str, Any]:
    return {
        "name": resource.name,
        "url": str(resource.links.canonical),
        "summary": resource.summary,
        "tasks": ", ".join(resource.tasks),
        "released": resource.released_at.value,
        "status": resource.curation.status.value,
    }


def build_rendered_files(root: Path) -> list[RenderedFile]:
    resources = load_resources(root)
    environment = _environment(root)
    rendered: list[RenderedFile] = []

    papers = [resource for resource in resources if isinstance(resource, PaperResource)]
    grouped_papers: dict[str, dict[int, list[dict[str, Any]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for paper in papers:
        grouped_papers[_year_group(paper.year)][paper.year].append(_paper_view(paper))
    paper_template = environment.get_template("papers-by-year.md.j2")
    for group, path in LEGACY_PAPER_PATHS.items():
        sections = []
        for year in sorted(grouped_papers[group], reverse=True):
            entries = sorted(grouped_papers[group][year], key=lambda item: item["name"].casefold())
            sections.append({"year": year, "entries": entries})
        rendered.append(
            RenderedFile(
                Path(path), paper_template.render(group=group, sections=sections).rstrip() + "\n"
            )
        )

    by_kind: dict[ResourceKind, list[Resource]] = defaultdict(list)
    for resource in resources:
        by_kind[resource.kind].append(resource)
    list_template = environment.get_template("resource-list.md.j2")
    list_paths = {
        ResourceKind.PAPER: ("papers/README.md", "Papers"),
        ResourceKind.MODEL: ("models/README.md", "Models"),
        ResourceKind.DATASET: ("datasets/README.md", "Datasets"),
        ResourceKind.CODE: ("codes/README.md", "Codes"),
        ResourceKind.SKILL: ("skills/README.md", "Skills"),
        ResourceKind.PLATFORM: ("platforms/README.md", "Platforms"),
    }
    for kind, (path, title) in list_paths.items():
        sorted_resources = sorted(by_kind[kind], key=_resource_sort_key, reverse=True)
        entries = [_resource_view(item) for item in sorted_resources]
        rendered.append(
            RenderedFile(
                Path(path),
                list_template.render(title=title, kind=kind.value, entries=entries),
            )
        )

    counts = {kind.value: len(by_kind[kind]) for kind in ResourceKind}
    updates_root = root / "updates"
    latest_updates = (
        sorted(updates_root.glob("*/*.md"), reverse=True)[:10] if updates_root.exists() else []
    )
    update_views = [
        {"date": path.stem, "path": path.relative_to(root).as_posix()} for path in latest_updates
    ]
    context = {"counts": counts, "updates": update_views}
    rendered.append(
        RenderedFile(Path("README.md"), environment.get_template("README.md.j2").render(**context))
    )
    rendered.append(
        RenderedFile(
            Path("README.zh-CN.md"),
            environment.get_template("README.zh-CN.md.j2").render(**context),
        )
    )
    return rendered


def render_repository(root: Path, *, check: bool = False) -> list[Path]:
    changed: list[Path] = []
    for rendered in build_rendered_files(root):
        path = root / rendered.relative_path
        existing = path.read_text(encoding="utf-8") if path.exists() else None
        if existing != rendered.content:
            changed.append(rendered.relative_path)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(rendered.content, encoding="utf-8")
    return changed


def write_daily_update(
    root: Path,
    resources: list[Resource],
    update_date: date,
    *,
    source_summary: dict[str, int] | None = None,
    source_errors: list[dict[str, str]] | None = None,
) -> Path | None:
    if not resources:
        return None
    environment = _environment(root)
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for resource in sorted(resources, key=lambda item: (item.kind.value, item.name.casefold())):
        grouped[resource.kind.value].append(_resource_view(resource))
    path = root / "updates" / str(update_date.year) / f"{update_date.isoformat()}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        environment.get_template("daily-update.md.j2").render(
            update_date=update_date.isoformat(),
            grouped=dict(grouped),
            source_summary=source_summary or {},
            source_errors=source_errors or [],
        ),
        encoding="utf-8",
    )
    return path
