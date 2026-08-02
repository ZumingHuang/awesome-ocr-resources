# Contributing

Thank you for helping maintain this OCR and Document AI resource collection.

## Before submitting

1. Read [CURATION.md](CURATION.md) and confirm the resource is directly relevant.
2. Prefer an official paper, model card, dataset card, upstream repository, or product documentation URL.
3. Search `data/` for the canonical URL, DOI, arXiv ID, Hub repository ID, or GitHub repository.
4. Never guess a license. Use `NOASSERTION` when the official source does not state one.

## Add or update a resource

1. Add one YAML file below the matching `data/<kind>/` directory.
2. Run `uv run ocr-resources validate`.
3. Run `uv run ocr-resources render` and commit the generated Markdown.
4. Run the test and lint commands listed in the pull request template.

Do not edit generated list pages directly. The original historical paths under `papers/papers_by_year/` are retained for compatibility but are generated from YAML.

## Security

Do not install or execute code from a resource while reviewing it. A Skill submission must disclose command execution, network access, and credential requirements. See [SECURITY.md](SECURITY.md).
