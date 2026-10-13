"""11 - Common design patterns in Pythonic form."""
from abc import ABC, abstractmethod
from typing import Callable

# --- Factory ---
class Shape(ABC):
    @abstractmethod
    def draw(self): ...
class Sq(Shape):
    def draw(self): return "square"
class Ci(Shape):
    def draw(self): return "circle"
def shape_factory(kind: str) -> Shape:
    return {"square": Sq, "circle": Ci}[kind]()
print(shape_factory("circle").draw())

# --- Singleton (module-level object is the most Pythonic singleton) ---
class _Config: pass
config = _Config()

# --- Observer ---
class EventBus:
    def __init__(self): self._subs: dict[str, list[Callable]] = {}
    def subscribe(self, event, fn): self._subs.setdefault(event, []).append(fn)
    def publish(self, event, data): [fn(data) for fn in self._subs.get(event, [])]
bus = EventBus()
bus.subscribe("saved", lambda d: print("log:", d))
bus.subscribe("saved", lambda d: print("email:", d))
bus.publish("saved", "doc1")

# --- Strategy (functions are first-class, so no class needed) ---
def tax_us(x): return x * 1.07
def tax_eu(x): return x * 1.20
def checkout(total, strategy: Callable[[float], float]): return round(strategy(total), 2)
print(checkout(100, tax_us), checkout(100, tax_eu))

# --- Decorator pattern (see 02_intermediate) & Command ---
class Command:
    def __init__(self, do, undo): self.do, self.undo = do, undo
stack = []
state = {"n": 0}
inc = Command(lambda: state.update(n=state["n"] + 1), lambda: state.update(n=state["n"] - 1))
inc.do(); stack.append(inc); inc.do(); stack.append(inc)
stack.pop().undo(); print(state)

# --- Builder with fluent interface ---
class Query:
    def __init__(self): self.parts = []
    def select(self, *c): self.parts.append("SELECT " + ", ".join(c)); return self
    def frm(self, t): self.parts.append("FROM " + t); return self
    def where(self, c): self.parts.append("WHERE " + c); return self
    def build(self): return " ".join(self.parts)
print(Query().select("id", "name").frm("users").where("age > 18").build())
