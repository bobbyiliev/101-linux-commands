#!/usr/bin/env python3
"""Basic tests for the CLI module."""

import os
import subprocess
import sys
from pathlib import Path
CLI_DIR = Path(__file__).parent
CLI_ENV = {**os.environ, "PYTHONIOENCODING": "utf-8"}


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "cli.py", *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=CLI_DIR,
        env=CLI_ENV,
    )


def test_cli_help():
    """Test that the CLI shows help."""
    result = run_cli("--help")
    assert result.returncode == 0
    assert "101 Linux Commands CLI" in result.stdout


def test_hello_command():
    """Test the hello command."""
    result = run_cli("hello", "greet")
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout


def test_hello_command_with_name():
    """Test the hello command with a custom name."""
    result = run_cli("hello", "greet", "--name", "Linux")
    assert result.returncode == 0
    assert "Hello, Linux!" in result.stdout


def test_hello_help():
    """Test the hello command help."""
    result = run_cli("hello", "--help")
    assert result.returncode == 0
    assert "Hello command group" in result.stdout


def test_build_command_stub():
    """Build command should print placeholder message."""
    result = run_cli("build")
    assert result.returncode == 0
    assert "Building ebook with Ibis..." in result.stdout


if __name__ == "__main__":
    test_cli_help()
    test_hello_command()
    test_hello_command_with_name()
    test_hello_help()
    test_build_command_stub()
    print("✅ All tests passed!")
