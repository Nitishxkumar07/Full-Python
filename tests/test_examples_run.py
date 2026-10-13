"""Smoke test: every study script must run without errors."""
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = sorted(p for d in ("01_basics", "02_intermediate", "03_oop", "04_advanced", "05_modern_python")
                 for p in (ROOT / d).glob("*.py"))


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: f"{p.parent.name}/{p.name}")
def test_script_runs(script):
    result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, timeout=60)
    assert result.returncode == 0, result.stderr
