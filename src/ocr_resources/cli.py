from __future__ import annotations

from datetime import date
from pathlib import Path

import typer

from ocr_resources.audit import audit_links
from ocr_resources.discovery.runner import discover_resources
from ocr_resources.migration.legacy_markdown import migrate_legacy
from ocr_resources.rendering import render_repository
from ocr_resources.repository import validate_repository
from ocr_resources.schema import generate_schemas

app = typer.Typer(no_args_is_help=True, help="Maintain structured OCR resources.")
migrate_app = typer.Typer(no_args_is_help=True, help="Import legacy data.")
app.add_typer(migrate_app, name="migrate")


def repository_root(value: Path | None = None) -> Path:
    return (value or Path.cwd()).resolve()


@migrate_app.command("legacy")
def migrate_legacy_command(
    root: Path | None = typer.Option(None, help="Repository root."),
    force: bool = typer.Option(False, help="Replace existing structured data."),
) -> None:
    """Import the repository's original Markdown lists."""
    report = migrate_legacy(repository_root(root), force=force)
    typer.echo(f"Migrated {report.paper_output} papers and {report.dataset_output} datasets.")


@app.command("render")
def render_command(
    root: Path | None = typer.Option(None, help="Repository root."),
    check: bool = typer.Option(False, help="Fail instead of writing when output is stale."),
) -> None:
    """Render Markdown views from structured data."""
    changed = render_repository(repository_root(root), check=check)
    if check and changed:
        for path in changed:
            typer.echo(f"STALE: {path}", err=True)
        raise typer.Exit(code=1)
    if changed:
        typer.echo(f"Rendered {len(changed)} file(s).")
    else:
        typer.echo("Generated files are current.")


@app.command("schemas")
def schemas_command(
    root: Path | None = typer.Option(None, help="Repository root."),
    check: bool = typer.Option(False, help="Fail if committed schemas are stale."),
) -> None:
    """Generate JSON Schema files from Pydantic models."""
    changed = generate_schemas(repository_root(root), check=check)
    if check and changed:
        for path in changed:
            typer.echo(f"STALE: {path}", err=True)
        raise typer.Exit(code=1)
    typer.echo(f"Updated {len(changed)} schema file(s)." if changed else "Schemas are current.")


@app.command("discover")
def discover_command(
    root: Path | None = typer.Option(None, help="Repository root."),
    lookback_days: int = typer.Option(7, min=1, max=30),
    source: list[str] | None = typer.Option(None, help="Source(s): arxiv, huggingface, github."),
    dry_run: bool = typer.Option(False, help="Report candidates without changing resource data."),
    until: str | None = typer.Option(None, help="Inclusive end date in YYYY-MM-DD format."),
) -> None:
    """Discover, score, and stage new candidate resources."""
    allowed = {"arxiv", "huggingface", "github"}
    selected = set(source or allowed)
    unknown = selected - allowed
    if unknown:
        raise typer.BadParameter(f"unknown source(s): {', '.join(sorted(unknown))}")
    try:
        until_date = date.fromisoformat(until) if until else None
    except ValueError as exc:
        raise typer.BadParameter("until must use YYYY-MM-DD format") from exc
    report = discover_resources(
        repository_root(root),
        lookback_days=lookback_days,
        selected_sources=selected,
        dry_run=dry_run,
        until=until_date,
    )
    typer.echo(
        f"Found {sum(report['sources'].values())} candidate(s); "
        f"matched {report['matched']}; staged {report['added']}."
    )
    if report["source_errors"]:
        for error in report["source_errors"]:
            typer.echo(f"SOURCE ERROR ({error['source']}): {error['error']}", err=True)
        # Only a total blackout is fatal; otherwise keep the healthy sources' results.
        if not report["sources_ok"]:
            raise typer.Exit(code=2)
        typer.echo(
            f"DEGRADED: continuing without {', '.join(report['sources_failed'])}.",
            err=True,
        )


@app.command("audit-links")
def audit_links_command(
    root: Path | None = typer.Option(None, help="Repository root."),
    timeout: float = typer.Option(15.0, min=1.0, max=60.0),
) -> None:
    """Audit canonical resource links without changing resource status."""
    report = audit_links(repository_root(root), timeout=timeout)
    typer.echo(f"Checked {report['checked']} links; {report['failed']} failed.")
    if report["failed"]:
        raise typer.Exit(code=1)


@app.command("validate")
def validate_command(
    root: Path | None = typer.Option(None, help="Repository root."),
) -> None:
    """Validate every resource and cross-resource invariant."""
    errors = validate_repository(repository_root(root))
    if errors:
        for error in errors:
            typer.echo(f"ERROR: {error}", err=True)
        raise typer.Exit(code=1)
    typer.echo("Resource data is valid.")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
