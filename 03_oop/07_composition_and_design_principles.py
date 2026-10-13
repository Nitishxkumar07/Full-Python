"""07 - Composition over inheritance, SOLID, dependency injection."""
from abc import ABC, abstractmethod

# "Has-a" beats "is-a" when behaviour varies independently.
class Engine:
    def start(self): return "engine on"

class Car:
    def __init__(self, engine: Engine):    # dependency injection
        self.engine = engine
    def start(self): return f"car: {self.engine.start()}"
print(Car(Engine()).start())

# --- SOLID in one small example ---
# S: each class has one reason to change
# O: open for extension, closed for modification
# L: subtypes substitute for base types
# I: small interfaces
# D: depend on abstractions

class Notifier(ABC):                       # abstraction (D, I)
    @abstractmethod
    def send(self, msg: str) -> str: ...

class Email(Notifier):
    def send(self, msg): return f"email: {msg}"
class SMS(Notifier):                       # added without editing OrderService (O)
    def send(self, msg): return f"sms: {msg}"

class OrderService:                        # single responsibility (S)
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    def place(self, item): return self.notifier.send(f"order placed: {item}")

print(OrderService(Email()).place("book"))
print(OrderService(SMS()).place("pen"))
