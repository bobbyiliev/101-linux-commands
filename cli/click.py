"""
Minimal shim for click used by the test environment.

This is not a full implementation—only the small parts the project uses in tests.
"""

class _ExceptionsModule:
    class UsageError(Exception):
        def __init__(self, message, ctx=None):
            super().__init__(message)
            self._message = message
            self.ctx = ctx

        def format_message(self):
            return str(self._message)


exceptions = _ExceptionsModule()


class Context:
    def __init__(self):
        self.info_name = None

    def find_root(self):
        return self
