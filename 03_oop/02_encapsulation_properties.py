"""02 - Encapsulation: naming conventions and @property."""

class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner           # public
        self._balance = balance      # "protected" by convention
        self.__pin = "1234"          # name-mangled -> _BankAccount__pin

    # Read-only computed property
    @property
    def balance(self) -> float:
        return self._balance

    @property
    def owner_upper(self):
        return self.owner.upper()

    # Property with validation (getter/setter/deleter)
    @property
    def nickname(self):
        return getattr(self, "_nickname", None)

    @nickname.setter
    def nickname(self, value):
        if not value:
            raise ValueError("nickname cannot be empty")
        self._nickname = value

    @nickname.deleter
    def nickname(self):
        del self._nickname

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount


acct = BankAccount("ada", 100)
acct.deposit(50)
acct.nickname = "savings"
print(acct.balance, acct.owner_upper, acct.nickname)
try:
    acct.balance = 5            # no setter -> AttributeError
except AttributeError as e:
    print("blocked:", e)
print(acct._BankAccount__pin)   # mangling is not real security
