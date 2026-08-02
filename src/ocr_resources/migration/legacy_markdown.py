from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from ocr_resources.identity import normalize_arxiv_id, slugify
from ocr_resources.models import (
    Curation,
    CurationStatus,
    DatasetResource,
    DatePrecision,
    LegacyProvenance,
    LicenseInfo,
    PaperResource,
    PartialDate,
    Provenance,
    ResourceKind,
    ResourceLinks,
)
from ocr_resources.repository import load_resource, write_resource
from ocr_resources.taxonomy import Taxonomy, load_taxonomy

MIGRATION_DATE = date(2026, 7, 26)
PAPER_FILES = [
    "before-2010.md",
    "2011-2014.md",
    "2015-2018.md",
    "2019-2022.md",
    "2023-present.md",
]
LEGACY_ROOT = Path("legacy")
VENUE_NAMES = {
    "AAAI",
    "BMVC",
    "CVPR",
    "ECCV",
    "Frontiers of Computer Science",
    "ICCV",
    "ICDAR",
    "ICLR",
    "ICPR",
    "IJDAR",
    "IJCAI",
    "IJCV",
    "NIPS",
    "NIPS (workshop)",
    "PR",
    "TIP",
    "TMM",
    "TPAMI",
    "Thesis",
}
LINK_PATTERN = re.compile(r"\\?\[\[([^\]]+)\]\(([^)]+)\)\\?\]")
BARE_PATTERN = re.compile(r"\\\[([^\[\]]+)\\\]")
ARXIV_PATTERN = re.compile(r"arxiv\.org/(?:abs|pdf)/(?:abs/)?([^/?#]+?)(?:\.pdf)?$")


@dataclass
class ParsedPaper:
    year: int
    section: str
    title: str
    authors_raw: str
    link_line: str
    source_file: str
    source_line: int
    raw: list[str]
    links: list[tuple[str, str]] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass
class MigrationReport:
    paper_input: int = 0
    paper_output: int = 0
    paper_unique: int = 0
    dataset_input: int = 0
    dataset_output: int = 0
    warnings: list[dict[str, object]] = field(default_factory=list)
    mappings: dict[str, int] = field(default_factory=dict)
    unresolved_tags: dict[str, int] = field(default_factory=dict)

    def warn(self, source: str, line: int, message: str) -> None:
        self.warnings.append({"source": source, "line": line, "message": message})

    def as_dict(self) -> dict[str, object]:
        return {
            "paper_input": self.paper_input,
            "paper_output": self.paper_output,
            "paper_unique": self.paper_unique,
            "dataset_input": self.dataset_input,
            "dataset_output": self.dataset_output,
            "warnings": self.warnings,
            "mappings": dict(sorted(self.mappings.items())),
            "unresolved_tags": dict(sorted(self.unresolved_tags.items())),
        }


def _clean_markdown_text(value: str) -> str:
    value = value.strip().removesuffix("  ").strip()
    if value.startswith("**") and value.endswith("**"):
        value = value[2:-2]
    return value.strip()


def _infer_year(title: str, links: list[tuple[str, str]], fallback: int | None) -> int:
    if fallback is not None:
        return fallback
    for label, url in links:
        for value in (label, url):
            years = re.findall(r"(?:19|20)\d{2}", value)
            if years:
                return int(years[-1])
    raise ValueError(f"cannot infer year for {title}")


def _parse_link_line(value: str) -> tuple[list[tuple[str, str]], list[str]]:
    links = LINK_PATTERN.findall(value)
    without_links = LINK_PATTERN.sub("", value)
    tags = BARE_PATTERN.findall(without_links)
    return links, tags


def parse_paper_file(path: Path) -> list[ParsedPaper]:
    lines = path.read_text(encoding="utf-8").splitlines()
    entries: list[ParsedPaper] = []
    section = ""
    section_year: int | None = None
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if line.startswith("## "):
            section = line[3:].strip()
            section_year = int(section) if section.isdigit() else None
            index += 1
            continue
        if not line:
            index += 1
            continue
        if index + 2 >= len(lines):
            raise ValueError(f"incomplete paper entry at {path}:{index + 1}")
        title_line = lines[index]
        author_line = lines[index + 1]
        link_line = lines[index + 2]
        if link_line.startswith("\\[") is False:
            raise ValueError(f"expected links at {path}:{index + 3}: {link_line}")
        title = _clean_markdown_text(title_line)
        links, tags = _parse_link_line(link_line)
        year = _infer_year(title, links, section_year)
        warnings: list[str] = []
        if not title_line.strip().startswith("**"):
            warnings.append("title was not bold in legacy Markdown")
        entries.append(
            ParsedPaper(
                year=year,
                section=section,
                title=title,
                authors_raw=_clean_markdown_text(author_line),
                link_line=link_line,
                source_file=path.as_posix(),
                source_line=index + 1,
                raw=[title_line, author_line, link_line],
                links=links,
                tags=tags,
                warnings=warnings,
            )
        )
        index += 3
    return entries


