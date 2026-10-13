"""01 - Variables, data types, type conversion, operators."""

# --- Variables: dynamically typed, names are references to objects ---
name = "Ada"          # str
age = 36              # int
height = 1.68         # float
is_dev = True         # bool
nothing = None        # NoneType
z = 3 + 4j            # complex

print(type(name), type(age), type(height), type(is_dev), type(nothing), type(z))

# --- Multiple assignment / swapping / unpacking ---
a, b, c = 1, 2, 3
a, b = b, a                       # swap without temp variable
first, *middle, last = [1, 2, 3, 4, 5]
print(a, b, first, middle, last)

# --- Type conversion ---
print(int("42"), float("3.5"), str(10), bool(0), bool("x"), list("abc"))

# --- Operators ---
print(7 / 2, 7 // 2, 7 % 2, 2 ** 10)          # true div, floor div, modulo, power
print(divmod(17, 5))                           # (3, 2)
print(1 < 2 < 3)                               # chained comparison
print(not True, True and False, True or False) # logical
print(5 & 3, 5 | 3, 5 ^ 3, ~5, 1 << 3, 16 >> 2)  # bitwise

# --- Identity vs equality ---
x = [1, 2]
y = [1, 2]
print(x == y, x is y)             # True False (equal value, different objects)

# --- Truthiness: empty containers, 0, None, "" are falsy ---
for value in (0, "", [], {}, None, "0", [0]):
    print(repr(value), "->", bool(value))

# --- Integers have arbitrary precision; floats do not ---
print(2 ** 100)
print(0.1 + 0.2 == 0.3)                       # False
import math
print(math.isclose(0.1 + 0.2, 0.3))           # True

# --- Constants by convention ---
MAX_RETRIES = 3

# --- Numeric literals with underscores ---
million = 1_000_000
print(million, 0b1010, 0o17, 0xFF)
