import typer


app = typer.Typer(help="List the commands available on Linux.")


@app.callback(invoke_without_command=True)
def list():
    commands = [
        "ls - List directory contents.",
        "cd - Change directory.",
        "pwd - Print working directory.",
        "cat - Concatenate and display files.",
    ]
    for command in commands:
        typer.echo(command)
