"""01 - Classes, objects, instance vs class attributes, methods."""

class Dog:
    species = "Canis familiaris"          # class attribute (shared)
    count = 0

    def __init__(self, name: str, age: int):
        self.name = name                  # instance attributes
        self.age = age
        Dog.count += 1

    # instance method
    def bark(self) -> str:
        return f"{self.name} says woof"

    # class method: receives the class; great for alternative constructors
    @classmethod
    def from_string(cls, text: str) -> "Dog":
        name, age = text.split(",")
        return cls(name.strip(), int(age))

    # static method: no self/cls, just a namespaced function
    @staticmethod
    def is_valid_age(age: int) -> bool:
        return 0 <= age < 40

    def __repr__(self):                   # developer-friendly (for debugging)
        return f"Dog(name={self.name!r}, age={self.age})"

    def __str__(self):                    # user-friendly (print)
        return f"{self.name} ({self.age})"


rex = Dog("Rex", 3)
fido = Dog.from_string("Fido, 5")
print(rex.bark(), repr(fido), str(fido), Dog.count)
print(Dog.is_valid_age(50), rex.species, vars(rex))

# Instance attribute shadows class attribute; class attribute unchanged.
rex.species = "wolf"
print(rex.species, fido.species, Dog.species)

# Dynamic attribute access
setattr(rex, "color", "brown")
print(getattr(rex, "color"), hasattr(rex, "weight"), isinstance(rex, Dog))
