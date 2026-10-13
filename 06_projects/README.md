# Projects

## todo_cli
```bash
cd 06_projects/todo_cli
python todo.py add "Learn decorators"
python todo.py add "Read about asyncio"
python todo.py done 1
python todo.py list
python todo.py rm 2
```
Concepts used: dataclasses, StrEnum, pathlib, json, argparse subcommands, `match`, type hints.

## Ideas to build next
1. Expense tracker with SQLite (`sqlite3`) and a report command.
2. Async web scraper (`asyncio` + `httpx`) with rate limiting.
3. REST API with FastAPI + pydantic + pytest.
4. Plugin system using `__init_subclass__` and entry points.
