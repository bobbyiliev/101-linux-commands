# 101 Linux Commands CLI Tool

Interactive CLI tool companion for the 101 Linux Commands eBook.

## Usage

To get started, install the dependencies and run the CLI:

```bash
pip install -r requirements.txt
python -m cli.cli --help
```

You can also install the CLI as an editable package:

```bash
pip install -e .
linux-cli --help
```

### Examples

Here are some examples of how to use the CLI:

> Note: The `list`, `search`, and `show` commands are still under development.

*   **List all commands:**

    ```bash
    linux-cli list
    ```

*   **Search for a command:**

    ```bash
    linux-cli search grep
    ```

*   **Show details for a command:**

    ```bash
    linux-cli show ls
    ```

*   **Count lines/words/bytes (wc-like):**

    ```bash
    # Count a single file
    linux-cli count file.txt

    # Count multiple files and show total
    linux-cli count --total file1.txt file2.txt

    # Read from stdin
    cat file.txt | linux-cli count
    ```

*   **Locate an executable (which-like):**

    ```bash
    # Show first match in PATH
    linux-cli which python3

    # Show all matches in PATH
    linux-cli which --all python3
    ```

## Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black cli/
```

### Import Sorting
```bash
isort cli/
```

### Linting
```bash
flake8 cli/
```

### Type Checking
```bash
mypy cli/
```

## GitHub Actions

The CLI has its own workflow that runs:
- Code formatting checks (Black)
- Import sorting checks (isort) 
- Linting (Flake8)
- Type checking (MyPy)
- Tests (pytest)

This workflow only triggers on changes to the `cli/` directory.