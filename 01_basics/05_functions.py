"""05 - Functions: args, kwargs, scope, lambdas, first-class functions."""

# --- Defaults, keyword args, docstrings, annotations ---
def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting."""
    return f"{greeting}, {name}!"

print(greet("Ada"), greet(greeting="Hi", name="Bo"))

# --- *args and **kwargs ---
def summarize(*args, **kwargs):
    return sum(args), kwargs

print(summarize(1, 2, 3, mode="fast"))

# --- Positional-only (/) and keyword-only (*) parameters ---
def f(a, b, /, c, *, d):
    return a, b, c, d
print(f(1, 2, 3, d=4))

# --- Unpacking arguments ---
vals = [1, 2, 3]
opts = {"mode": "x"}
print(summarize(*vals, **opts))

# --- Mutable default argument pitfall ---
def bad(item, bucket=[]):
    bucket.append(item); return bucket
def good(item, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(item); return bucket
print(bad(1), bad(2))     # [1] [1, 2]  <- shared state!
print(good(1), good(2))   # [1] [2]

# --- Scope: LEGB (Local, Enclosing, Global, Built-in) ---
counter = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()
def bump():
    global counter
    counter += 1
print(outer()); bump(); print(counter)

# --- First-class functions & lambdas ---
def apply(fn, value):
    return fn(value)
print(apply(lambda n: n ** 2, 5))

# --- Recursion ---
def fact(n: int) -> int:
    return 1 if n <= 1 else n * fact(n - 1)
print(fact(5))

# --- Multiple return values (really a tuple) ---
def min_max(items):
    return min(items), max(items)
lo, hi = min_max([3, 1, 4])
print(lo, hi)
