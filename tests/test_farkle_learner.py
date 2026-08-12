"""Tests for the experience-table learner and simulation/comparison code.

Run from the computer_science_1 repo root:

    PYTHONPATH=lessons/code pytest tests/test_farkle_learner.py -v

These are smoke tests: they check the learning/experiment code executes
end to end and behaves sensibly (tables grow, averages move in a sane
direction, comparisons are reproducible) -- not that a stochastic learner
hits some exact "magic" win rate, which the prompt explicitly rules out
as a requirement.
"""

import random
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lessons" / "code"))

from farkle import engine, learner, simulate, strategies  # noqa: E402


def test_experience_table_starts_empty():
    table = learner.ExperienceTable(seed=1)
    assert table.situations_seen() == 0


def test_training_populates_the_table():
    table = learner.ExperienceTable(epsilon=0.3, seed=1)
    learner.train(table, num_turns=500, seed=1)
    assert table.situations_seen() > 0


def test_training_is_reproducible_with_same_seed():
    table_a = learner.ExperienceTable(epsilon=0.2, seed=1)
    learner.train(table_a, num_turns=300, seed=1)

    table_b = learner.ExperienceTable(epsilon=0.2, seed=1)
    learner.train(table_b, num_turns=300, seed=1)

    assert table_a.values == table_b.values


def test_choose_action_without_exploration_is_deterministic():
    table = learner.ExperienceTable(epsilon=0.2, seed=1)
    learner.train(table, num_turns=2000, seed=1)
    state = engine.build_state(turn_score=300, dice_remaining=3,
                                total_score=0, target_score=4000,
                                opponent_score=None)
    first = table.choose_action(state, explore=False)
    second = table.choose_action(state, explore=False)
    assert first == second
    assert first in ("roll", "bank")


def test_learner_prefers_banking_at_very_high_turn_scores():
    # With enough training, banking a very large turn score (little to
    # gain, a lot to lose) should look at least as good as rolling again.
    table = learner.ExperienceTable(epsilon=0.3, seed=2, bucket_size=50)
    learner.train(table, num_turns=30000, seed=2)
    high_state = engine.build_state(turn_score=950, dice_remaining=1,
                                     total_score=0, target_score=4000,
                                     opponent_score=None)
    key = table._state_key(high_state)  # noqa: SLF001 (test inspects internals on purpose)
    bank_avg = table._average(key, "bank")  # noqa: SLF001
    roll_avg = table._average(key, "roll")  # noqa: SLF001
    assert bank_avg >= roll_avg


def test_table_save_and_load_round_trip():
    table = learner.ExperienceTable(epsilon=0.2, seed=1)
    learner.train(table, num_turns=1000, seed=1)
    with tempfile.TemporaryDirectory() as tmp_dir:
        path = str(Path(tmp_dir) / "table.json")
        table.save(path)
        loaded = learner.load_table(path)
    assert loaded.values == table.values
    assert loaded.epsilon == table.epsilon


def test_table_rows_have_expected_shape():
    table = learner.ExperienceTable(epsilon=0.2, seed=1)
    learner.train(table, num_turns=500, seed=1)
    rows = table.table_rows()
    assert len(rows) > 0
    for row in rows:
        assert set(row.keys()) == {
            "turn_score_bucket", "dice_remaining", "roll_average",
            "roll_seen", "bank_average", "bank_seen", "current_preference",
        }
        assert row["current_preference"] in ("roll", "bank")


def test_as_strategy_plays_a_full_turn():
    table = learner.ExperienceTable(epsilon=0.2, seed=1)
    learner.train(table, num_turns=1000, seed=1)
    learned_strategy = table.as_strategy()
    rng = random.Random(99)
    points = engine.take_turn(rng, learned_strategy, total_score=0)
    assert points >= 0


def test_run_many_games_end_to_end_and_reproducible():
    strategy_a = strategies.BUILT_IN_STRATEGIES["bank_at_300"]
    strategy_b = strategies.BUILT_IN_STRATEGIES["bank_at_800"]
    summary_a = simulate.run_many_games(strategy_a, strategy_b, num_games=200, seed=5)
    summary_b = simulate.run_many_games(strategy_a, strategy_b, num_games=200, seed=5)
    assert summary_a == summary_b
    assert summary_a["num_games"] == 200
    assert 0.0 <= summary_a["win_rate_a"] <= 1.0
    assert 0.0 <= summary_a["win_rate_b"] <= 1.0
    assert summary_a["win_rate_a"] + summary_a["win_rate_b"] + summary_a["tie_rate"] == 1.0


def test_format_comparison_is_readable_text():
    strategy_a = strategies.BUILT_IN_STRATEGIES["bank_at_300"]
    strategy_b = strategies.BUILT_IN_STRATEGIES["bank_at_800"]
    summary = simulate.run_many_games(strategy_a, strategy_b, num_games=50, seed=1)
    report = simulate.format_comparison(summary)
    assert "bank_at_300" in report
    assert "bank_at_800" in report
    assert "win rate" in report
