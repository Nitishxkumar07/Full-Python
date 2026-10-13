"""A small, well-structured CLI to-do app: dataclasses, enums, pathlib, json, argparse, typing."""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from datetime import date
from enum import StrEnum
from pathlib import Path


class Status(StrEnum):
    TODO = "todo"
    DONE = "done"


@dataclass
class Task:
    id: int
    title: str
    status: Status = Status.TODO
    created: str = field(default_factory=lambda: date.today().isoformat())


class TaskStore:
    """Persists tasks to a JSON file."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.tasks: list[Task] = self._load()

    def _load(self) -> list[Task]:
        if not self.path.exists():
            return []
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        return [Task(**{**t, "status": Status(t["status"])}) for t in raw]

    def save(self) -> None:
        data = [asdict(t) for t in self.tasks]
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def add(self, title: str) -> Task:
        task = Task(id=max((t.id for t in self.tasks), default=0) + 1, title=title)
        self.tasks.append(task)
        self.save()
        return task

    def complete(self, task_id: int) -> Task:
        task = self._get(task_id)
        task.status = Status.DONE
        self.save()
        return task

    def remove(self, task_id: int) -> None:
        self.tasks.remove(self._get(task_id))
        self.save()

    def _get(self, task_id: int) -> Task:
        for t in self.tasks:
            if t.id == task_id:
                return t
        raise KeyError(f"no task with id {task_id}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="todo", description="Tiny to-do manager")
    p.add_argument("--file", type=Path, default=Path("tasks.json"))
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    add = sub.add_parser("add"); add.add_argument("title")
    done = sub.add_parser("done"); done.add_argument("id", type=int)
    rm = sub.add_parser("rm"); rm.add_argument("id", type=int)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    store = TaskStore(args.file)
    try:
        match args.cmd:
            case "add":
                t = store.add(args.title); print(f"added #{t.id}: {t.title}")
            case "done":
                t = store.complete(args.id); print(f"completed #{t.id}")
            case "rm":
                store.remove(args.id); print(f"removed #{args.id}")
            case "list":
                for t in store.tasks:
                    mark = "x" if t.status is Status.DONE else " "
                    print(f"[{mark}] {t.id}: {t.title}")
    except KeyError as e:
        print(f"error: {e.args[0]}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
