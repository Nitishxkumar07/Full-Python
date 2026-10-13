"""03 - Inheritance, super(), method overriding, polymorphism, duck typing."""

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("subclass must implement")
    def describe(self):
        return f"{self.name}: {self.speak()}"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name)        # call parent initializer
        self.indoor = indoor
    def speak(self):
        return "Meow"

# Polymorphism: same call, different behaviour
for a in (Dog("Rex"), Cat("Tom")):
    print(a.describe())

print(issubclass(Cat, Animal), isinstance(Dog("x"), Animal), Cat.__mro__)

# Duck typing: "if it quacks like a duck" -- no inheritance required
class Robot:
    def speak(self):
        return "Beep"
def make_noise(thing):
    return thing.speak()
print(make_noise(Robot()), make_noise(Dog("d")))
