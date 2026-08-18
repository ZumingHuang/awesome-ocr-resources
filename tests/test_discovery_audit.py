from __future__ import annotations

from datetime import date

import httpx
import pytest

from ocr_resources.audit import validate_public_url
from ocr_resources.discovery.arxiv import ArxivCollector
from ocr_resources.discovery.base import DiscoveryWindow, RawCandidate, get_with_retry
from ocr_resources.discovery.github import GitHubCollector
from ocr_resources.discovery.huggingface import HuggingFaceCollector
from ocr_resources.discovery.scoring import score_candidate
from ocr_resources.models import ResourceKind


def test_arxiv_collector_parses_atom_response() -> None:
    atom = """<?xml version="1.0" encoding="UTF-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
      <entry>
        <id>https://arxiv.org/abs/2607.12345v2</id>
        <published>2026-07-25T12:00:00Z</published>
        <title>Daily OCR Paper</title>
        <summary>Optical character recognition for documents.</summary>
        <author><name>Alice Example</name></author>
        <category term="cs.CV" />
      </entry>
    </feed>"""
    transport = httpx.MockTransport(lambda request: httpx.Response(200, text=atom))
    client = httpx.Client(transport=transport)
    collector = ArxivCollector("https://example.test/query", ["all:ocr"], client=client)
    values = collector.collect(DiscoveryWindow(date(2026, 7, 20), date(2026, 7, 26)))
    assert len(values) == 1
    assert values[0].source_id == "2607.12345"
    assert values[0].authors == ["Alice Example"]


def test_arxiv_collector_paces_requests_per_terms_of_use() -> None:
    empty = '<?xml version="1.0" encoding="UTF-8"?><feed xmlns="http://www.w3.org/2005/Atom"/>'
    client = httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(200, text=empty)))
    slept: list[float] = []
    collector = ArxivCollector(
        "https://example.test/query",
        ["all:a", "all:b", "all:c"],
        client=client,
        sleep=slept.append,
        monotonic=lambda: 0.0,
    )
    collector.collect(DiscoveryWindow(date(2026, 7, 20), date(2026, 7, 26)))
    assert slept == [3.0, 3.0]


def test_get_with_retry_recovers_from_throttling() -> None:
    replies = [httpx.Response(429, text="Rate exceeded."), httpx.Response(200, text="ok")]
    client = httpx.Client(transport=httpx.MockTransport(lambda _: replies.pop(0)))
    slept: list[float] = []
    response = get_with_retry(client, "https://example.test/q", sleep=slept.append)
    assert response.status_code == 200
    assert len(slept) == 1


def test_get_with_retry_honours_retry_after() -> None:
    replies = [
        httpx.Response(429, headers={"Retry-After": "7"}, text="Rate exceeded."),
        httpx.Response(200, text="ok"),
    ]
    client = httpx.Client(transport=httpx.MockTransport(lambda _: replies.pop(0)))
    slept: list[float] = []
    get_with_retry(client, "https://example.test/q", sleep=slept.append)
    assert slept == [7.0]


def test_get_with_retry_reraises_persistent_throttling() -> None:
    client = httpx.Client(
        transport=httpx.MockTransport(lambda _: httpx.Response(429, text="Rate exceeded."))
    )
    slept: list[float] = []
    with pytest.raises(httpx.HTTPStatusError):
        get_with_retry(client, "https://example.test/q", attempts=3, sleep=slept.append)
    assert len(slept) == 2


def test_get_with_retry_reraises_timeouts() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("The read operation timed out", request=request)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    slept: list[float] = []
    with pytest.raises(httpx.ReadTimeout):
        get_with_retry(client, "https://example.test/q", attempts=2, sleep=slept.append)
    assert len(slept) == 1


def test_get_with_retry_does_not_retry_client_errors() -> None:
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        return httpx.Response(404)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    with pytest.raises(httpx.HTTPStatusError):
        get_with_retry(client, "https://example.test/q", sleep=lambda _: None)
    assert len(calls) == 1


def test_huggingface_collector_handles_models_and_datasets() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        name = "org/ocr-data" if request.url.path.endswith("datasets") else "org/ocr-model"
        return httpx.Response(
            200,
            json=[
                {
                    "id": name,
                    "createdAt": "2026-07-25T12:00:00Z",
                    "tags": ["ocr"],
                    "downloads": 100,
                }
            ],
        )

    client = httpx.Client(transport=httpx.MockTransport(handler))
    collector = HuggingFaceCollector("https://example.test/api", ["OCR"], client=client)
    values = collector.collect(DiscoveryWindow(date(2026, 7, 20), date(2026, 7, 26)))
    assert {value.kind for value in values} == {ResourceKind.MODEL, ResourceKind.DATASET}


def test_github_collector_does_not_fetch_or_execute_discovered_content() -> None:
    requested: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requested.append(request.url.path)
        if request.url.path.endswith("repositories"):
            return httpx.Response(200, json={"items": []})
        return httpx.Response(
            200,
            json={
                "items": [
                    {
                        "path": ".claude/skills/ocr/SKILL.md",
                        "html_url": "https://github.com/org/repo/blob/main/SKILL.md",
                        "repository": {"full_name": "org/repo"},
                    }
                ]
            },
        )

    client = httpx.Client(transport=httpx.MockTransport(handler))
    collector = GitHubCollector(
        "https://example.test", [], ["OCR filename:SKILL.md"], client=client
    )
    values = collector.collect(DiscoveryWindow(date(2026, 7, 20), date(2026, 7, 26)))
    assert len(values) == 1
    assert values[0].kind == ResourceKind.SKILL
    assert requested == ["/search/code"]


def test_scoring_requires_relevance() -> None:
    rules = {
        "thresholds": {"draft_pr": 65},
        "weights": {
            "relevance": 30,
            "authority": 20,
            "completeness": 15,
            "usability": 15,
            "impact": 10,
            "freshness": 10,
        },
        "required_terms": ["OCR", "document"],
    }
    candidate = RawCandidate(
        source="test",
        source_id="1",
        kind=ResourceKind.CODE,
        name="An OCR toolkit",
        canonical_url="https://example.com/ocr",
        released_at=date(2026, 7, 25),
        summary="Document parsing.",
        metadata={"stars": 100},
    )
    score = score_candidate(candidate, rules)
    assert score.total == 100
    assert score.eligible


def test_public_url_safety() -> None:
    assert validate_public_url("https://example.com/resource") is None
    assert validate_public_url("file:///etc/passwd") is not None
    assert validate_public_url("http://localhost/admin") is not None
    assert validate_public_url("http://127.0.0.1/admin") is not None
    assert validate_public_url("http://169.254.169.254/latest/meta-data") is not None
    assert validate_public_url("http://10.0.0.1/internal") is not None
