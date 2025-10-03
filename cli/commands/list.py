import typer

app = typer.Typer(help="List the commands available on Linux.")

@app.callback(invoke_without_command=True)
def list(ctx: typer.Context, verbose: bool = typer.Option(False, "--verbose", help="Show examples for each command")):
    """
    Display a list of commonly used Linux commands.
    """
    commands = {
        "ls": "List directory contents",
        "cd": "Change directory",
        "pwd": "Print working directory",
        "cat": "Concatenate and display files",
        "mkdir": "Make directories",
        "rm": "Remove files or directories",
        "cp": "Copy files and directories",
        "mv": "Move or rename files and directories",
        "touch": "Create empty files",
        "grep": "Search text using patterns",
        "chmod": "Change file permissions",
        "man": "Display manual pages",
    }

    examples = {
        "ls": "ls -l",
        "cd": "cd /home/user",
        "pwd": "pwd",
        "cat": "cat file.txt",
        "mkdir": "mkdir new_folder",
        "rm": "rm file.txt",
        "cp": "cp source.txt dest.txt",
        "mv": "mv old.txt new.txt",
        "touch": "touch newfile.txt",
        "grep": "grep 'hello' file.txt",
        "chmod": "chmod +x script.sh",
        "man": "man ls",
    }

    typer.echo("\n📜 Common Linux Commands:\n")
    for cmd, desc in commands.items():
        typer.echo(f"🔹 {cmd:<6} - {desc}")
        if verbose:
            typer.echo(f"     Example: {examples[cmd]}")
    typer.echo()

if __name__ == "__main__":
    app()
