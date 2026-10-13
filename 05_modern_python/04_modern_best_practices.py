"""04 - Modern idioms you should use today."""
from __future__ import annotations
import argparse
import logging
import shutil
import subprocess
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path

# 1) pathlib over os.path
cfg = Path.home() / ".config" / "app.toml"

# 2) f-strings, dataclasses, enums, type hints everywhere
@dataclass(frozen=True, slots=True)
class Job:
    name: str
    retries: int = 3

# 3) Use collections.abc and builtin generics for annotations
def chunks(items: Sequence[int], size: int) -> Iterator[Sequence[int]]:
    for i in range(0, len(items), size):
        yield items[i:i + size]
print(list(chunks([1, 2, 3, 4, 5], 2)))

# 4) subprocess: no shell=True, always check
if shutil.which("echo"):
    out = subprocess.run(["echo", "hi"], capture_output=True, text=True, check=True)
    print(out.stdout.strip())

# 5) argparse CLI
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="demo")
    p.add_argument("path", nargs="?", default=".")
    p.add_argument("-v", "--verbose", action="store_true")
    return p
args = build_parser().parse_args([])
logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)

# 6) Secrets: never hardcode; read from environment
import os, secrets
token = os.environ.get("API_TOKEN") or secrets.token_hex(8)

# 7) Safe parsing/serialisation: json/tomllib, never pickle untrusted data,
#    never eval user input, parameterised SQL queries only.
import sqlite3
con = sqlite3.connect(":memory:")
con.execute("create table t (name text)")
con.execute("insert into t values (?)", ("Robert'); DROP TABLE t;--",))
print(con.execute("select count(*) from t").fetchone())

# 8) Prefer `uv`/venv, ruff, mypy, pytest -- see 04_advanced/05_packaging_and_tooling.md
