from __future__ import annotations

from datetime import UTC

import httpx

from ocr_resources.discovery.base import DiscoveryWindow, RawCandidate, parse_datetime
from ocr_resources.models import ResourceKind


class HuggingFaceCollector:
    name = "huggingface"

    def __init__(
        self,
        endpoint: str,
        queries: list[str],
        *,
        token: str | None = None,
        client: httpx.Client | None = None,
    ) -> None:
        headers = {"User-Agent": "awesome-ocr-resources/0.1 (metadata curation)"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self.endpoint = endpoint.rstrip("/")
        self.queries = queries
        self.client = client or httpx.Client(timeout=30, follow_redirects=True, headers=headers)

    def collect(self, window: DiscoveryWindow) -> list[RawCandidate]:
        candidates: dict[tuple[ResourceKind, str], RawCandidate] = {}
        for kind, api_path in (
            (ResourceKind.MODEL, "models"),
            (ResourceKind.DATASET, "datasets"),
        ):
            for query in self.queries:
                response = self.client.get(
                    f"{self.endpoint}/{api_path}",
                    params={
                        "search": query,
                        "sort": "lastModified",
                        "direction": -1,
                        "limit": window.limit,
                        "full": "true",
                    },
                )
                response.raise_for_status()
                for item in response.json():
                    repository_id = item.get("id") or item.get("modelId")
                    if not repository_id:
                        continue
                    timestamp = parse_datetime(item.get("createdAt") or item.get("lastModified"))
                    if not timestamp:
                        continue
                    timestamp = timestamp.astimezone(UTC)
                    if not (window.since <= timestamp.date() <= window.until):
                        continue
                    tags = [str(tag) for tag in item.get("tags", [])]
                    description = item.get("description") or ""
                    namespace = "datasets/" if kind == ResourceKind.DATASET else ""
                    url = f"https://huggingface.co/{namespace}{repository_id}"
                    candidates[(kind, repository_id)] = RawCandidate(
                        source=self.name,
                        source_id=repository_id,
                        kind=kind,
                        name=repository_id,
                        canonical_url=url,
                        released_at=timestamp.date(),
                        summary=description,
                        tags=tags,
                        metadata={
                            "repository_id": repository_id,
                            "downloads": item.get("downloads", 0),
                            "likes": item.get("likes", 0),
                            "query": query,
                        },
                    )
        return list(candidates.values())
