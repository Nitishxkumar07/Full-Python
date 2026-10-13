"""04 - Profiling, timeit, memory, and fast-Python idioms."""
import timeit
import cProfile
import pstats
import io
import tracemalloc
import sys

# --- timeit: micro-benchmarks ---
print("list comp :", timeit.timeit("[i*i for i in range(1000)]", number=2000))
print("map+lambda:", timeit.timeit("list(map(lambda i: i*i, range(1000)))", number=2000))

# --- Membership: list O(n) vs set O(1) ---
data_list, data_set = list(range(10_000)), set(range(10_000))
print("list in:", timeit.timeit("9999 in l", globals={"l": data_list}, number=2000))
print("set  in:", timeit.timeit("9999 in s", globals={"s": data_set}, number=2000))

# --- String building: join, not +=  ---
parts = [str(i) for i in range(1000)]
fast = "".join(parts)

# --- cProfile ---
def work():
    return sorted(str(i) for i in range(50_000))
pr = cProfile.Profile(); pr.enable(); work(); pr.disable()
out = io.StringIO()
pstats.Stats(pr, stream=out).sort_stats("cumulative").print_stats(3)
print(out.getvalue().splitlines()[0])

# --- tracemalloc: find memory hogs ---
tracemalloc.start()
big = [bytearray(1000) for _ in range(1000)]
current, peak = tracemalloc.get_traced_memory()
print(f"current={current/1e6:.1f}MB peak={peak/1e6:.1f}MB")
tracemalloc.stop()

# --- Generators vs lists in memory ---
print(sys.getsizeof([i for i in range(100_000)]), sys.getsizeof(i for i in range(100_000)))

# Tips: use built-ins, local variable caching in hot loops, __slots__, array/numpy for numerics,
# lru_cache for pure functions, multiprocessing for CPU-bound, profile BEFORE optimizing.
