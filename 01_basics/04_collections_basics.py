"""04 - list, tuple, set, dict, comprehensions."""

# --- list: ordered, mutable ---
nums = [3, 1, 2]
nums.append(4); nums.extend([5, 6]); nums.insert(0, 0)
nums.remove(3); popped = nums.pop()
nums.sort(); print(nums, popped, sorted(nums, reverse=True))
print(nums[1:3], len(nums), 2 in nums, nums.index(2))

# --- copying: shallow vs deep ---
import copy
nested = [[1, 2], [3]]
shallow = nested.copy()
deep = copy.deepcopy(nested)
nested[0].append(99)
print(shallow, deep)                     # shallow shares inner list

# --- tuple: ordered, immutable, hashable (if contents are) ---
point = (1, 2)
x, y = point
single = (1,)                            # comma makes the tuple

# --- set: unique, unordered, fast membership ---
a, b = {1, 2, 3}, {3, 4}
print(a | b, a & b, a - b, a ^ b)
print(set([1, 1, 2]))

# --- dict: key -> value (insertion-ordered since 3.7) ---
user = {"name": "Ada", "age": 36}
user["email"] = "ada@x.io"
print(user.get("phone", "n/a"), user.keys(), list(user.values()))
user.setdefault("tags", []).append("admin")
merged = user | {"age": 37}              # 3.9+ union
print(merged)
user.pop("email")

# --- Comprehensions ---
squares = [n * n for n in range(6) if n % 2 == 0]
lookup = {w: len(w) for w in ["a", "bb", "ccc"]}
unique = {n % 3 for n in range(10)}
gen = (n * 2 for n in range(3))          # lazy generator expression
print(squares, lookup, unique, list(gen))

# --- Sorting with key ---
people = [("Bo", 30), ("Al", 25)]
print(sorted(people, key=lambda p: p[1]))

# --- Useful built-ins ---
print(sum([1, 2]), min(3, 1), max([4, 9]), any([0, 1]), all([1, 1]))
print(list(map(str, [1, 2])), list(filter(None, [0, 1, 2])))
