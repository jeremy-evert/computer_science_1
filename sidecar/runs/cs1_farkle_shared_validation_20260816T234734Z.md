# CS1 Week 16 shared Farkle validation receipt

- UTC: 20260816T234734Z
- status: **GREEN**
- Python: 3.12.3
- shared repository: `jeremy-evert/Farkle_and_Machine_Learning`
- shared source commit: `d3a1ed379a652731b0b6237c33b4fe42c518ac9e`
- shared repo head at sync: `13f64b4bca1208e9a2f4e9835c2515d3937c2ea7`

## Contract checks

- GREEN — shared provenance manifest: repository=jeremy-evert/Farkle_and_Machine_Learning; source=src/farkle_ml; source commit=d3a1ed379a652731b0b6237c33b4fe42c518ac9e
- GREEN — no duplicated computational modules in CS1 facade: none
- GREEN — CS1 facade resolves canonical modules: engine/learner/simulate/strategies are canonical module objects
- GREEN — regression tests: exit=0
- GREEN — threshold comparison smoke: exit=0
- GREEN — learner comparison smoke: exit=0

## Migration interpretation

This receipt compares the migrated CS1 path against the same regression
suite and bounded CLI behaviors used for the pre-migration April baseline.
The CS1 lesson/CLI remain course-owned; the computational modules are
provided by the provenance-pinned canonical shared package.

## regression tests

Command: `/usr/bin/python3 -m pytest tests/test_farkle_engine.py tests/test_farkle_learner.py -v`
Exit: `0`

```text
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.0.3, pluggy-1.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase(PosixPath('/home/jevert/git/computer_science_1_farkle/.hypothesis/examples'))
rootdir: /home/jevert/git/computer_science_1_farkle
plugins: anyio-4.14.1, hypothesis-6.98.15
collecting ... collected 32 items

tests/test_farkle_engine.py::test_single_one_scores_100 PASSED           [  3%]
tests/test_farkle_engine.py::test_single_five_scores_50 PASSED           [  6%]
tests/test_farkle_engine.py::test_no_scoring_dice_is_farkle PASSED       [  9%]
tests/test_farkle_engine.py::test_three_of_a_kind_non_one PASSED         [ 12%]
tests/test_farkle_engine.py::test_three_ones_scores_1000 PASSED          [ 15%]
tests/test_farkle_engine.py::test_four_of_a_kind_doubles_three_of_a_kind PASSED [ 18%]
tests/test_farkle_engine.py::test_five_of_a_kind_quadruples_three_of_a_kind PASSED [ 21%]
tests/test_farkle_engine.py::test_six_of_a_kind_octuples_three_of_a_kind PASSED [ 25%]
tests/test_farkle_engine.py::test_triple_plus_leftover_singles PASSED    [ 28%]
tests/test_farkle_engine.py::test_all_non_scoring_dice_never_used PASSED [ 31%]
tests/test_farkle_engine.py::test_roll_dice_is_reproducible_with_same_seed PASSED [ 34%]
tests/test_farkle_engine.py::test_roll_dice_returns_requested_count_in_range PASSED [ 37%]
tests/test_farkle_engine.py::test_take_turn_never_returns_negative PASSED [ 40%]
tests/test_farkle_engine.py::test_take_turn_bank_immediately_after_first_score PASSED [ 43%]
tests/test_farkle_engine.py::test_take_turn_is_reproducible_with_same_seed PASSED [ 46%]
tests/test_farkle_engine.py::test_take_turn_trace_records_every_roll PASSED [ 50%]
tests/test_farkle_engine.py::test_build_state_has_expected_keys PASSED   [ 53%]
tests/test_farkle_learner.py::test_experience_table_starts_empty PASSED  [ 56%]
tests/test_farkle_learner.py::test_training_populates_the_table PASSED   [ 59%]
tests/test_farkle_learner.py::test_training_is_reproducible_with_same_seed PASSED [ 62%]
tests/test_farkle_learner.py::test_choose_action_without_exploration_is_deterministic PASSED [ 65%]
tests/test_farkle_learner.py::test_learner_prefers_banking_at_very_high_turn_scores PASSED [ 68%]
tests/test_farkle_learner.py::test_table_save_and_load_round_trip PASSED [ 71%]
tests/test_farkle_learner.py::test_table_rows_have_expected_shape PASSED [ 75%]
tests/test_farkle_learner.py::test_table_row_preference_matches_actual_greedy_policy_with_sparse_evidence PASSED [ 78%]
tests/test_farkle_learner.py::test_as_strategy_plays_a_full_turn PASSED  [ 81%]
tests/test_farkle_learner.py::test_custom_threshold_strategy_is_supported PASSED [ 84%]
tests/test_farkle_learner.py::test_invalid_custom_threshold_is_rejected PASSED [ 87%]
tests/test_farkle_learner.py::test_run_many_games_end_to_end_balanced_and_reproducible PASSED [ 90%]
tests/test_farkle_learner.py::test_farkle_rate_uses_each_players_own_turns PASSED [ 93%]
tests/test_farkle_learner.py::test_play_game_tracks_player_turns PASSED  [ 96%]
tests/test_farkle_learner.py::test_format_comparison_is_readable_text PASSED [100%]

============================== 32 passed in 0.21s ==============================
```

## threshold comparison smoke

Command: `/usr/bin/python3 -m farkle.cli compare --games 50 --seed 17 --strategy-a bank_at_300 --strategy-b bank_at_425`
Exit: `0`

```text
50 games, seed=17 (starts A/B=25/25)
  bank_at_300                  wins    34 win rate 68.0% avg score 3762 farkle/own-turn 21.2%
  bank_at_425                  wins    16 win rate 32.0% avg score 3229 farkle/own-turn 51.5%
  ties 0 (0.0%) avg turns/game 18.3
```

## learner comparison smoke

Command: `/usr/bin/python3 -m farkle.cli learn-vs-baseline --turns 500 --games 50 --seed 17 --baseline bank_at_425`
Exit: `0`

```text
Step 1: trained the experience table on 500 solo turns (seed=17).
        68 (situation, action) pairs now have data.

Step 2: comparing the learned strategy to baseline 'bank_at_425' over 50 FRESH games (none of these games were used in training).

50 games, seed=18 (starts A/B=25/25)
  learned_experience_table     wins    34 win rate 68.0% avg score 3957 farkle/own-turn 8.7%
  bank_at_425                  wins    16 win rate 32.0% avg score 3178 farkle/own-turn 50.1%
  ties 0 (0.0%) avg turns/game 18.7
```
