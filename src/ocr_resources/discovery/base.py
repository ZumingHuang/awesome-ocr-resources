from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, Protocol

from ocr_resources.models import ResourceKind


@dataclass(frozen=True)
class DiscoveryWindow:
    since: date
    until: date
    limit: int = 50


@dataclass
class RawCandidate:
    source: str
    source_id: str
    kind: ResourceKind
    name: str
    canonical_url: str
    released_at: date | None
    summary: str = ""
    authors: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


class Collector(Protocol):
    name: str

    def collect(self, window: DiscoveryWindow) -> list[RawCandidate]: ...


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))
