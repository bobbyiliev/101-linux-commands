import typer

from state import set_verbose, verbose_active

app = typer.Typer(help="Hello command group")


@app.command()
def greet(
    ctx: typer.Context,
    name: str = typer.Option("World", "--name", "-n", help="Name to greet."),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        is_flag=True,
        help="Enable verbose output for this command.",
    ),
) -> None:
    """Say hello to someone."""

    if verbose:
        set_verbose(ctx, True)

    if verbose_active(ctx):
        typer.echo(f"[verbose] Preparing greeting for {name}", err=True)

    typer.echo(f"Hello, {name}!")
