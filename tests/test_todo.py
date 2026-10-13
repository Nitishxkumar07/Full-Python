"""pytest examples: fixtures, parametrize, raises, tmp_path, capsys."""
import pytest
from todo import Status, TaskStore, main


@pytest.fixture
def store(tmp_path):
    return TaskStore(tmp_path / "tasks.json")


def test_add_assigns_incrementing_ids(store):
    assert store.add("a").id == 1
    assert store.add("b").id == 2


def test_persistence(tmp_path):
    path = tmp_path / "t.json"
    TaskStore(path).add("persist me")
    assert TaskStore(path).tasks[0].title == "persist me"


def test_complete_and_remove(store):
    t = store.add("x")
    assert store.complete(t.id).status is Status.DONE
    store.remove(t.id)
    assert store.tasks == []


@pytest.mark.parametrize("bad_id", [0, 99, -1])
def test_unknown_id_raises(store, bad_id):
    with pytest.raises(KeyError):
        store.complete(bad_id)


def test_cli_list(tmp_path, capsys):
    f = str(tmp_path / "c.json")
    assert main(["--file", f, "add", "hello"]) == 0
    assert main(["--file", f, "list"]) == 0
    assert "[ ] 1: hello" in capsys.readouterr().out


def test_cli_error_code(tmp_path):
    assert main(["--file", str(tmp_path / "c.json"), "done", "5"]) == 1
