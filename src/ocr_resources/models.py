from __future__ import annotations

from datetime import date
from enum import StrEnum
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, model_validator


class ResourceKind(StrEnum):
    PAPER = "paper"
    MODEL = "model"
    DATASET = "dataset"
    CODE = "code"
    SKILL = "skill"
    PLATFORM = "platform"


class CurationStatus(StrEnum):
    CANDIDATE = "candidate"
    NEEDS_REVIEW = "needs-review"
    VERIFIED = "verified"
    STALE = "stale"
    ARCHIVED = "archived"


class DatePrecision(StrEnum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"
    UNKNOWN = "unknown"


class PartialDate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    value: str
    precision: DatePrecision

    @model_validator(mode="after")
    def validate_value(self) -> PartialDate:
        parts = self.value.split("-")
        expected = {
            DatePrecision.YEAR: 1,
            DatePrecision.MONTH: 2,
            DatePrecision.DAY: 3,
        }
        if self.precision == DatePrecision.UNKNOWN:
            if self.value != "unknown":
                raise ValueError("unknown date precision requires value 'unknown'")
            return self
        if len(parts) != expected[self.precision]:
            raise ValueError(f"date does not match {self.precision.value} precision")
        try:
            year = int(parts[0])
            month = int(parts[1]) if len(parts) > 1 else 1
            day = int(parts[2]) if len(parts) > 2 else 1
            date(year, month, day)
        except ValueError as exc:
            raise ValueError("invalid date") from exc
        return self


class ResourceLinks(BaseModel):
    model_config = ConfigDict(extra="allow")

    canonical: HttpUrl
    homepage: HttpUrl | None = None
    paper: HttpUrl | None = None
    code: HttpUrl | None = None
    model: HttpUrl | None = None
    dataset: HttpUrl | None = None
    documentation: HttpUrl | None = None


class LicenseInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = "NOASSERTION"
    url: HttpUrl | None = None


class Relation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    type: str


class LegacyProvenance(BaseModel):
    model_config = ConfigDict(extra="forbid")

    file: str
    line: int
    section: str
    title: str
    authors: str = ""
    tags: list[str] = Field(default_factory=list)
    links: list[dict[str, str]] = Field(default_factory=list)
    raw: list[str] = Field(default_factory=list)


class Provenance(BaseModel):
    model_config = ConfigDict(extra="allow")

    canonical_source: HttpUrl
    discovered_via: str
    discovered_at: date
    source_id: str | None = None
    source_metadata: dict[str, object] = Field(default_factory=dict)
    legacy: LegacyProvenance | None = None
    legacy_duplicates: list[LegacyProvenance] = Field(default_factory=list)


class Curation(BaseModel):
    model_config = ConfigDict(extra="allow")

    status: CurationStatus
    reviewer: str | None = None
    relevance_score: int | None = Field(default=None, ge=0, le=100)


class BaseResource(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal[1] = 1
    id: str
    kind: ResourceKind
    name: str = Field(min_length=1)
    released_at: PartialDate
    added_at: date
    last_verified_at: date
    summary: str = ""
    tasks: list[str] = Field(default_factory=list)
    modalities: list[str] = Field(default_factory=lambda: ["unspecified"])
    languages: list[str] = Field(default_factory=lambda: ["unspecified"])
    links: ResourceLinks
    license: LicenseInfo = Field(default_factory=LicenseInfo)
    relations: list[Relation] = Field(default_factory=list)
    provenance: Provenance
    curation: Curation


class PaperResource(BaseResource):
    kind: Literal[ResourceKind.PAPER]
    authors: list[str]
    year: int
    venue: str | None = None
    publication_status: Literal["preprint", "accepted", "published", "unknown"] = "unknown"
    arxiv_id: str | None = None
    doi: str | None = None


class ModelResource(BaseResource):
    kind: Literal[ResourceKind.MODEL]
    provider: str
    repository_id: str | None = None
    parameter_count: int | None = Field(default=None, ge=0)
    open_weights: bool | None = None
    deployment: list[str] = Field(default_factory=list)


class DatasetResource(BaseResource):
    kind: Literal[ResourceKind.DATASET]
    provider: str | None = None
    repository_id: str | None = None
    usage: list[Literal["train", "pretrain", "validation", "benchmark"]]
    sample_count: int | None = Field(default=None, ge=0)
    annotations: list[str] = Field(default_factory=list)
    access: Literal["open", "gated", "application", "unknown"] = "unknown"


class CodeResource(BaseResource):
    kind: Literal[ResourceKind.CODE]
    repository: str
    official: bool | None = None
    landmark: bool = False
    programming_languages: list[str] = Field(default_factory=list)
    maintenance_status: Literal["active", "inactive", "archived", "unknown"] = "unknown"


class SkillCapabilities(BaseModel):
    model_config = ConfigDict(extra="forbid")

    executes_commands: bool | None = None
    network_access: bool | None = None
    requires_credentials: bool | None = None


class SkillResource(BaseResource):
    kind: Literal[ResourceKind.SKILL]
    ecosystem: str
    repository: str
    manifest_path: str
    install: str | None = None
    capabilities: SkillCapabilities = Field(default_factory=SkillCapabilities)


class PlatformResource(BaseResource):
    kind: Literal[ResourceKind.PLATFORM]
    provider: str
    regions: list[str]
    delivery_modes: list[Literal["api", "saas", "on-premise", "sdk"]]


Resource = Annotated[
    PaperResource
    | ModelResource
    | DatasetResource
    | CodeResource
    | SkillResource
    | PlatformResource,
    Field(discriminator="kind"),
]

RESOURCE_MODEL_BY_KIND: dict[ResourceKind, type[BaseResource]] = {
    ResourceKind.PAPER: PaperResource,
    ResourceKind.MODEL: ModelResource,
    ResourceKind.DATASET: DatasetResource,
    ResourceKind.CODE: CodeResource,
    ResourceKind.SKILL: SkillResource,
    ResourceKind.PLATFORM: PlatformResource,
}
