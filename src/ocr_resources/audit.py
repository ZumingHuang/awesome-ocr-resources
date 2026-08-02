from __future__ import annotations

import ipaddress
import json
import socket
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlsplit

import httpx

from ocr_resources.repository import load_resources

MAX_REDIRECTS = 5


def _ip_is_public(value: str) -> bool:
    address = ipaddress.ip_address(value)
    return address.is_global


def validate_public_url(url: str, *, resolve_dns: bool = False) -> str | None:
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"}:
        return "only HTTP(S) URLs are allowed"
    host = parsed.hostname
    if not host:
        return "URL has no hostname"
    if host.casefold() == "localhost" or host.casefold().endswith(".localhost"):
        return "localhost is not allowed"
    try:
        if not _ip_is_public(host):
            return "non-public IP address is not allowed"
    except ValueError:
        pass
    if resolve_dns:
        try:
            addresses = {str(item[4][0]) for item in socket.getaddrinfo(host, parsed.port or 443)}
        except OSError as exc:
            return f"DNS resolution failed: {exc}"
        if not addresses or any(not _ip_is_public(value) for value in addresses):
            return "hostname resolves to a non-public IP address"
    return None


def check_url(client: httpx.Client, url: str) -> dict[str, Any]:
    current = url
    for _redirect_count in range(MAX_REDIRECTS + 1):
        safety_error = validate_public_url(current, resolve_dns=True)
        if safety_error:
            return {"url": url, "status": "unsafe", "detail": safety_error}
        try:
            response = client.head(current, follow_redirects=False)
            if response.status_code in {403, 405}:
                response = client.get(current, follow_redirects=False)
        except httpx.HTTPError as exc:
            return {"url": url, "status": "error", "detail": str(exc)}
        if response.is_redirect:
            location = response.headers.get("location")
            if not location:
                return {"url": url, "status": "error", "detail": "redirect has no location"}
            current = urljoin(current, location)
            continue
        return {
            "url": url,
            "final_url": current,
            "status": "ok" if response.is_success else "error",
            "status_code": response.status_code,
        }
    return {"url": url, "status": "error", "detail": "too many redirects"}


def audit_links(root: Path, *, timeout: float = 15.0) -> dict[str, Any]:
    urls = sorted({str(resource.links.canonical) for resource in load_resources(root)})
    with httpx.Client(
        timeout=timeout,
        headers={"User-Agent": "awesome-ocr-resources/0.1 (link audit)"},
    ) as client:
        results = [check_url(client, url) for url in urls]
    report: dict[str, Any] = {
        "checked": len(results),
        "ok": sum(result["status"] == "ok" for result in results),
        "failed": sum(result["status"] != "ok" for result in results),
        "results": results,
    }
    reports = root / "reports"
    reports.mkdir(exist_ok=True)
    (reports / "link-audit.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report
