"""Tests for the Farkle learner and experiment evidence contract."""

import random
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lessons" / "code"))

from farkle import engine, learner, simulate, strategies  # noqa: E402


def test_experience_table_starts_empty():
    assert learner.ExperienceTable(seed=1).situations_seen() == 0


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
    state = engine.build_state(300, 3, 0, 4000, None)
    assert table.choose_action(state, explore=False) == table.choose_action(
        state, explore=False
    )


def test_learner_prefers_banking_at_very_high_turn_scores():
    table = learner.ExperienceTable(epsilon=0.3, seed=2, bucket_size=50)
    learner.train(table, num_turns=30000, seed=2)
    high_state = engine.build_state(950, 1, 0, 4000, None)
    key = table._state_key(high_state)  # noqa: SLF001
    assert table._average(key, "bank") >= table._average(key, "roll")  # noqa: SLF001


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
    assert rows
    for row in rows:
        assert set(row) == {
            "turn_score_bucket", "dice_remaining", "roll_average",
            "roll_seen", "bank_average", "bank_seen", "current_preference",
        }
        assert row["current_preference"] in ("roll", "bank")


def test_table_row_preference_matches_actual_greedy_policy_with_sparse_evidence():
    table = learner.ExperienceTable(seed=1)
    state = engine.build_state(300, 3, 0, 4000, None)
    key = table._state_key(state)  # noqa: SLF001
    table.values[(key, "roll")] = [-100.0, 1]
    row = table.table_rows()[0]
    assert row["current_preference"] == "bank"
    assert table.choose_action(state, explore=False) == "bank"


def test_as_strategy_plays_a_full_turn():
    table = learner.ExperienceTable(epsilon=0.2, seed=1)
    learner.train(table, num_turns=1000, seed=1)
    points = engine.take_turn(random.Random(99), table.as_strategy(), total_score=0)
    assert points >= 0


def test_custom_threshold_strategy_is_supported():
    strategy = strategies.resolve_strategy("bank_at_425")
    low = engine.build_state(400, 3, 0, 4000, None)
    high = engine.build_state(450, 3, 0, 4000, None)
    assert strategy(low) == "roll"
    assert strategy(high) == "bank"
    assert strategy.__name__ == "bank_at_425"


def test_invalid_custom_threshold_is_rejected():
    for name in ("bank_at_zero", "bank_at_0", "bank_at_-5", "unknown"):
        try:
            strategies.resolve_strategy(name)
        except ValueError:
            pass
        else:
            raise AssertionError(f"{name} should have been rejected")


def test_run_many_games_end_to_end_balanced_and_reproducible():
    strategy_a = strategies.BUILT_IN_STRATEGIES["bank_at_300"]
    strategy_b = strategies.BUILT_IN_STRATEGIES["bank_at_800"]
    summary_a = simulate.run_many_games(strategy_a, strategy_b, 200, 5)
    summary_b = simulate.run_many_games(strategy_a, strategy_b, 200, 5)
    assert summary_a == summary_b
    assert summary_a["starts_a"] == 100
    assert summary_a["starts_b"] == 100
    assert 0.0 <= summary_a["farkle_rate_a"] <= 1.0
    assert 0.0 <= summary_a["farkle_rate_b"] <= 1.0
    assert (
        summary_a["win_rate_a"]
        + summary_a["win_rate_b"]
        + summary_a["tie_rate"]
    ) == 1.0


def test_farkle_rate_uses_each_players_own_turns(monkeypatch):
    def fake_play_game(rng, strategy_a, strategy_b, target_score, starting_player):
        return {
            "scores": [4000, 3000],
            "farkles": [1, 4],
            "turns_by_player": [2, 8],
            "turns_played": 10,
            "starting_player": starting_player,
            "winner": 0,
        }

    monkeypatch.setattr(simulate, "play_game", fake_play_game)
    summary = simulate.run_many_games(lambda state: "bank", lambda state: "bank", 2, 1)
    assert summary["farkle_rate_a"] == 0.5
    assert summary["farkle_rate_b"] == 0.5


def test_play_game_tracks_player_turns():
    result = simulate.play_game(
        random.Random(4),
        strategies.bank_at_300,
        strategies.bank_at_500,
        starting_player=1,
    )
    assert sum(result["turns_by_player"]) == result["turns_played"]
    assert result["starting_player"] == 1


def test_format_comparison_is_readable_text():
    summary = simulate.run_many_games(
        strategies.bank_at_300, strategies.bank_at_800, 50, 1
    )
    report = simulate.format_comparison(summary)
    assert "bank_at_300" in report
    assert "bank_at_800" in report
    assert "starts A/B=" in report
    assert "farkle/own-turn" in report
