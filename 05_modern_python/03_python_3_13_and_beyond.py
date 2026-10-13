"""03 - 3.13, 3.14 and what's coming.

New *syntax* is parsed before any `if` runs, so version-specific syntax is kept in
strings and run with exec() only on versions that support it. In a real project you
would simply set `requires-python` and write the syntax directly.
"""
import sys
from textwrap import dedent

print("running on", sys.version.split()[0])

# ================= 3.13 =================
# - New interactive REPL (multi-line editing, colour)
# - Experimental free-threaded build (no GIL):   python3.13t
# - Experimental JIT (build option --enable-experimental-jit)
# - copy.replace(), warnings.deprecated, TypeVar defaults (PEP 696)
if sys.version_info >= (3, 13):
    exec(dedent('''
        import copy
        from dataclasses import dataclass
        from warnings import deprecated

        @dataclass
        class P:
            x: int
            y: int
        print(copy.replace(P(1, 2), y=9))

        @deprecated("use new_api()")
        def old_api(): return 1

        class Box[T = int]:        # type parameter default (PEP 696)
            pass
        print("3.13 features OK")
    '''))
else:
    print("(3.13 demos skipped on this version)")

# Check whether the GIL is enabled (3.13+ free-threaded builds)
if hasattr(sys, "_is_gil_enabled"):
    print("GIL enabled:", sys._is_gil_enabled())

# ================= 3.14 =================
# - Template strings (t-strings, PEP 750): t"Hello {name}" builds a Template object,
#   letting libraries sanitize interpolations (SQL, HTML) safely.
# - Deferred evaluation of annotations (PEP 649/749): forward references just work.
# - `except A, B:` without parentheses (PEP 758).
# - concurrent.interpreters, compression.zstd, annotationlib, better free-threading.
if sys.version_info >= (3, 14):
    exec(dedent('''
        name = "Ada"
        tpl = t"Hello {name}"
        print(type(tpl).__name__, tpl.strings, [i.value for i in tpl.interpolations])
    '''))
else:
    print("(3.14 demos skipped on this version)")

# Always check release notes: https://docs.python.org/3/whatsnew/
# Tip: use `python -W error` in tests so deprecations become failures early.
