from __future__ import annotations

import re
import unicodedata
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from ocr_resources.models import (
    CodeResource,
    DatasetResource,
    ModelResource,
    PaperResource,
    PlatformResource,
    Resource,
    SkillResource,
)

_TRACKING_PARAMETERS = {
    "fbclid",
    "gclid",
    "ref",
    "source",
    "utm_campaign",
    "utm_medium",
    "utm_source",
}


def slugify(value: str, max_length: int = 80) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value[:max_length].rstrip("-") or "resource"


def normalize_title(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    return " ".join(re.findall(r"\w+", value))


def canonicalize_url(value: str) -> str:
    split = urlsplit(value)
    scheme = split.scheme.lower()
    host = (split.hostname or "").lower()
    port = split.port
    netloc = host
    if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        netloc = f"{host}:{port}"
    query = urlencode(
        sorted((key, val) for key, val in parse_qsl(split.query) if key not in _TRACKING_PARAMETERS)
    )
    path = split.path.rstrip("/") or "/"
    return urlunsplit((scheme, netloc, path, query, ""))


def normalize_arxiv_id(value: str) -> str:
    value = value.removeprefix("arXiv:").strip()
    return re.sub(r"v\d+$", "", value)


def canonical_key(resource: Resource) -> str:
    if isinstance(resource, PaperResource):
        if resource.doi:
            return f"paper:doi:{resource.doi.casefold()}"
        if resource.arxiv_id:
            return f"paper:arxiv:{normalize_arxiv_id(resource.arxiv_id)}"
        return f"paper:title:{normalize_title(resource.name)}:{resource.year}"
    if isinstance(resource, (ModelResource, DatasetResource)) and resource.repository_id:
        return f"{resource.kind.value}:hub:{resource.repository_id.casefold()}"
    if isinstance(resource, DatasetResource):
        url = canonicalize_url(str(resource.links.canonical))
        return f"dataset:url:{url}:{normalize_title(resource.name)}"
    if isinstance(resource, CodeResource):
        return f"code:github:{resource.repository.casefold()}"
    if isinstance(resource, SkillResource):
        repository = resource.repository.casefold()
        manifest = resource.manifest_path.casefold()
        ecosystem = resource.ecosystem.casefold()
        return f"skill:{ecosystem}:{repository}:{manifest}"
    if isinstance(resource, PlatformResource):
        provider = resource.provider.casefold()
        return f"platform:{provider}:{normalize_title(resource.name)}"
    return f"model:url:{canonicalize_url(str(resource.links.canonical))}"
