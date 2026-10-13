"""06 - Exception handling."""

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as exc:
        print("cannot divide by zero:", exc)
        return None
    except (TypeError, ValueError):
        print("bad types")
        raise                      # re-raise current exception
    else:
        return result              # runs only if no exception
    finally:
        print("cleanup always runs")

print(divide(4, 2))
print(divide(1, 0))

# --- Custom exceptions ---
class ValidationError(Exception):
    def __init__(self, field, message):
        super().__init__(f"{field}: {message}")
        self.field = field

def validate_age(age):
    if age < 0:
        raise ValidationError("age", "must be >= 0")
    return age

try:
    validate_age(-1)
except ValidationError as e:
    print("caught:", e, "| field =", e.field)

# --- Exception chaining ---
try:
    try:
        int("abc")
    except ValueError as e:
        raise RuntimeError("config parse failed") from e
except RuntimeError as e:
    print(e, "<-", repr(e.__cause__))

# --- assert (for developer checks, not user input) ---
assert 1 + 1 == 2, "math is broken"
