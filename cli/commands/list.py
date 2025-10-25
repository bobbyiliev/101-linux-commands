import typer

from states.global_state import debug, verbose_flag

app = typer.Typer(help="List common Linux commands with descriptions and examples.")

# Define commands with description and example
commands = [
    {"name": "ls", "desc": "List directory contents.", "example": "ls -lah"},
    {"name": "cd", "desc": "Change directory.", "example": "cd /home/user/Documents"},
    {"name": "pwd", "desc": "Print working directory.", "example": "pwd"},
    {
        "name": "cat",
        "desc": "Concatenate and display files.",
        "example": "cat file.txt",
    },
    {"name": "mkdir", "desc": "Create a new directory.", "example": "mkdir new_folder"},
]


@app.callback(invoke_without_command=True)
def list_commands():
    """List available Linux commands with descriptions and examples."""
    if verbose_flag["enabled"]:
        debug(f"Listing {len(commands)} commands")

    typer.echo("\nAvailable Linux Commands:\n")
    for cmd in commands:
        # Only one-line summary by default
        typer.echo(f"{cmd['name']} - {cmd['desc']}")

        # Extra details only if verbose
        if verbose_flag["enabled"]:
            typer.echo(f"  Description: {cmd['desc']}")
            typer.echo(f"  Example: {cmd['example']}\n")
