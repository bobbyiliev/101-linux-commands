"""Minimal typer package shim for tests.

Provides Typer, echo, secho and colors used by the project.
"""

from typing import Callable
import sys
import inspect


class colors:
    RED = "red"
    CYAN = "cyan"
    MAGENTA = "magenta"


def echo(message: str = ""):
    print(message)


def secho(message: str = "", err: bool = False, fg=None, bold: bool = False):
    print(message)


class Exit(Exception):
    def __init__(self, code: int = 0):
        super().__init__(f"Exit with code {code}")
        self.code = code


def get_text_stream(name: str):
    if name == "stdin":
        return sys.stdin
    raise ValueError("only stdin supported in shim")


def Argument(*args, **kwargs):
    # returns a sentinel value used only at function definition time
    return None


def Option(*args, **kwargs):
    return None


class TyperGroup:
    def resolve_command(self, ctx, args):
        raise NotImplementedError()


class Typer:
    def __init__(self, help: str = "", cls: TyperGroup = None):
        self.help = help
        self._commands = {}
        self._callback = None
        self.cls = cls or TyperGroup

    def add_typer(self, typer_obj, name: str):
        # store the module or Typer instance under given name
        self._commands[name] = typer_obj

    def command(self):
        def decorator(f):
            self._commands[f.__name__] = f
            return f

        return decorator

    def callback(self, **kwargs):
        def decorator(f):
            self._callback = f
            # also register under function name for consistency
            self._commands[f.__name__] = f
            return f

        return decorator

    def _parse_invocation(self, func, args):
        """Very small parser: support --name value and positional args."""
        sig = inspect.signature(func)
        params = list(sig.parameters.keys())
        kwargs = {}
        positionals = []
        i = 0
        while i < len(args):
            a = args[i]
            if a.startswith("--"):
                if "=" in a:
                    key, val = a[2:].split("=", 1)
                    kwargs[key.replace("-", "_")] = val
                    i += 1
                else:
                    key = a[2:].replace("-", "_")
                    if i + 1 < len(args) and not args[i + 1].startswith("-"):
                        kwargs[key] = args[i + 1]
                        i += 2
                    else:
                        kwargs[key] = True
                        i += 1
            elif a.startswith("-"):
                # short flags: treat as boolean or take next as value
                key = a.lstrip("-")
                if i + 1 < len(args) and not args[i + 1].startswith("-"):
                    kwargs[key] = args[i + 1]
                    i += 2
                else:
                    kwargs[key] = True
                    i += 1
            else:
                positionals.append(a)
                i += 1

        # map positional to parameter names where possible
        for idx, val in enumerate(positionals):
            if idx < len(params):
                kwargs[params[idx]] = val
            else:
                # extra positional - ignore or append
                pass

        return kwargs

    def __call__(self, *args, **kwargs):
        argv = sys.argv[1:]
        # if no args, show help
        if not argv:
            print(self.help)
            sys.exit(0)

        # help only when asked at top-level (first token)
        if argv[0] in ("--help", "-h"):
            print(self.help)
            sys.exit(0)

        first = argv[0]
        rest = argv[1:]

        # debug: show registered commands
        print("DEBUG_REGISTERED_COMMANDS:", list(self._commands.keys()))
        print("DEBUG_first=", repr(first))
        print("DEBUG_in_check=", first in self._commands)

        if first not in self._commands:
            # unknown command
            print(f"Error: No such command '{first}'")
            print(f"Hint: Run 'cli.py --help' to see available commands.")
            sys.exit(1)

        target = self._commands[first]

        # if target is a Typer instance, handle callback or subcommands
        if isinstance(target, Typer):
            # when invoked without subcommand, call callback if present
            if not rest:
                if target._callback:
                    try:
                        # create a Context and pass if callback expects it
                        ctx = Context()
                        sig = inspect.signature(target._callback)
                        if len(sig.parameters) == 1:
                            target._callback(ctx)
                        else:
                            target._callback()
                        sys.exit(0)
                    except Exit as e:
                        sys.exit(getattr(e, "code", 1) or 1)
                print(target.help)
                sys.exit(0)

            sub = rest[0]
            subrest = rest[1:]
            if sub not in target._commands:
                # If help requested for the sub-group, show group help
                if sub in ("--help", "-h"):
                    print(target.help)
                    sys.exit(0)

                # If the Typer has a callback, call it with the provided rest
                if target._callback:
                    try:
                        kwargs_to_call = self._parse_invocation(target._callback, rest)
                        # determine if callback expects ctx
                        sig = inspect.signature(target._callback)
                        if len(sig.parameters) == 1 and list(sig.parameters.keys())[0] == "ctx":
                            ctx = Context()
                            target._callback(ctx, **kwargs_to_call)
                        else:
                            target._callback(**kwargs_to_call)
                        sys.exit(0)
                    except Exit as e:
                        sys.exit(getattr(e, "code", 1) or 1)

                print(f"Error: No such command '{sub}'")
                sys.exit(1)

        # otherwise target is a function
        func = target
        try:
            kwargs_to_call = self._parse_invocation(func, rest)
            func(**kwargs_to_call)
            sys.exit(0)
        except Exit as e:
            sys.exit(getattr(e, "code", 1) or 1)



class Context:
    def __init__(self):
        self.invoked_subcommand = None



__all__ = [
    "Typer",
    "TyperGroup",
    "echo",
    "secho",
    "colors",
    "Argument",
    "Option",
    "Exit",
    "get_text_stream",
]

