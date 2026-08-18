from __future__ import annotations

import random
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from email.utils import parsedate_to_datetime
from typing import Any, Protocol

import httpx

from ocr_resources.models import ResourceKind

RETRY_STATUS_CODES = frozenset({429, 500, 502, 503, 504})


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


def retry_after_seconds(response: httpx.Response, maximum: float) -> float | None:
    """Read a Retry-After header given either as seconds or as an HTTP date."""
    header = response.headers.get("Retry-After")
    if not header:
        return None
    try:
        return min(max(float(header), 0.0), maximum)
    except ValueError:
        pass
    try:
        target = parsedate_to_datetime(header)
    except (TypeError, ValueError):
        return None
    if target.tzinfo is None:
        target = target.replace(tzinfo=UTC)
    return min(max((target - datetime.now(UTC)).total_seconds(), 0.0), maximum)


def get_with_retry(
    client: httpx.Client,
    url: str,
    *,
    params: dict[str, Any] | None = None,
    attempts: int = 4,
    base_delay: float = 2.0,
    max_delay: float = 30.0,
    sleep: Callable[[float], None] = time.sleep,
) -> httpx.Response:
    """GET ``url``, retrying throttled, transient, and timed-out responses.

    Public metadata APIs throttle aggressively: arXiv answers a burst with 429
    "Rate exceeded" or by stalling the connection until the read timeout, so
    ``TransportError`` (which covers timeouts) is retried alongside the throttling
    and gateway status codes. Honour ``Retry-After`` when the server sends one,
    otherwise back off exponentially with jitter. The last failure is re-raised so
    a source that is genuinely down still surfaces as a source error.
    """
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        delay: float | None = None
        try:
            response = client.get(url, params=params)
        except httpx.TransportError as exc:
            last_error = exc
        else:
            if response.status_code not in RETRY_STATUS_CODES:
                response.raise_for_status()
                return response
            last_error = httpx.HTTPStatusError(
                f"{response.status_code} {response.reason_phrase} for {url}",
                request=response.request,
                response=response,
            )
            delay = retry_after_seconds(response, max_delay)
        if attempt == attempts:
            break
        if delay is None:
            delay = min(base_delay * 2 ** (attempt - 1), max_delay) * (0.5 + random.random() / 2)
        sleep(delay)
    if last_error is None:  # pragma: no cover - attempts is always at least one
        raise RuntimeError(f"no request was attempted for {url}")
    raise last_error
