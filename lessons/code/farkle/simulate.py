"""simulate.py -- run many turns and games, and summarize the results.

Everything here is "evidence generation": play the game a lot of times
under controlled conditions (a fixed seed, or a range of seeds) and boil
the results down into numbers a person can reason about -- win rate,
average score, how often a strategy farkles. No inferential statistics
required; the point is closer to "did I run enough games that a few
lucky rolls can't explain the whole difference," which the lesson asks
students to reason about directly.
"""

import random

from . import engine

DEFAULT_MAX_TURNS = 400


def play_game(rng, strategy_a, strategy_b, target_score=engine.DEFAULT_TARGET_SCORE,
              max_turns=DEFAULT_MAX_TURNS):
    """Play one two-player game to the target score and return a summary.

    Players alternate turns starting with strategy_a. The first player to
    reach or pass target_score at the end of their own turn wins
    immediately -- our variant does not give the trailing player a bonus
    "final round" the way some house rules do. That is a documented
    simplification, not an oversight: it keeps a game's winner fully
    decided by the moment target_score is reached, which is easier for a
    CS1 student to trace by hand.
    """
    scores = [0, 0]
    farkles = [0, 0]
    turns_played = 0
    strategies = [strategy_a, strategy_b]

    while turns_played < max_turns:
        current_player = turns_played % 2
        opponent_player = 1 - current_player
        points = engine.take_turn(
            rng,
            strategies[current_player],
            total_score=scores[current_player],
            target_score=target_score,
            opponent_score=scores[opponent_player],
        )
        if points == 0:
            farkles[current_player] += 1
        scores[current_player] += points
        turns_played += 1
        if scores[current_player] >= target_score:
            break

    if scores[0] > scores[1]:
        winner = 0
    elif scores[1] > scores[0]:
        winner = 1
    else:
        winner = None

    return {
        "scores": scores,
        "farkles": farkles,
        "turns_played": turns_played,
        "winner": winner,
    }


def run_many_games(strategy_a, strategy_b, num_games, seed,
                    target_score=engine.DEFAULT_TARGET_SCORE):
    """Play `num_games` games between two strategies and summarize results.

    Uses one random.Random seeded with `seed`, advanced across every
    game in sequence -- so the exact same `seed` always reproduces the
    exact same sequence of games, but the games are not identical to
    each other (this is deliberate: real evidence needs many different
    situations, not one situation repeated).
    """
    rng = random.Random(seed)
    wins = [0, 0]
    ties = 0
    total_scores = [0, 0]
    total_farkles = [0, 0]
    total_turns = 0

    for _ in range(num_games):
        result = play_game(rng, strategy_a, strategy_b, target_score=target_score)
        if result["winner"] == 0:
            wins[0] += 1
        elif result["winner"] == 1:
            wins[1] += 1
        else:
            ties += 1
        total_scores[0] += result["scores"][0]
        total_scores[1] += result["scores"][1]
        total_farkles[0] += result["farkles"][0]
        total_farkles[1] += result["farkles"][1]
        total_turns += result["turns_played"]

    name_a = getattr(strategy_a, "__name__", "strategy_a")
    name_b = getattr(strategy_b, "__name__", "strategy_b")

    return {
        "num_games": num_games,
        "seed": seed,
        "strategy_a": name_a,
        "strategy_b": name_b,
        "win_rate_a": wins[0] / num_games,
        "win_rate_b": wins[1] / num_games,
        "tie_rate": ties / num_games,
        "avg_score_a": total_scores[0] / num_games,
        "avg_score_b": total_scores[1] / num_games,
        "avg_turns_per_game": total_turns / num_games,
        "farkle_rate_a": total_farkles[0] / total_turns if total_turns else 0.0,
        "farkle_rate_b": total_farkles[1] / total_turns if total_turns else 0.0,
    }


def format_comparison(summary):
    """Turn a run_many_games summary dict into a short, readable report."""
    lines = [
        f"{summary['num_games']} games, seed={summary['seed']}",
        f"  {summary['strategy_a']:<28} win rate {summary['win_rate_a']:.1%}"
        f"   avg score {summary['avg_score_a']:.0f}"
        f"   farkle rate {summary['farkle_rate_a']:.1%}",
        f"  {summary['strategy_b']:<28} win rate {summary['win_rate_b']:.1%}"
        f"   avg score {summary['avg_score_b']:.0f}"
        f"   farkle rate {summary['farkle_rate_b']:.1%}",
        f"  ties: {summary['tie_rate']:.1%}"
        f"   avg turns/game: {summary['avg_turns_per_game']:.1f}",
    ]
    return "\n".join(lines)
