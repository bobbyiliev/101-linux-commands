# Contributing

## Pull Requests

### Creating a Pull Request

This book has been designed so that people can easily expand it.
To request us to review changes that you create, you will need to create a pull request.
Creating a pull request is described in
 [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github).

### File Location/Types

### [`ebook`](./ebook)

This directory holds all of the translations of the eBook.

### [`ebook/{LANG}`](./ebook/{LANG})

In the `ebook` directory we have the translations of the eBook in different languages.

If you are adding a new translation, make sure to make a copy of the `./ebook/en` directory and use the language code as the new directory name.

### [`ebook/{LANG}/content`](./ebook/{LANG}/content)

All the Markdown files for the '101 Linux commands' eBook are located within the [`content`](./content) directory for the specific language.

For example if you are adding a Bulgarian translation copy the `./ebook/en` folder to `./ebook/bg`, translate the `.md` files in the `content` directory and submit a PR.

### eBook Generation

The project uses [Ibis Next](https://github.com/Hi-Folks/ibis-next) developed by [Roberto Butti](https://github.com/roberto-butti), forked from the original [Ibis](https://github.com/themsaid/ibis/) by [Mohamed Said](https://github.com/themsaid).

Ibis Next supports generating PDF, EPUB, and HTML formats from Markdown content.

## Setup and Usage

1. Install dependencies:

```bash
composer install
```

1. Generate PDF (light theme):

```bash
composer run pdf
```

1. Generate PDF (dark theme):

```bash
composer run pdf-dark
```

1. Generate EPUB:

```bash
composer run epub
```

1. Generate HTML:

```bash
composer run html
```

For more information about Ibis Next, visit: [Getting started with Ibis Next](https://github.com/Hi-Folks/ibis-next)

## Contribution Examples

### Typical Git workflow

1. Fork the repository on GitHub and clone your fork locally.

```bash
git clone https://github.com/<your-user>/101-linux-commands.git
cd 101-linux-commands
```

1. Create a dedicated branch for your changes.

```bash
git checkout -b feature/add-cli-example
```

1. While you work, check your status and stage files deliberately.

```bash
git status
git add CONTRIBUTING.md
```

1. Commit with a descriptive message and push your branch.

```bash
git commit -m "docs: add CLI contribution examples"
git push origin feature/add-cli-example
```

### Running the CLI locally

1. Move into the CLI workspace.

```bash
cd cli
```

1. (Recommended) Create and activate a virtual environment. Use the command that matches your shell:

```bash
cd cli
uv sync --frozen --group dev

# for Windows PowerShell
.\.venv\Scripts\Activate.ps1
# OR for macOS/Linux
source .venv/bin/activate
```

1. Confirm the CLI works.

```bash
linux-cli --help
# or run directly without installation
python -m linux_commands_cli.cli hello greet --name "Linux Contributor"
# greet someone specific using the installed entry point
linux-cli hello greet --name "Linux Contributor"
```

### Adding a new command

1. Create a new command module inside `cli/commands/`. Example (`cli/commands/ping.py`):

```python
import typer


app = typer.Typer(help="Ping command group")


@app.command()
def once():
    """Print a ping message."""
    typer.echo("pong")
```

1. Register the command with the main Typer app in `cli/cli.py`:

```python
from linux_commands_cli.commands import hello, ping

app = typer.Typer(help="101 Linux Commands CLI 🚀")
app.add_typer(hello.app, name="hello")
app.add_typer(ping.app, name="ping")
```

1. Add or update tests in `tests/cli/test_cli.py` to cover your new command. Mirror the existing `hello` command tests and update expectations.

1. Run the CLI manually to verify your command behaves as expected.

```bash
python -m linux_commands_cli.cli ping once
```

### Running tests

1. Ensure you're in the `cli` directory with your virtual environment activated.

1. Install the testing dependency if you haven't already.

```bash
pip install pytest
```

1. Execute the test suite:

```bash
pytest
```

1. (Optional but encouraged) Run the additional quality checks that the workflow executes:

```bash
black cli/
isort cli/
flake8 cli/
mypy cli/
```

## Issue Creation

In the event that you have an issue using the guide or have a suggestion for a change but don't want to contribute changes,
 we are more than happy to help.
Make sure that when you create your issue, it follows the format for the type of issue you select
 (it has individual templates for each issue type).

Issue template types include the following:

- Bug Reporting
- Feature Requests
- Help Requests
