"""
Count command - a minimal wc-like utility for the CLI.

Provides counts for lines, words and bytes for one or more files or stdin.
"""

from typing import List

import typer

app = typer.Typer(help="Count lines, words and bytes (simple wc-like)")


def _count_text(text: str) -> dict:
    lines = text.count("\n")
    words = len(text.split())
    # bytes: encode as utf-8 to approximate real byte length
    b = len(text.encode("utf-8"))
    return {"lines": lines, "words": words, "bytes": b}


@app.command()
def count(
    files: List[str] = typer.Argument(None, help="Files to count. If none, reads stdin."),
    show_total: bool = typer.Option(False, "--total", "-t", help="Show total across files."),
):
    """Count lines, words and bytes for each FILE. If no files are provided, read from stdin."""

    total = {"lines": 0, "words": 0, "bytes": 0}

    if not files:
        typer.echo("Reading from stdin (end with Ctrl-D)...")
        text = typer.get_text_stream("stdin").read()
        c = _count_text(text)
        typer.echo(f"{c['lines']:7} {c['words']:7} {c['bytes']:7}")
        return

    for path in files:
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                text = f.read()
        except FileNotFoundError:
            typer.secho(f"✖ File not found: {path}", err=True, fg=typer.colors.RED)
            continue
        c = _count_text(text)
        total["lines"] += c["lines"]
        total["words"] += c["words"]
        total["bytes"] += c["bytes"]
        typer.echo(f"{c['lines']:7} {c['words']:7} {c['bytes']:7} {path}")

    if show_total and len(files) > 1:
        typer.echo(f"{total['lines']:7} {total['words']:7} {total['bytes']:7} total")
