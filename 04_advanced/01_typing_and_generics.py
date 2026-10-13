"""01 - Type hints, generics, TypedDict, Literal, overloads (check with mypy/pyright)."""
from typing import (Any, Callable, Generic, Iterable, Literal, Optional, Protocol,
                    TypedDict, TypeVar, overload, Final, ClassVar, Annotated, cast)

T = TypeVar("T")
Number = TypeVar("Number", int, float)

def first(items: Iterable[T]) -> T:
    return next(iter(items))

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    def push(self, item: T) -> None:
        self._items.append(item)
    def pop(self) -> T:
        return self._items.pop()

s = Stack[int](); s.push(1); print(s.pop(), first("abc"))

class Movie(TypedDict):
    title: str
    year: int
m: Movie = {"title": "Alien", "year": 1979}

Mode = Literal["r", "w"]
def open_mode(mode: Mode) -> str: return mode

MAX: Final = 10

@overload
def parse(x: str) -> int: ...
@overload
def parse(x: bytes) -> str: ...
def parse(x):
    return int(x) if isinstance(x, str) else x.decode()
print(parse("5"), parse(b"hi"))

def maybe(x: Optional[int] = None) -> int | None:    # `X | None` preferred (3.10+)
    return x

Handler = Callable[[str], int]
UserId = Annotated[int, "must be positive"]

# Type hints are NOT enforced at runtime. Run a checker:
#   pip install mypy && mypy .
print(Stack.__orig_bases__)
