import importlib.util
import subprocess
import sys
from pathlib import Path

EXAMPLE = Path(__file__).resolve().parents[1] / "dictionary_example" / "rps_dict_of_dicts.py"


def load():
    spec = importlib.util.spec_from_file_location("rps_dict_of_dicts", EXAMPLE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_table_is_complete_and_consistent():
    rps = load()
    moves = set(rps.rules)
    assert moves == {"rock", "paper", "scissors"}
    flip = {"win": "lose", "lose": "win", "tie": "tie"}
    for a in moves:
        assert set(rps.rules[a]) == moves
        assert rps.judge(a, a) == "tie"
        for b in moves:
            assert rps.judge(a, b) == flip[rps.judge(b, a)]


def test_demo_runs_and_is_deterministic():
    runs = [
        subprocess.run([sys.executable, str(EXAMPLE)], capture_output=True, text=True, check=True).stdout
        for _ in range(2)
    ]
    assert runs[0] == runs[1]
    assert "Score -> win: 2, lose: 1, tie: 1" in runs[0]


def test_play_rejects_bad_move():
    out = subprocess.run(
        [sys.executable, str(EXAMPLE), "play"], input="bogus\nquit\n", capture_output=True, text=True, check=True
    ).stdout
    assert "Not a valid move" in out
