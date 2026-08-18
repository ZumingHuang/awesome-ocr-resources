from __future__ import annotations

import httpx

from ocr_resources.discovery.base import (
    DiscoveryWindow,
    RawCandidate,
    get_with_retry,
    parse_datetime,
)
from ocr_resources.models import ResourceKind


class GitHubCollector:
    name = "github"

    def __init__(
        self,
        endpoint: str,
        code_queries: list[str],
        skill_queries: list[str],
        *,
        minimum_stars: int = 10,
        token: str | None = None,
        client: httpx.Client | None = None,
    ) -> None:
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "awesome-ocr-resources/0.1",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self.endpoint = endpoint.rstrip("/")
        self.code_queries = code_queries
        self.skill_queries = skill_queries
        self.minimum_stars = minimum_stars
        self.client = client or httpx.Client(timeout=30, follow_redirects=True, headers=headers)

    def collect(self, window: DiscoveryWindow) -> list[RawCandidate]:
        candidates = self._collect_repositories(window)
        candidates.extend(self._collect_skills(window))
        unique = {(candidate.kind, candidate.source_id): candidate for candidate in candidates}
        return list(unique.values())

    def _collect_repositories(self, window: DiscoveryWindow) -> list[RawCandidate]:
        candidates: list[RawCandidate] = []
        for query in self.code_queries:
            qualified = (
                f"{query} created:{window.since.isoformat()}..{window.until.isoformat()} "
                f"stars:>={self.minimum_stars} fork:false"
            )
            response = get_with_retry(
                self.client,
                f"{self.endpoint}/search/repositories",
                params={"q": qualified, "sort": "updated", "per_page": window.limit},
            )
            payload = response.json()
            for item in payload.get("items", []):
                if item.get("fork"):
                    continue
                created = parse_datetime(item.get("created_at"))
                if not created:
                    continue
                candidates.append(
                    RawCandidate(
                        source=self.name,
                        source_id=str(item.get("node_id") or item["full_name"]),
                        kind=ResourceKind.CODE,
                        name=item["full_name"],
                        canonical_url=item["html_url"],
                        released_at=created.date(),
                        summary=item.get("description") or "",
                        tags=[str(topic) for topic in item.get("topics", [])],
                        metadata={
                            "repository": item["full_name"],
                            "stars": item.get("stargazers_count", 0),
                            "language": item.get("language"),
                            "archived": item.get("archived", False),
                            "query": query,
                        },
                    )
                )
        return candidates

    def _collect_skills(self, window: DiscoveryWindow) -> list[RawCandidate]:
        candidates: list[RawCandidate] = []
        for query in self.skill_queries:
            response = get_with_retry(
                self.client,
                f"{self.endpoint}/search/code",
                params={"q": query, "per_page": min(window.limit, 100)},
            )
            payload = response.json()
            for item in payload.get("items", []):
                repository = item["repository"]
                path = item["path"]
                source_id = f"{repository['full_name']}:{path}"
                candidates.append(
                    RawCandidate(
                        source=self.name,
                        source_id=source_id,
                        kind=ResourceKind.SKILL,
                        name=f"{repository['full_name']} / {path}",
                        canonical_url=item["html_url"],
                        released_at=window.until,
                        summary="OCR or document workflow declared in SKILL.md.",
                        tags=["skill", "ocr"],
                        metadata={
                            "repository": repository["full_name"],
                            "manifest_path": path,
                            "ecosystem": "agent-skills",
                            "query": query,
                        },
                    )
                )
        return candidates
