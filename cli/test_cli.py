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


def test_hello_command_verbose_option():
    """Command-level verbose flag should emit debug output."""
    result = run_cli("hello", "greet", "--verbose")
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout
    assert "[verbose]" in result.stderr


def test_global_verbose_flag():
    """Global verbose flag should cascade to subcommands."""
    result = run_cli("--verbose", "hello", "greet", "--name", "Tester")
    assert result.returncode == 0
    assert "Hello, Tester!" in result.stdout
    assert "[verbose] Verbose mode enabled" in result.stderr
    assert "[verbose] Preparing greeting for Tester" in result.stderr


def test_hello_help():
    """Test the hello command help."""
    result = run_cli("hello", "--help")
    assert result.returncode == 0
    assert "Hello command group" in result.stdout


def test_list_command_basic():
    """List command should show lesson titles."""
    result = run_cli("list", "--limit", "3")
    assert result.returncode == 0
    assert "000" in result.stdout
    assert "Introduction" in result.stdout


def test_list_command_verbose_option():
    """Command-level verbose flag should emit debug output."""
    result = run_cli("list", "--limit", "2", "--verbose")
    assert result.returncode == 0
    assert "[verbose] Located" in result.stderr


def test_list_command_global_verbose():
    """Global verbose flag should cascade to list command."""
    result = run_cli("--verbose", "list", "--limit", "1")
    assert result.returncode == 0
    assert "[verbose] Verbose mode enabled" in result.stderr
    assert "[verbose] Located" in result.stderr


if __name__ == "__main__":
    test_cli_help()
    test_hello_command()
    test_hello_command_with_name()
    test_hello_command_verbose_option()
    test_global_verbose_flag()
    test_hello_help()
    test_list_command_basic()
    test_list_command_verbose_option()
    test_list_command_global_verbose()
    print("✅ All tests passed!")