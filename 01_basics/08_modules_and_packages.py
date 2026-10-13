"""08 - Modules, imports, __name__ guard, useful stdlib."""
import math
import random
import sys
from collections import Counter
from datetime import datetime, timedelta
import os

# Import styles: `import x`, `from x import y`, `import x as z`.
print(math.sqrt(16), math.pi, math.floor(2.7), math.ceil(2.1))
random.seed(1)
print(random.randint(1, 10), random.choice("abc"))
print(Counter("mississippi").most_common(2))
print(datetime(2026, 1, 1) + timedelta(days=30))
print(sys.version_info[:2], os.name)

def main():
    print("running as script")

# Runs only when executed directly, not when imported.
if __name__ == "__main__":
    main()

# A *package* is a folder with modules (and optionally __init__.py).
# Install third-party packages in a virtual environment:
#   python -m venv .venv && source .venv/bin/activate && pip install requests