def _canonical_link(links: list[tuple[str, str]]) -> tuple[str, str | None, str | None, str | None]:
    paper_url: str | None = None
    code_url: str | None = None
    homepage_url: str | None = None
    for label, url in links:
        lowered = label.casefold()
        if lowered in {"code"}:
            code_url = code_url or url
        elif lowered in {"homepage"}:
            homepage_url = homepage_url or url
        elif lowered not in {"supp", "supplement", "slides", "video"}:
            paper_url = paper_url or url
    canonical = paper_url or homepage_url or code_url
    if canonical is None:
        raise ValueError("paper has no usable URL")
    return canonical, paper_url, code_url, homepage_url


def _paper_id(entry: ParsedPaper, existing: set[str]) -> tuple[str, str | None, bool]:
    arxiv_id = None
    for _, url in entry.links:
        match = ARXIV_PATTERN.search(url.rstrip("/"))
        if match:
            arxiv_id = normalize_arxiv_id(match.group(1))
            candidate = f"paper:arxiv:{arxiv_id}"
            if candidate not in existing:
                return candidate, arxiv_id, False
            return candidate, arxiv_id, True
    base = f"paper:legacy:{entry.year}:{slugify(entry.title)}"
    candidate = base
    suffix = 2
    while candidate in existing:
        candidate = f"{base}-{suffix}"
        suffix += 1
    return candidate, arxiv_id, False


def _legacy_provenance(entry: ParsedPaper) -> LegacyProvenance:
    return LegacyProvenance(
        file=entry.source_file,
        line=entry.source_line,
        section=entry.section,
        title=entry.title,
        authors=entry.authors_raw,
        tags=entry.tags,
        links=[{"label": label, "url": url} for label, url in entry.links],
        raw=entry.raw,
    )


def _paper_identity(entry: ParsedPaper) -> str:
    for _, url in entry.links:
        match = ARXIV_PATTERN.search(url.rstrip("/"))
        if match:
            return f"arxiv:{normalize_arxiv_id(match.group(1))}"
    return f"title:{slugify(entry.title)}:{entry.year}"


def _merge_duplicate_paper(
    root: Path,
    destination: Path,
    entry: ParsedPaper,
    taxonomy: Taxonomy,
    report: MigrationReport,
) -> None:
    resource = load_resource(destination)
    if not isinstance(resource, PaperResource):
        raise TypeError(f"expected paper resource at {destination}")
    resource.provenance.legacy_duplicates.append(_legacy_provenance(entry))
    for task in entry.tags:
        mapped = taxonomy.map_legacy_task(task)
        if mapped and mapped not in resource.tasks:
            resource.tasks.append(mapped)
    write_resource(root, resource, destination.relative_to(root))
    report.warn(
        entry.source_file,
        entry.source_line,
        f"merged duplicate legacy occurrence into {resource.id}",
    )


def _paper_to_resource(
    entry: ParsedPaper,
    taxonomy: Taxonomy,
    existing: set[str],
    report: MigrationReport,
) -> PaperResource:
    canonical, paper_url, code_url, homepage_url = _canonical_link(entry.links)
    tasks: list[str] = []
    venue: str | None = None
    for label, _ in entry.links:
        if label in VENUE_NAMES or re.match(r"^(CVPR|ECCV|ICCV|BMVC) \d{4}$", label):
            venue = venue or label
    for tag in entry.tags:
        mapped = taxonomy.map_legacy_task(tag)
        if mapped:
            if mapped not in tasks:
                tasks.append(mapped)
            key = f"{tag} -> {mapped}"
            report.mappings[key] = report.mappings.get(key, 0) + 1
        elif tag in VENUE_NAMES:
            venue = venue or tag
        else:
            report.unresolved_tags[tag] = report.unresolved_tags.get(tag, 0) + 1
            report.warn(entry.source_file, entry.source_line, f"unresolved legacy tag: {tag}")
    for warning in entry.warnings:
        report.warn(entry.source_file, entry.source_line, warning)
    resource_id, arxiv_id, duplicate = _paper_id(entry, existing)
    if duplicate:
        raise ValueError(f"duplicate paper identity {resource_id}")
    existing.add(resource_id)
    authors = [author.strip() for author in entry.authors_raw.split(",") if author.strip()]
    return PaperResource(
        id=resource_id,
        kind=ResourceKind.PAPER,
        name=entry.title,
        released_at=PartialDate(value=str(entry.year), precision=DatePrecision.YEAR),
        added_at=MIGRATION_DATE,
        last_verified_at=MIGRATION_DATE,
        tasks=tasks or ["other"],
        modalities=["unspecified"],
        languages=["unspecified"],
        links=ResourceLinks.model_validate(
            {
                "canonical": canonical,
                "paper": paper_url,
                "code": code_url,
                "homepage": homepage_url,
            }
        ),
        license=LicenseInfo(),
        provenance=Provenance.model_validate(
            {
                "canonical_source": canonical,
                "discovered_via": "legacy-markdown",
                "discovered_at": MIGRATION_DATE,
                "legacy": _legacy_provenance(entry),
            }
        ),
        curation=Curation(status=CurationStatus.NEEDS_REVIEW),
        authors=authors,
        year=entry.year,
        venue=venue,
        publication_status="published" if venue else "unknown",
        arxiv_id=arxiv_id,
    )


