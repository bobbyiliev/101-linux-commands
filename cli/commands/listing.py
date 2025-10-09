"""Command utilities for listing available lessons."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Optional

import typer

from state import set_verbose, verbose_active

app = typer.Typer(help="List available Linux command lessons.")

_CONTENT_DIR = Path(__file__).resolve().parents[2] / "ebook" / "en" / "content"


def _get_lessons() -> Iterable[Path]:
    if not _CONTENT_DIR.exists():
        return []
    return sorted(_CONTENT_DIR.glob("*.md"))


def _format_title(path: Path) -> str:
    stem = path.stem
    prefix, _, slug = stem.partition("-")
    title = slug.replace("-", " ").strip().title() if slug else prefix.replace("-", " ")
    if prefix.isdigit():
        return f"{prefix} {title}".strip()
    return title


@app.callback(invoke_without_command=True)
def list_commands(
    ctx: typer.Context,
    limit: Optional[int] = typer.Option(
        None,
        "--limit",
        "-l",
        min=1,
        help="Limit the number of commands displayed. Shows all when omitted.",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        is_flag=True,
        help="Enable verbose output for this command.",
    ),
) -> None:
    """Display the available Linux command lessons."""

    if verbose:
        set_verbose(ctx, True)

    lessons = list(_get_lessons())
    total = len(lessons)

    if verbose_active(ctx):
        typer.echo(f"[verbose] Located {total} command lessons", err=True)

    if total == 0:
        typer.echo("No command lessons found.")
        return

    limit_value = total if limit is None else min(limit, total)

    if verbose_active(ctx) and limit is not None:
        typer.echo(f"[verbose] Limiting output to {limit_value} entries", err=True)

    for path in lessons[:limit_value]:
        typer.echo(_format_title(path))


__all__ = ["app"]
