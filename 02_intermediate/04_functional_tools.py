"""04 - functools, itertools, operator, collections."""
import functools, itertools, operator
from collections import Counter, defaultdict, deque, namedtuple, ChainMap, OrderedDict

# --- functools ---
print(functools.reduce(operator.mul, [1, 2, 3, 4]))
add5 = functools.partial(operator.add, 5)
print(add5(10))

@functools.lru_cache(maxsize=128)
def square(n): return n * n
square(3); print(square.cache_info())

@functools.singledispatch
def describe(x): return "something"
@describe.register
def _(x: int): return "an int"
@describe.register
def _(x: list): return "a list"
print(describe(1), describe([1]), describe("s"))

@functools.total_ordering
class Version:
    def __init__(self, n): self.n = n
    def __eq__(self, o): return self.n == o.n
    def __lt__(self, o): return self.n < o.n
print(Version(1) <= Version(2))

# --- itertools ---
print(list(itertools.chain([1], [2, 3])))
print(list(itertools.product("ab", [1, 2])))
print(list(itertools.permutations([1, 2, 3], 2)))
print(list(itertools.combinations("abc", 2)))
print(list(itertools.accumulate([1, 2, 3, 4])))
print([(k, list(g)) for k, g in itertools.groupby("aabbb")])
print(list(itertools.islice(itertools.count(10, 5), 3)))
print(list(itertools.zip_longest([1, 2], "a", fillvalue="-")))
print(list(itertools.starmap(pow, [(2, 3), (3, 2)])))

# --- collections ---
c = Counter("banana"); print(c.most_common(1))
dd = defaultdict(list); dd["x"].append(1); print(dict(dd))
dq = deque([1, 2, 3], maxlen=3); dq.append(4); dq.appendleft(0); print(dq)
Point = namedtuple("Point", "x y"); print(Point(1, 2)._asdict())
print(ChainMap({"a": 1}, {"a": 2, "b": 3})["a"])

# --- operator module (faster than lambdas) ---
people = [("Al", 30), ("Bo", 25)]
print(sorted(people, key=operator.itemgetter(1)))
