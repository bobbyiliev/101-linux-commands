"""
CLI entry point for the 101 Linux Commands application.
"""

import click
import typer
from typer.main import TyperGroup
from typing import List

from linux_commands_cli.commands import hello, list, search, show, version


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


app = typer.Typer(help="101 Linux Commands CLI 🚀", cls=CustomTyper)
app.add_typer(hello.app, name="hello")
app.add_typer(list.app, name="list")
app.add_typer(version.app, name="version")
app.command()(show.show)
app.add_typer(search.app, name="search")


def main() -> None:
    """CLI entry point."""
    app()


if __name__ == "__main__":
    main()
