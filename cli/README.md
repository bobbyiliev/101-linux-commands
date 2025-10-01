# 101 Linux Commands CLI Tool

Interactive CLI tool companion for the 101 Linux Commands eBook.

## Installation

From the CLI directory:

```bash
pip install -r requirements.txt
pip install -e .
```

## Usage

```bash
# Using the installed command
linux-cli --help
l101 --help

# Or running directly
python -m cli.cli --help
```

## Commands

### Hello Command

```bash
linux-cli hello greet
linux-cli hello greet "Linux User"
```

### Build Command

```bash
linux-cli build
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
