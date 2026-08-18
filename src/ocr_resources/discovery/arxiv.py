from __future__ import annotations

import re
import time
import xml.etree.ElementTree as ET
from collections.abc import Callable
from urllib.parse import urlencode

import httpx

from ocr_resources.discovery.base import (
    DiscoveryWindow,
    RawCandidate,
    get_with_retry,
    parse_datetime,
)
from ocr_resources.identity import normalize_arxiv_id
from ocr_resources.models import ResourceKind

ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"

# arXiv's Terms of Use ask for no more than one request every three seconds.
ARXIV_MIN_INTERVAL_SECONDS = 3.0


class ArxivCollector:
    name = "arxiv"

    def __init__(
        self,
        endpoint: str,
        queries: list[str],
        *,
        client: httpx.Client | None = None,
        user_agent: str = "awesome-ocr-resources/0.1 (metadata curation)",
        min_interval: float = ARXIV_MIN_INTERVAL_SECONDS,
        sleep: Callable[[float], None] = time.sleep,
        monotonic: Callable[[], float] = time.monotonic,
    ) -> None:
        self.endpoint = endpoint
        self.queries = queries
        self.min_interval = min_interval
        self._sleep = sleep
        self._monotonic = monotonic
        self._last_request_at: float | None = None
        self.client = client or httpx.Client(
            timeout=httpx.Timeout(connect=10.0, read=30.0, write=10.0, pool=10.0),
            follow_redirects=True,
            headers={"User-Agent": user_agent},
        )

    def _throttle(self) -> None:
        """Space consecutive calls by at least ``min_interval`` seconds."""
        if self._last_request_at is not None:
            elapsed = self._monotonic() - self._last_request_at
            if elapsed < self.min_interval:
                self._sleep(self.min_interval - elapsed)
        self._last_request_at = self._monotonic()

    def collect(self, window: DiscoveryWindow) -> list[RawCandidate]:
        candidates: dict[str, RawCandidate] = {}
        for query in self.queries:
            params = {
                "search_query": query,
                "start": 0,
                "max_results": window.limit,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }
            self._throttle()
            response = get_with_retry(
                self.client,
                f"{self.endpoint}?{urlencode(params)}",
                sleep=self._sleep,
            )
            root = ET.fromstring(response.text)
            for entry in root.findall(f"{ATOM}entry"):
                identifier_url = (entry.findtext(f"{ATOM}id") or "").strip()
                arxiv_id = normalize_arxiv_id(identifier_url.rsplit("/", 1)[-1])
                published = parse_datetime(entry.findtext(f"{ATOM}published"))
                if not published or not (window.since <= published.date() <= window.until):
                    continue
                title = re.sub(r"\s+", " ", entry.findtext(f"{ATOM}title") or "").strip()
                summary = re.sub(r"\s+", " ", entry.findtext(f"{ATOM}summary") or "").strip()
                authors = [
                    (author.findtext(f"{ATOM}name") or "").strip()
                    for author in entry.findall(f"{ATOM}author")
                ]
                categories = [node.attrib["term"] for node in entry.findall(f"{ATOM}category")]
                doi = entry.findtext(f"{ARXIV}doi")
                candidates[arxiv_id] = RawCandidate(
                    source=self.name,
                    source_id=arxiv_id,
                    kind=ResourceKind.PAPER,
                    name=title,
                    canonical_url=f"https://arxiv.org/abs/{arxiv_id}",
                    released_at=published.date(),
                    summary=summary,
                    authors=authors,
                    tags=categories,
                    metadata={"arxiv_id": arxiv_id, "doi": doi, "query": query},
                )
        return list(candidates.values())
