"""02 - Closures and decorators."""
import functools
import time

# --- Closure: inner function remembers enclosing variables ---
def make_multiplier(n):
    def mul(x):
        return x * n
    return mul
double = make_multiplier(2)
print(double(8))

# --- Basic decorator (always use functools.wraps) ---
def timer(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} took {time.perf_counter() - start:.6f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    """Sum numbers."""
    return sum(range(n))
slow_sum(100_000)
print(slow_sum.__name__, slow_sum.__doc__)

# --- Decorator with arguments ---
def retry(times=3):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kw):
            for attempt in range(1, times + 1):
                try:
                    return fn(*a, **kw)
                except Exception as e:
                    print(f"attempt {attempt} failed: {e}")
            raise RuntimeError("all retries failed")
        return wrapper
    return decorator

calls = {"n": 0}
@retry(times=3)
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ValueError("boom")
    return "ok"
print(flaky())

# --- Class-based decorator & stacking ---
class CountCalls:
    def __init__(self, fn):
        functools.update_wrapper(self, fn)
        self.fn, self.count = fn, 0
    def __call__(self, *a, **kw):
        self.count += 1
        return self.fn(*a, **kw)

@CountCalls
def hello(): return "hi"
hello(); hello()
print(hello.count)

# --- Built-in caching decorators ---
@functools.cache
def fib(n): return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(80))
