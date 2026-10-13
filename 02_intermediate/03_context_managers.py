"""03 - Context managers (`with`)."""
from contextlib import contextmanager, suppress, ExitStack, redirect_stdout
import io
import time

# --- Class-based ---
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        return False            # False = don't swallow exceptions

with Timer() as t:
    sum(range(100_000))
print(f"{t.elapsed:.5f}s")

# --- Generator-based ---
@contextmanager
def tag(name):
    print(f"<{name}>", end="")
    try:
        yield
    finally:
        print(f"</{name}>")

with tag("b"):
    print("bold", end="")

# --- contextlib helpers ---
with suppress(FileNotFoundError):
    open("/nonexistent/file")

buf = io.StringIO()
with redirect_stdout(buf):
    print("captured")
print(repr(buf.getvalue()))

with ExitStack() as stack:
    stack.callback(print, "closing A")
    stack.callback(print, "closing B")     # callbacks run in reverse order
