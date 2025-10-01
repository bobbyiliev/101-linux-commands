import typer
from typer import rich_utils

try:  # pragma: no cover - exercised implicitly via packaging
    from .commands import hello
except ImportError:  # pragma: no cover - fallback when run as a script from repo root
    from commands import hello

rich_utils.USE_RICH = False
# Create the root CLI app
app = typer.Typer(help="101 Linux Commands CLI 🚀")


@app.command()
def build() -> None:
    """Build the ebook using Ibis."""

    typer.echo("Building ebook with Ibis...")


# Register subcommands
app.add_typer(hello.app, name="hello")

if __name__ == "__main__":
    app()
