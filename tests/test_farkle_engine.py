"""Tests for the Farkle scoring/turn engine (lessons/code/farkle/engine.py).

Run from the computer_science_1 repo root:

    PYTHONPATH=lessons/code pytest tests/test_farkle_engine.py -v

These tests exist so the Week 16 demo can be trusted: a buggy dice engine
would ruin the lesson (a class could watch a "learner" that is really just
learning to exploit a scoring bug). Every rule documented in engine.py's
module docstring has at least one test here.
"""

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lessons" / "code"))

from farkle import engine  # noqa: E402


def test_single_one_scores_100():
    assert engine.score_roll([1, 2, 3, 4, 6, 6]) == (100, 1)


def test_single_five_scores_50():
    assert engine.score_roll([5, 2, 3, 4, 6, 6]) == (50, 1)


def test_no_scoring_dice_is_farkle():
    points, used = engine.score_roll([2, 3, 4, 6, 6, 2])
    assert points == 0
    assert used == 0
    assert engine.is_farkle(points) is True


def test_three_of_a_kind_non_one():
    # Three 4s -> 4 * 100 = 400
    assert engine.score_roll([4, 4, 4, 2, 3, 6]) == (400, 3)


def test_three_ones_scores_1000():
    assert engine.score_roll([1, 1, 1, 2, 3, 6]) == (1000, 3)


def test_four_of_a_kind_doubles_three_of_a_kind():
    # Four 2s -> three-of-a-kind value 200, doubled once (2x) = 400
    assert engine.score_roll([2, 2, 2, 2, 3, 6]) == (400, 4)


def test_five_of_a_kind_quadruples_three_of_a_kind():
    # Five 3s -> three-of-a-kind value 300, doubled twice (4x) = 1200
    assert engine.score_roll([3, 3, 3, 3, 3, 6]) == (1200, 5)


def test_six_of_a_kind_octuples_three_of_a_kind():
    # Six 1s -> 1000 * 8 = 8000
    assert engine.score_roll([1, 1, 1, 1, 1, 1]) == (8000, 6)


def test_triple_plus_leftover_singles():
    # Three 6s (600) plus a leftover 1 (100) plus a leftover 5 (50) = 750
    # dice used: 3 + 1 + 1 = 5; the remaining 4 does not score.
    assert engine.score_roll([6, 6, 6, 1, 5, 4]) == (750, 5)


def test_all_non_scoring_dice_never_used():
    points, used = engine.score_roll([2, 2, 3, 3, 4, 6])
    assert points == 0
    assert used == 0


def test_roll_dice_is_reproducible_with_same_seed():
    rng_a = random.Random(42)
    rng_b = random.Random(42)
    assert engine.roll_dice(6, rng_a) == engine.roll_dice(6, rng_b)


def test_roll_dice_returns_requested_count_in_range():
    rng = random.Random(7)
    dice = engine.roll_dice(6, rng)
    assert len(dice) == 6
    assert all(1 <= die <= 6 for die in dice)


def test_take_turn_never_returns_negative():
    rng = random.Random(3)
    always_roll = lambda state: "roll"  # noqa: E731
    for _ in range(200):
        points = engine.take_turn(rng, always_roll, total_score=0)
        assert points >= 0


def test_take_turn_bank_immediately_after_first_score():
    rng = random.Random(9)
    bank_first = lambda state: "bank"  # noqa: E731
    points = engine.take_turn(rng, bank_first, total_score=0)
    # Either 0 (first roll farkled) or a positive score from banking
    # immediately after the first scoring roll.
    assert points >= 0


def test_take_turn_is_reproducible_with_same_seed():
    bank_at_300 = lambda state: "bank" if state["turn_score"] >= 300 else "roll"  # noqa: E731
    points_a = engine.take_turn(random.Random(123), bank_at_300, total_score=0)
    points_b = engine.take_turn(random.Random(123), bank_at_300, total_score=0)
    assert points_a == points_b


def test_take_turn_trace_records_every_roll():
    rng = random.Random(5)
    trace: list = []
    bank_first = lambda state: "bank"  # noqa: E731
    engine.take_turn(rng, bank_first, total_score=0, trace=trace)
    assert len(trace) >= 1
    assert any("rolled" in line for line in trace)


def test_build_state_has_expected_keys():
    state = engine.build_state(turn_score=100, dice_remaining=4,
                                total_score=500, target_score=4000,
                                opponent_score=200)
    assert state == {
        "turn_score": 100,
        "dice_remaining": 4,
        "total_score": 500,
        "target_score": 4000,
        "opponent_score": 200,
    }
