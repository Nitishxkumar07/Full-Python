"""01 - Iterators and generators."""

# --- Iterator protocol: __iter__ and __next__ ---
class Countdown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

print(list(Countdown(3)))

# --- Generator function: yield produces values lazily ---
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
print(list(islice(fib(), 10)))

# --- send(), yield from ---
def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

acc = accumulator(); next(acc)
print(acc.send(5), acc.send(10))

def chain(*iterables):
    for it in iterables:
        yield from it
print(list(chain([1, 2], "ab")))

# --- Generator expressions are memory efficient ---
print(sum(n * n for n in range(1_000_000)))
