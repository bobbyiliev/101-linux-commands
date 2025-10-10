"""Version command for 101-linux-commands CLI."""

import sys
import typer
from pathlib import Path

from linux_commands_cli.__version__ import __version__


sys.path.insert(0, str(Path(__file__).parent.parent))

app = typer.Typer(help="version command")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Show the current version of 101-linux CLI"""
    if ctx.invoked_subcommand is None:
        typer.echo(f"101-linux v{__version__}")


@app.command()
def show():
    """Show the current version of 101-linux CLI"""
    typer.echo(f"101-linux v{__version__}")
