"""
Which command - locate executables in PATH.

Simple implementation that searches PATH and prints matching executable paths.
"""

from typing import List

import os
import shutil
import typer

app = typer.Typer(help="Locate a program file in the user's PATH")


@app.command()
def which(name: str = typer.Argument(..., help="Program name to locate"), all: bool = typer.Option(False, "--all", "-a", help="Show all matches in PATH")) -> None:
    """Locate NAME in the user's PATH, similar to the UNIX `which` command."""

    # prefer shutil.which for the first match
    if all:
        matches: List[str] = []
        for directory in os.get_exec_path():
            candidate = os.path.join(directory, name)
            if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
                matches.append(candidate)
        if not matches:
            raise typer.Exit(code=1)
        for m in matches:
            typer.echo(m)
        return

    path = shutil.which(name)
    if not path:
        typer.secho(f"{name} not found", err=True, fg=typer.colors.RED)
        raise typer.Exit(code=1)
    typer.echo(path)
