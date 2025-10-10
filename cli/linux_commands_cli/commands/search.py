import typer
from typing import Dict, List


app = typer.Typer(
    help=("Search available commands by keyword " "(name or description).")
)


def _get_available_commands() -> List[Dict[str, str]]:
    """
    Mocked list of available commands.
    Replace with real registry/source when available.
    """
    return [
        {"name": "ls", "description": "List directory contents"},
        {"name": "grep", "description": "Search for PATTERN in files"},
        {
            "name": "find",
            "description": "Search for files in a directory hierarchy",
        },
        {
            "name": "awk",
            "description": "Pattern scanning and processing language",
        },
        {
            "name": "cat",
            "description": ("Concatenate files and print on the standard " "output"),
        },
        {"name": "head", "description": "Output the first part of files"},
        {"name": "tail", "description": "Output the last part of files"},
        {
            "name": "sed",
            "description": ("Stream editor for filtering and transforming " "text"),
        },
    ]


def _search_commands(
    keyword: str,
    commands: List[Dict[str, str]],
) -> List[Dict[str, str]]:
    k = (keyword or "").strip().lower()
    if not k:
        return []
    return [
        cmd
        for cmd in commands
        if (k in cmd.get("name", "").lower())
        or (k in cmd.get("description", "").lower())
    ]


@app.callback(invoke_without_command=True)
def search(
    keyword: str = typer.Argument(
        ...,
        help="Keyword to search for, e.g. 'grep'",
    ),
) -> None:
    """
    Search available commands by keyword (matches command name or description).
    Example: python cli.py search grep
    """
    results = _search_commands(keyword, _get_available_commands())
    if not results:
        typer.echo("No commands found.")
        raise typer.Exit(code=1)

    for cmd in results:
        name = cmd.get("name", "").strip()
        desc = cmd.get("description", "").strip()
        typer.echo(f"{name}: {desc}")
