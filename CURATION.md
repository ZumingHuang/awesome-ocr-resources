# Curation Policy

## Scope

The collection covers text detection and recognition, text spotting, handwriting, document image restoration, layout analysis, document parsing, key information extraction, table and formula recognition, Document VQA, and closely related OCR-centered Document AI.

A general-purpose multimodal model is included only when an official source demonstrates a material OCR or document-understanding capability, publishes a relevant model/data/code artifact, or reports document benchmark results.

## Categories

- **Papers:** research publications and substantive preprints.
- **Models:** official weights, model cards, APIs, or product releases.
- **Datasets:** training, pretraining, validation, and benchmark datasets.
- **Codes:** notable upstream toolkits and official implementations.
- **Skills:** installable, reusable agent workflows with a manifest and documented interface.
- **Platforms:** official OCR/Document AI APIs, SaaS products, SDKs, and on-premise services.

An MCP server is a code resource unless it also ships an installable Skill manifest.

## Evidence and quality

Every resource needs a canonical first-party URL. Discovery scores are triage aids, not acceptance decisions. Maintainers review relevance, identity, metadata, licensing, and links before changing `curation.status` from `candidate` or `needs-review` to `verified`.

Dates have separate meanings:

- `released_at`: when the resource was released; precision may be year, month, or day.
- `added_at`: when it entered this collection.
- `last_verified_at`: when its metadata and links were last checked.

## Lifecycle

A transient link failure does not delete a resource. Mark unresolved entries `stale`; use `archived` only after confirming discontinuation or an upstream archive. Landmark code may remain listed even when inactive.

## Automation boundary

Automation discovers, normalizes, deduplicates, scores, and validates. It never auto-merges a candidate, executes third-party code, or invents missing licenses and identifiers.
