"""10 - Metaclasses: classes are objects, and `type` builds them."""

# Classes are instances of `type`.
print(type(int), type(type))

# Create a class dynamically.
Dyn = type("Dyn", (object,), {"x": 1, "hello": lambda self: "hi"})
print(Dyn().x, Dyn().hello())

# --- Custom metaclass: enforce rules / auto-register at class creation ---
class UpperAttrs(type):
    def __new__(mcls, name, bases, ns):
        ns = {(k if k.startswith("__") else k.upper()): v for k, v in ns.items()}
        return super().__new__(mcls, name, bases, ns)

class Settings(metaclass=UpperAttrs):
    debug = True
print(Settings.DEBUG)

class Singleton(type):
    _instances = {}
    def __call__(cls, *a, **kw):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*a, **kw)
        return cls._instances[cls]

class Db(metaclass=Singleton): pass
print(Db() is Db())

# Rule of thumb: prefer decorators, __init_subclass__, or dataclasses.
# Reach for metaclasses only for deep framework-level needs (ORMs, enums).
