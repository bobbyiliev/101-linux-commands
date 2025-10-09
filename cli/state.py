"""Shared CLI state helpers for global flags."""

from __future__ import annotations

import typer

_VERBOSE_KEY = "verbose"


def set_verbose(ctx: typer.Context, value: bool) -> None:
    """Persist the verbose flag on this context and all parents."""
    current = ctx
    while current is not None:
        current.ensure_object(dict)
        current.obj[_VERBOSE_KEY] = value
        current = current.parent


def verbose_active(ctx: typer.Context) -> bool:
    """Check whether verbose mode is enabled anywhere up the chain."""
    current = ctx
    while current is not None:
        if current.obj and current.obj.get(_VERBOSE_KEY):
            return True
        current = current.parent
    return False


__all__ = ["set_verbose", "verbose_active"]
