"""08 - dataclasses, enums, __slots__, namedtuple/NamedTuple."""
from dataclasses import dataclass, field, asdict, replace
from enum import Enum, IntEnum, Flag, auto
from typing import NamedTuple

# --- dataclass: auto __init__, __repr__, __eq__ ---
@dataclass(order=True, frozen=True, slots=True)
class Point:
    x: float
    y: float = 0.0

p = Point(1, 2)
print(p, p == Point(1, 2), p < Point(2, 0), asdict(p), replace(p, y=9))

@dataclass
class Team:
    name: str
    members: list[str] = field(default_factory=list)   # never use [] as default
    id: int = field(default=0, repr=False)

    def __post_init__(self):
        self.name = self.name.strip().title()
t = Team("  rockets ")
t.members.append("Ada")
print(t)

@dataclass(kw_only=True)
class Config:
    host: str
    port: int = 8000
print(Config(host="localhost"))

# --- Enums ---
class Color(Enum):
    RED = 1
    GREEN = 2
print(Color.RED, Color(2), Color["GREEN"].name, [c.name for c in Color])

class Priority(IntEnum):
    LOW = 1
    HIGH = 2
print(Priority.HIGH > Priority.LOW)

class Perm(Flag):
    R = auto(); W = auto(); X = auto()
print(Perm.R | Perm.W, Perm.R in (Perm.R | Perm.W))

# --- __slots__: no per-instance __dict__, less memory ---
class Slim:
    __slots__ = ("a", "b")
    def __init__(self, a, b): self.a, self.b = a, b
s = Slim(1, 2)
try:
    s.c = 3
except AttributeError as e:
    print("slots block new attrs:", e)

# --- NamedTuple ---
class Coord(NamedTuple):
    lat: float
    lon: float
print(Coord(1.0, 2.0), Coord(1.0, 2.0).lat)
