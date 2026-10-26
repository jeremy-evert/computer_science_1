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


def run(name, *args, stdin=None):
    return subprocess.run(
        [sys.executable, str(EXAMPLE.with_name(name)), *args], input=stdin, capture_output=True, text=True, check=True
    ).stdout


def load_named(name):
    path = EXAMPLE.with_name(name)
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_if_elif_and_dict_versions_agree_on_every_matchup():
    old = load_named("rps_if_elif.py")
    new = load_named("rps_dict_of_dicts.py")
    for a in ("rock", "paper", "scissors"):
        for b in ("rock", "paper", "scissors"):
            assert old.judge(a, b) == new.judge(a, b)


def test_if_elif_demo_runs_and_scores_match_dict_demo():
    old = run("rps_if_elif.py")
    new = run("rps_dict_of_dicts.py")
    assert "Score -> win: 2, lose: 1, tie: 1" in old
    assert [l for l in old.splitlines() if l.startswith("You:")] == [l for l in new.splitlines() if l.startswith("You:")]


def test_advanced_table_is_fair_and_symmetric():
    adv = load_named("rps_advanced_dict.py")
    assert len(adv.rules) == 7
    flip = {"win": "lose", "lose": "win", "tie": "tie"}
    for a in adv.rules:
        results = list(adv.rules[a].values())
        assert results.count("win") == 3 and results.count("lose") == 3 and results.count("tie") == 1
        for b in adv.rules:
            assert adv.judge(a, b) == flip[adv.judge(b, a)]


def test_advanced_demo_and_branch_counts():
    adv = load_named("rps_advanced_dict.py")
    assert [adv.old_way_branch_count(n) for n in (3, 5, 7, 9)] == [5, 12, 23, 38]
    assert "batman disarms glock" in run("rps_advanced_dict.py")
    assert "Not a valid move" in run("rps_advanced_dict.py", "play", stdin="bogus\nquit\n")