def _dataset_to_resource(
    name: str,
    url: str,
    legacy_tasks: list[str],
    source_line: int,
    taxonomy: Taxonomy,
    report: MigrationReport,
) -> DatasetResource:
    tasks: list[str] = []
    for task in legacy_tasks:
        mapped = taxonomy.map_legacy_task(task)
        if mapped and mapped not in tasks:
            tasks.append(mapped)
            key = f"{task} -> {mapped}"
            report.mappings[key] = report.mappings.get(key, 0) + 1
        elif not mapped:
            report.unresolved_tags[task] = report.unresolved_tags.get(task, 0) + 1
            report.warn(
                "legacy/datasets/README.md", source_line, f"unresolved dataset task: {task}"
            )
    repository_id: str | None = None
    parsed = urlparse(url)
    if parsed.netloc == "huggingface.co" and parsed.path.startswith("/datasets/"):
        repository_id = parsed.path.removeprefix("/datasets/").strip("/")
    return DatasetResource(
        id=f"dataset:legacy:{slugify(name)}",
        kind=ResourceKind.DATASET,
        name=name,
        released_at=PartialDate(value="unknown", precision=DatePrecision.UNKNOWN),
        added_at=MIGRATION_DATE,
        last_verified_at=MIGRATION_DATE,
        tasks=tasks or ["other"],
        modalities=["unspecified"],
        languages=["unspecified"],
        links=ResourceLinks.model_validate({"canonical": url, "dataset": url}),
        license=LicenseInfo(),
        provenance=Provenance.model_validate(
            {
                "canonical_source": url,
                "discovered_via": "legacy-markdown",
                "discovered_at": MIGRATION_DATE,
                "legacy": LegacyProvenance(
                    file="legacy/datasets/README.md",
                    line=source_line,
                    section="Overview",
                    title=name,
                    tags=legacy_tasks,
                    links=[{"label": "dataset", "url": url}],
                    raw=[f"| [{name}]({url}) | {','.join(legacy_tasks)} |"],
                ),
            }
        ),
        curation=Curation(status=CurationStatus.NEEDS_REVIEW),
        repository_id=repository_id,
        usage=[],
        access="unknown",
    )


def migrate_legacy(root: Path, *, force: bool = False) -> MigrationReport:
    taxonomy = load_taxonomy(root)
    data_root = root / "data"
    if data_root.exists() and any(data_root.glob("**/*.yaml")):
        if not force:
            raise FileExistsError(
                "data already contains YAML resources; pass --force to replace them"
            )
        shutil.rmtree(data_root)
    for directory in ("papers", "models", "datasets", "codes", "skills", "platforms"):
        (data_root / directory).mkdir(parents=True, exist_ok=True)
    report = MigrationReport()
    existing_ids: set[str] = set()
    identity_paths: dict[str, Path] = {}
    for filename in PAPER_FILES:
        path = root / LEGACY_ROOT / "papers" / "papers_by_year" / filename
        entries = parse_paper_file(path)
        for entry in entries:
            entry.source_file = path.relative_to(root).as_posix()
        report.paper_input += len(entries)
        for entry in entries:
            identity = _paper_identity(entry)
            if identity in identity_paths:
                _merge_duplicate_paper(root, identity_paths[identity], entry, taxonomy, report)
                report.paper_output += 1
                continue
            paper_resource = _paper_to_resource(entry, taxonomy, existing_ids, report)
            destination = write_resource(root, paper_resource)
            identity_paths[identity] = destination
            report.paper_output += 1
            report.paper_unique += 1
    dataset_path = root / LEGACY_ROOT / "datasets" / "README.md"
    row_pattern = re.compile(r"^\| \[([^]]+)\]\(([^)]+)\) \| ([^|]+) \|$")
    for line_number, line in enumerate(dataset_path.read_text(encoding="utf-8").splitlines(), 1):
        match = row_pattern.match(line)
        if not match:
            continue
        name, url, task_text = match.groups()
        legacy_tasks = [value.strip() for value in task_text.split(",")]
        report.dataset_input += 1
        dataset_resource = _dataset_to_resource(
            name, url, legacy_tasks, line_number, taxonomy, report
        )
        write_resource(root, dataset_resource)
        report.dataset_output += 1
    if (report.paper_input, report.paper_output, report.paper_unique) != (233, 233, 232):
        raise RuntimeError(
            "paper migration count mismatch: "
            f"{report.paper_input}/{report.paper_output}/{report.paper_unique}"
        )
    if (report.dataset_input, report.dataset_output) != (27, 27):
        raise RuntimeError(
            f"dataset migration count mismatch: {report.dataset_input}/{report.dataset_output}"
        )
    reports = root / "reports"
    reports.mkdir(exist_ok=True)
    (reports / "legacy-migration.json").write_text(
        json.dumps(report.as_dict(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    for directory in ("models", "codes", "skills", "platforms"):
        (data_root / directory / ".gitkeep").touch()
    return report
