"""09 - Descriptors, __getattr__, __setattr__, __init_subclass__, __class_getitem__."""

# --- Descriptor: reusable attribute logic (how property works under the hood) ---
class Positive:
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, obj, objtype=None):
        if obj is None: return self
        return getattr(obj, self.name)
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name[1:]} must be positive")
        setattr(obj, self.name, value)

class Product:
    price = Positive()
    qty = Positive()
    def __init__(self, price, qty):
        self.price, self.qty = price, qty

p = Product(10, 2)
print(p.price, p.qty)
try:
    p.price = -1
except ValueError as e:
    print(e)

# --- Dynamic attribute hooks ---
class Config:
    def __init__(self, **kw): self.__dict__.update(kw)
    def __getattr__(self, name):               # called only when normal lookup fails
        return f"<missing {name}>"
    def __setattr__(self, name, value):
        print(f"set {name}")
        super().__setattr__(name, value)
c = Config(a=1)
print(c.a, c.nope)

# --- Hooks at class creation time ---
class Plugin:
    registry = {}
    def __init_subclass__(cls, key=None, **kw):
        super().__init_subclass__(**kw)
        Plugin.registry[key or cls.__name__.lower()] = cls

class Csv(Plugin, key="csv"): pass
class Json(Plugin): pass
print(Plugin.registry)

# --- Generic-like subscript syntax ---
class Box:
    def __class_getitem__(cls, item): return f"Box[{item.__name__}]"
print(Box[int])
