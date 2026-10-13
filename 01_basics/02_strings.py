"""02 - Strings: slicing, methods, formatting."""

s = "Hello, Python"

# --- Indexing & slicing: s[start:stop:step] ---
print(s[0], s[-1], s[0:5], s[::-1], s[::2])

# --- Strings are immutable ---
# s[0] = "J"  -> TypeError
s2 = "J" + s[1:]
print(s2)

# --- Common methods ---
print(s.upper(), s.lower(), s.title(), s.swapcase())
print("  pad  ".strip(), "a,b,c".split(","), "-".join(["a", "b", "c"]))
print(s.replace("Python", "World"), s.find("Py"), s.count("l"))
print(s.startswith("Hello"), s.endswith("on"), "123".isdigit(), "abc".isalpha())
print("py".center(10, "*"), "7".zfill(3), "Hello"[1:-1])

# --- Formatting: f-strings are the modern default ---
name, price = "Tea", 3.14159
print(f"{name} costs ${price:.2f}")
print(f"{1234567:,}  {0.256:.1%}  {42:08b}  {255:#x}  {name:>8}|{name:<8}|{name:^8}")
print(f"{name=}  {price=:.1f}")             # debug specifier (3.8+)
print("{} costs {}".format(name, price))    # older style
print("%s costs %.1f" % (name, price))      # oldest style

# --- Multiline & raw strings ---
text = """line one
line two"""
print(text.splitlines())
print(r"C:\new\table")                       # raw: backslashes are literal

# --- Bytes vs str (encoding) ---
encoded = "héllo".encode("utf-8")
print(encoded, encoded.decode("utf-8"))

# --- 3.9+ prefix/suffix helpers ---
print("test_file.py".removeprefix("test_").removesuffix(".py"))
