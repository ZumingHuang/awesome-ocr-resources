from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from ocr_resources.identity import canonicalize_url, normalize_arxiv_id, normalize_title, slugify
from ocr_resources.models import DatePrecision, PartialDate
from ocr_resources.taxonomy import load_taxonomy

ROOT = Path(__file__).parents[1]


def test_partial_date_accepts_each_supported_precision() -> None:
    assert PartialDate(value="2026", precision=DatePrecision.YEAR).value == "2026"
    assert PartialDate(value="2026-07", precision=DatePrecision.MONTH).value == "2026-07"
    assert PartialDate(value="2026-07-26", precision=DatePrecision.DAY).value == "2026-07-26"
    assert PartialDate(value="unknown", precision=DatePrecision.UNKNOWN).value == "unknown"


@pytest.mark.parametrize("value", ["2026-13", "2026-02-31", "unknown-01"])
def test_partial_date_rejects_invalid_values(value: str) -> None:
    precision = (
        DatePrecision.UNKNOWN
        if value.startswith("unknown")
        else (DatePrecision.MONTH if value.count("-") == 1 else DatePrecision.DAY)
    )
    with pytest.raises(ValueError):
        PartialDate(value=value, precision=precision)


def test_identity_normalization() -> None:
    assert slugify("OCR: 文档 AI / Test") == "ocr-ai-test"
    assert normalize_title("  Text-Spotting: A Test! ") == "text spotting a test"
    assert normalize_arxiv_id("arXiv:2607.12345v3") == "2607.12345"
    assert (
        canonicalize_url("HTTPS://Example.COM:443/path/?utm_source=x&b=2&a=1#fragment")
        == "https://example.com/path?a=1&b=2"
    )


def test_taxonomy_maps_legacy_variants() -> None:
    taxonomy = load_taxonomy(ROOT)
    assert taxonomy.map_legacy_task("Document-VQA") == "document-vqa"
    assert taxonomy.map_legacy_task("document-VQA") == "document-vqa"
    assert taxonomy.map_legacy_task("end-to-end-ocr") == "text-spotting"
    assert date.today().year >= 2026
