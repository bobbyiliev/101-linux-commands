"""
Hello command for the 101 Linux Commands CLI.
"""

import typer


app = typer.Typer(help="Hello command group")


@app.command()
def greet(name: str = "World"):
    """Say hello to someone."""
    typer.echo(f"Hello, {name}!")
