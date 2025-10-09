"""
CLI entry point for the 101 Linux Commands application.
"""

from typing import List

import click
import typer
from typer.main import TyperGroup

from commands import hello, list, search, show, version


class CustomTyper(TyperGroup):
    def resolve_command(self, ctx: click.Context, args: List[str]):
        try:
            return super().resolve_command(ctx, args)
        except click.exceptions.UsageError as e:
            original = e.format_message()

            if "No such command" in original:
                script_name = ctx.find_root().info_name or "cli"
                hint = f"💡 Hint: Run '{script_name} --help' to see available commands."

                new_message = f"{original}\n{hint}"
                raise click.exceptions.UsageError(new_message, ctx=ctx) from e

            raise
 
@app.callback()
def main(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        is_flag=True,
        help="Enable verbose debug output for all commands.",
    ),
) -> None:
    """Configure application-wide options before subcommands run."""

    set_verbose(ctx, verbose)
    if verbose:
        typer.echo("[verbose] Verbose mode enabled", err=True)

# Register subcommands
app.add_typer(hello.app, name="hello")
app.add_typer(listing.app, name="list")
app.add_typer(version.app, name="version")
app.command()(show.show)

def main() -> None:
    """CLI entry point."""
    app()

if __name__ == "__main__":
    main()