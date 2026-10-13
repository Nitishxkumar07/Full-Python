"""03 - Introspection, inspect, dynamic code, import hooks overview."""
import inspect
import importlib
import dis
import sys

def sample(a: int, b: str = "x", *args, **kw) -> bool:
    """Docstring."""
    return True

# --- Inspecting callables ---
sig = inspect.signature(sample)
print(sig, list(sig.parameters), sig.return_annotation)
print(inspect.getdoc(sample), inspect.isfunction(sample))
print(sample.__annotations__, sample.__code__.co_varnames)

# --- Introspecting objects ---
print([m for m in dir("s") if not m.startswith("_")][:5])
print(inspect.getmembers(sys.modules[__name__], inspect.isfunction)[0][0])

# --- Dynamic import ---
mod = importlib.import_module("math")
print(mod.sqrt(81))

# --- Bytecode ---
dis.dis(lambda x: x + 1)

# --- eval/exec/compile: powerful but dangerous with untrusted input! ---
ns = {}
exec("def sq(n): return n * n", ns)
print(ns["sq"](7))
import ast
print(ast.literal_eval("[1, 2, {'a': 3}]"))      # safe alternative to eval

# --- Monkey patching ---
class Greeter:
    def hi(self): return "hi"
Greeter.hi = lambda self: "patched"
print(Greeter().hi())

# --- Class decorators ---
def add_repr(cls):
    cls.__repr__ = lambda self: f"{cls.__name__}({vars(self)})"
    return cls
@add_repr
class P:
    def __init__(self): self.x = 1
print(P())

# --- weakref & gc ---
import gc, weakref
class Node: pass
n = Node(); r = weakref.ref(n)
del n; gc.collect()
print("weakref alive:", r() is not None)
print(sys.getsizeof([]), sys.getrefcount(sample) > 0)
