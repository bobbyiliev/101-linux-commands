"""
Build the ebook using Ibis CLI.
"""

from datetime import datetime

import typer

from states.global_state import debug, verbose_flag

app = typer.Typer(help="Ebook Builder CLI using Ibis")


@app.command()
def build(
    dry_run: bool = typer.Option(
        False, help="Simulate the build process without creating files."
    ),
    output: str = typer.Option(
        "output/ebook", help="Directory to save the built ebook."
    ),
):
    """Build the ebook using Ibis."""
    typer.echo("Building ebook with Ibis...")

    start_time = datetime.now()
    typer.secho(
        f"Starting ebook build at {start_time.strftime('%H:%M:%S')}",
        fg=typer.colors.BLUE,
    )

    if dry_run:
        typer.secho(
            "Dry run enabled — no files will be generated.", fg=typer.colors.YELLOW
        )
    else:
        typer.echo(f"Building ebook in '{output}'...")

    if verbose_flag["enabled"]:
        debug("Starting the build process using Ibis")

    # Placeholder for future build steps
    steps = ["Compiling markdown", "Generating PDF", "Generating EPUB"]
    for step in steps:
        if dry_run:
            typer.echo(f"[Dry-run] {step} skipped.")
        else:
            typer.echo(f"{step} completed.")

    end_time = datetime.now()
    typer.secho(
        f"Build process finished at {end_time.strftime('%H:%M:%S')}",
        fg=typer.colors.GREEN,
    )
    typer.secho(f"Total time: {end_time - start_time}", fg=typer.colors.CYAN)

    # Debug message for test compatibility
    if verbose_flag["enabled"]:
        debug("Build process completed")
