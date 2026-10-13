"""06 - Abstract Base Classes and structural typing (Protocol)."""
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

# --- ABC: cannot be instantiated; forces subclasses to implement ---
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @property
    @abstractmethod
    def name(self) -> str: ...

    def describe(self):                       # concrete method is fine
        return f"{self.name} with area {self.area():.2f}"

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2
    @property
    def name(self): return "circle"

print(Circle(2).describe())
try:
    Shape()
except TypeError as e:
    print("cannot instantiate:", e)

# --- Protocol: structural subtyping (static duck typing) ---
@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None: ...

class Conn:
    def close(self): print("closed")

def shutdown(x: Closeable): x.close()
shutdown(Conn())
print(isinstance(Conn(), Closeable))          # True without inheriting

# --- Virtual subclass registration ---
class Legacy: pass
Shape.register(Legacy)
print(issubclass(Legacy, Shape))
