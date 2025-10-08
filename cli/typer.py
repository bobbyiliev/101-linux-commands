"""
Very small Typer shim for the exercise tests.

Implements Typer, TyperGroup, echo, secho and basic colors used by the project.
"""

from typing import Callable

class colors:
    RED = "red"
    CYAN = "cyan"
    MAGENTA = "magenta"


def echo(message: str = ""):
    print(message)


def secho(message: str = "", err: bool = False, fg=None, bold: bool = False):
    print(message)


class TyperGroup:
    def resolve_command(self, ctx, args):
        raise NotImplementedError()


class Typer:
    def __init__(self, help: str = "", cls: TyperGroup = None):
        self.help = help
        self._commands = {}
        self.cls = cls or TyperGroup

    def add_typer(self, typer_obj, name: str):
        # typer_obj is a module with 'app' Typer or a Typer instance
        try:
            self._commands[name] = typer_obj
        except Exception:
            self._commands[name] = typer_obj

    def command(self):
        def decorator(f):
            self._commands[f.__name__] = f
            return f

        return decorator

    def __call__(self, *args, **kwargs):
        # When invoked, just print help for test simplicity
        print(self.help)
