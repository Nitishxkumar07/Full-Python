"""01 - Modern features: 3.8 -> 3.10."""
import sys
from dataclasses import dataclass

# ---- 3.8 ----
# Walrus operator
if (n := len("hello")) > 3:
    print(f"{n=}")                              # f-string debug specifier

# Positional-only parameters
def power(base, exp, /): return base ** exp
print(power(2, 5))

# ---- 3.9 ----
a, b = {"x": 1}, {"y": 2}
print(a | b)                                    # dict union
nums: list[int] = [1, 2]                        # builtin generics, no typing.List
print("v1.2".removeprefix("v"))
from functools import cache
@cache
def sq(n): return n * n
print(sq(9))

# ---- 3.10 ----
# Structural pattern matching
def handle(cmd):
    match cmd:
        case ["go", direction]:
            return f"going {direction}"
        case ["pick", ("sword" | "shield") as item]:
            return f"picked {item}"
        case {"type": "user", "name": str(name)}:
            return f"user {name}"
        case [first, *rest] if rest:
            return f"{first} + {len(rest)} more"
        case int(x) | float(x):
            return f"number {x}"
        case None:
            return "nothing"
        case _:
            return "unknown"

for c in (["go", "north"], ["pick", "sword"], {"type": "user", "name": "Ada"},
          [1, 2, 3], 4.5, None, "zzz"):
    print(handle(c))

@dataclass
class Point:
    x: int
    y: int
match Point(0, 5):
    case Point(x=0, y=y):
        print("on y axis at", y)

# Union types with |
def f(x: int | str | None) -> int | None:
    return x if isinstance(x, int) else None
print(isinstance(3, int | str))

# zip(strict=True) catches length bugs
try:
    list(zip([1, 2], [1], strict=True))
except ValueError as e:
    print("strict zip:", e)

# dataclass slots / kw_only (3.10)
@dataclass(slots=True, kw_only=True)
class User:
    name: str
    age: int = 0
print(User(name="Ada"))

# Parenthesized context managers (3.10)
with (open(__file__) as f1, open(__file__) as f2):
    print(f1.readline().strip() == f2.readline().strip())

import itertools
print(list(itertools.pairwise([1, 2, 3, 4])))   # 3.10
print(sys.version_info >= (3, 10))
