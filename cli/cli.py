import typer

from commands import hello, listing
from state import set_verbose

# Create the root CLI app
app = typer.Typer(help="101 Linux Commands CLI 🚀")


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

if __name__ == "__main__":
    app()
