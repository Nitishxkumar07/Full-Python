# Python Study: Basics to Advanced OOP and Modern Python

A hands-on, runnable course. Every file is a short lesson with comments and printed output.
Tested on **Python 3.12**. Newer-version features (3.13/3.14) are guarded so everything still runs on 3.12.

## Quick start
```bash
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt                      # only for tests/tooling
python 01_basics/01_variables_and_types.py           # run any lesson
./run_all.sh                                         # run all 33 lessons
pytest                                               # run tests (41)
```

## Learning path
| Folder | Topics |
|---|---|
| `01_basics` | variables and types, strings, control flow, list/tuple/set/dict, functions, exceptions, file I/O, modules |
| `02_intermediate` | iterators and generators, closures and decorators, context managers, functools/itertools/collections, regex/datetime/json/logging, testing |
| `03_oop` | classes, encapsulation and properties, inheritance and polymorphism, MRO and mixins, dunder methods, ABC and Protocol, composition and SOLID, dataclasses/enums/slots, descriptors, metaclasses, design patterns |
| `04_advanced` | typing and generics, threading/multiprocessing/asyncio, introspection and metaprogramming, performance and memory, packaging and tooling |
| `05_modern_python` | 3.8 to 3.10 (walrus, `match`, `X \| Y`), 3.11 to 3.12 (exception groups, `tomllib`, `type` statement, PEP 695 generics, `@override`), 3.13 and 3.14 overview, modern best practices |
| `06_projects` | `todo_cli` (a complete small app) and ideas for next projects |
| `tests` | pytest fixtures, parametrize, `tmp_path`, `capsys`, smoke tests for all lessons |

## Suggested order
1. Work through `01_basics` in order (about 1 week).
2. `02_intermediate`, then `03_oop` files 01 to 08 (about 2 weeks).
3. `03_oop` files 09 to 11, then `04_advanced` (about 2 weeks).
4. `05_modern_python`, then build the projects and extend them.

## How to study each file
1. Read it top to bottom, then run it.
2. Change values and predict the output before running again.
3. Break things on purpose (remove `functools.wraps`, add a mutable default) to see the failure.
4. Write your own version from memory without looking.

## Tooling cheat sheet
```bash
ruff check . && ruff format .     # lint and format
mypy .                            # static type check
pytest -x -q                      # stop at first failure
python -X dev file.py             # extra runtime checks
python -m cProfile -s cumtime file.py
```

## Publishing as a Git repo
```bash
git init && git add . && git commit -m "Initial commit: Python study"
git branch -M main
git remote add origin https://github.com/<you>/python-study.git
git push -u origin main
```

License: MIT.
