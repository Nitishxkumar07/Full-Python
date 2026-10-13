# 05 - Packaging & Tooling (reference)

## Virtual environments
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Modern project layout (`pyproject.toml`)
```toml
[project]
name = "mypkg"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["requests>=2.32"]

[project.optional-dependencies]
dev = ["pytest", "ruff", "mypy"]

[project.scripts]
mycli = "mypkg.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```
Prefer the `src/` layout: `src/mypkg/__init__.py`, `tests/`.

## Tools worth knowing
| Purpose | Tool |
|---|---|
| Fast installer / env manager | `uv` (or pip + venv) |
| Lint + format | `ruff` (replaces flake8, isort, black) |
| Type check | `mypy`, `pyright` |
| Tests | `pytest`, `pytest-cov`, `hypothesis` |
| Task runner | `make`, `nox`, `tox` |
| Git hooks | `pre-commit` |

## Quality gate
```bash
ruff check . && ruff format --check . && mypy . && pytest -q
```
