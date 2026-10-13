"""03 - Conditionals and loops."""

# --- if / elif / else ---
score = 82
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(grade)

# --- Ternary expression ---
status = "pass" if score >= 50 else "fail"
print(status)

# --- for loops, range, enumerate, zip ---
for i in range(3):
    print("i =", i)
for idx, ch in enumerate("abc", start=1):
    print(idx, ch)
for n, l in zip([1, 2, 3], "xyz"):
    print(n, l)

# --- while with break / continue / else ---
n = 0
while True:
    n += 1
    if n == 2:
        continue
    if n > 4:
        break
    print("n =", n)

# for/else: else runs only if loop wasn't broken
for x in range(2, 10):
    if x * x > 20:
        print("found", x)
        break
else:
    print("no match")

# --- Walrus operator (3.8+) assigns inside an expression ---
data = [1, 2, 3, 4]
if (count := len(data)) > 3:
    print(f"{count} items")

# --- pass is a placeholder ---
def todo():
    pass

# --- Loop over dicts ---
d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)
