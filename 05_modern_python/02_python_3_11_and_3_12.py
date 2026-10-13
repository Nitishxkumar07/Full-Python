"""02 - Modern features: 3.11 and 3.12."""
import asyncio
import itertools
import tomllib
from enum import StrEnum
from typing import Self, override, TypedDict, NotRequired

# ================= 3.11 =================
# Exception groups and except*
def run():
    raise ExceptionGroup("batch", [ValueError("bad value"), TypeError("bad type")])
try:
    run()
except* ValueError as eg:
    print("value errors:", [str(e) for e in eg.exceptions])
except* TypeError as eg:
    print("type errors:", [str(e) for e in eg.exceptions])

# Exception notes
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        e.add_note("while computing ratio")
        raise
except ZeroDivisionError as e:
    print(e.__notes__)

# tomllib: built-in TOML reader
cfg = tomllib.loads('[server]\nport = 8080\ndebug = true')
print(cfg["server"]["port"])

# StrEnum, Self type
class Env(StrEnum):
    DEV = "dev"
    PROD = "prod"
print(Env.DEV == "dev", f"{Env.PROD}")

class Builder:
    def __init__(self): self.parts: list[str] = []
    def add(self, p: str) -> Self:          # fluent API that works with subclasses
        self.parts.append(p); return self
print(Builder().add("a").add("b").parts)

class Opts(TypedDict):
    name: str
    debug: NotRequired[bool]

async def tg():
    async with asyncio.TaskGroup() as g:    # structured concurrency
        t = g.create_task(asyncio.sleep(0.01, "done"))
    return t.result()
print(asyncio.run(tg()))

# ================= 3.12 =================
# PEP 695: new generic syntax and `type` aliases
def largest[T: (int, float)](items: list[T]) -> T:
    return max(items)

class Box[T]:
    def __init__(self, item: T): self.item = item
    def get(self) -> T: return self.item

type Matrix = list[list[float]]
type Pair[A, B] = tuple[A, B]
print(largest([3, 9, 2]), Box("x").get(), Matrix.__value__)

# @override decorator catches typos in method names (checked by type checkers)
class Base:
    def run(self) -> str: return "base"
class Child(Base):
    @override
    def run(self) -> str: return "child"
print(Child().run())

# More flexible f-strings (nested quotes, multi-line expressions, backslashes)
songs = ["a", "b"]
print(f"{', '.join(songs)}")
print(f"{"\n".join(songs)}")                # same-quote reuse is legal in 3.12

# itertools.batched
print(list(itertools.batched(range(7), 3)))

# pathlib.Path.walk, better error messages, per-interpreter GIL (internal)
from pathlib import Path
print(next(Path(".").walk())[0])
