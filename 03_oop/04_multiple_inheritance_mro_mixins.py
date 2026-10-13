"""04 - Multiple inheritance, MRO (C3 linearization), cooperative super(), mixins."""

class A:
    def hello(self): return ["A"]
class B(A):
    def hello(self): return ["B"] + super().hello()
class C(A):
    def hello(self): return ["C"] + super().hello()
class D(B, C):
    def hello(self): return ["D"] + super().hello()

print(D().hello())                            # ['D','B','C','A']
print([k.__name__ for k in D.__mro__])        # method resolution order

# --- Mixins: small reusable behaviours (no standalone use) ---
import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=True)

class ReprMixin:
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in vars(self).items())
        return f"{type(self).__name__}({attrs})"

class User(JsonMixin, ReprMixin):
    def __init__(self, name, age):
        self.name, self.age = name, age

u = User("Ada", 36)
print(u, u.to_json())
