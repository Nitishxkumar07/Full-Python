"""05 - Magic (dunder) methods and operator overloading."""
from functools import total_ordering
import math

@total_ordering
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self): return f"Vector({self.x}, {self.y})"
    def __add__(self, o): return Vector(self.x + o.x, self.y + o.y)
    def __sub__(self, o): return Vector(self.x - o.x, self.y - o.y)
    def __mul__(self, k): return Vector(self.x * k, self.y * k)
    __rmul__ = __mul__                         # support 3 * v
    def __neg__(self): return Vector(-self.x, -self.y)
    def __abs__(self): return math.hypot(self.x, self.y)
    def __eq__(self, o): return (self.x, self.y) == (o.x, o.y)
    def __lt__(self, o): return abs(self) < abs(o)
    def __hash__(self): return hash((self.x, self.y))
    def __bool__(self): return bool(abs(self))
    def __iter__(self): yield self.x; yield self.y
    def __getitem__(self, i): return (self.x, self.y)[i]
    def __len__(self): return 2
    def __call__(self, k): return self * k
    def __contains__(self, v): return v in (self.x, self.y)

v, w = Vector(1, 2), Vector(3, 4)
print(v + w, w - v, 3 * v, -v, abs(w), v < w, v == Vector(1, 2))
print(list(v), v[0], len(v), bool(Vector(0, 0)), v(10), 2 in v)
print({v: "a"}[Vector(1, 2)])

# --- Container protocol example ---
class Deck:
    def __init__(self): self.cards = list(range(1, 6))
    def __len__(self): return len(self.cards)
    def __getitem__(self, i): return self.cards[i]
d = Deck()
print(len(d), d[0], d[1:3], list(reversed(d)))     # iteration & slicing for free

# --- Object lifecycle ---
class Res:
    def __new__(cls, *a, **k):
        print("__new__ creates the object"); return super().__new__(cls)
    def __init__(self): print("__init__ initializes it")
    def __del__(self): print("__del__ called on cleanup")
Res()
