"""cli.py -- the runnable CS1 Week 16 Farkle experiment.

The student-facing command remains ``python3 -m farkle.cli ...`` while the
computational engine, strategies, learner, and simulation come from the
provenance-pinned canonical ``farkle_ml`` package.

Strategy arguments accept the named built-ins or a custom positive threshold
such as ``bank_at_425``. Every command remains seed-driven and reproducible.
"""

import argparse
import random
import sys

from farkle_ml import engine, learner, simulate, strategies


def _strategy(name):
    try:
        return strategies.resolve_strategy(name)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc


def cmd_play(args):
    rng = random.Random(args.seed)
    strategy = _strategy(args.strategy)
    print(
        f"Playing one turn with strategy '{strategy.__name__}' "
        f"({strategy.description}), seed={args.seed}"
    )
    trace = []
    points = engine.take_turn(rng, strategy, total_score=0, trace=trace)
    for line in trace:
        print(line)
    print(f"Turn result: {points} points banked")


def cmd_compare(args):
    strategy_a = _strategy(args.strategy_a)
    strategy_b = _strategy(args.strategy_b)
    summary = simulate.run_many_games(
        strategy_a, strategy_b, args.games, args.seed
    )
    print(simulate.format_comparison(summary))


def cmd_train(args):
    table = learner.ExperienceTable(epsilon=args.epsilon, seed=args.seed)
    learner.train(table, args.turns, seed=args.seed)
    print(
        f"Trained on {args.turns} solo turns (seed={args.seed}, "
        f"epsilon={args.epsilon})."
    )
    print(
        f"The table has learned about {table.situations_seen()} "
        f"(situation, action) pairs."
    )
    if args.save:
        table.save(args.save)
        print(f"Saved table to {args.save}")
    if args.show_table:
        print()
        print(
            f"{'turn score':>10} {'dice left':>9} {'roll avg (n)':>16} "
            f"{'bank avg (n)':>16}  prefers"
        )
        for row in table.table_rows():
            roll_cell = f"{row['roll_average']:.0f} ({row['roll_seen']})"
            bank_cell = f"{row['bank_average']:.0f} ({row['bank_seen']})"
            print(
                f"{row['turn_score_bucket']:>10} {row['dice_remaining']:>9} "
                f"{roll_cell:>16} {bank_cell:>16}  {row['current_preference']}"
            )


def cmd_learn_vs_baseline(args):
    table = learner.ExperienceTable(epsilon=args.epsilon, seed=args.seed)
    learner.train(table, args.turns, seed=args.seed)
    learned_strategy = table.as_strategy()
    baseline = _strategy(args.baseline)

    print(
        f"Step 1: trained the experience table on {args.turns} solo turns "
        f"(seed={args.seed})."
    )
    print(
        f"        {table.situations_seen()} (situation, action) pairs now have data.\n"
    )
    print(
        f"Step 2: comparing the learned strategy to baseline "
        f"'{baseline.__name__}' over {args.games} FRESH games "
        f"(none of these games were used in training).\n"
    )

    eval_seed = args.seed + 1
    summary = simulate.run_many_games(
        learned_strategy, baseline, args.games, eval_seed
    )
    print(simulate.format_comparison(summary))


def _add_strategy_help(parser, flag, default, help_text):
    parser.add_argument(
        flag,
        default=default,
        help=(
            help_text
            + " Use a named strategy or bank_at_N, e.g. bank_at_425."
        ),
    )


def build_parser():
    parser = argparse.ArgumentParser(
        description="CS1 Week 16 Farkle / machine-learning experiment runner."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    play_parser = subparsers.add_parser("play", help="Play and print one turn.")
    play_parser.add_argument("--seed", type=int, default=1)
    _add_strategy_help(
        play_parser, "--strategy", "bank_at_300", "Strategy to play."
    )
    play_parser.set_defaults(func=cmd_play)

    compare_parser = subparsers.add_parser(
        "compare", help="Compare two strategies over many balanced games."
    )
    compare_parser.add_argument("--seed", type=int, default=1)
    compare_parser.add_argument("--games", type=int, default=1000)
    _add_strategy_help(
        compare_parser, "--strategy-a", "bank_at_300", "First strategy."
    )
    _add_strategy_help(
        compare_parser, "--strategy-b", "bank_at_800", "Second strategy."
    )
    compare_parser.set_defaults(func=cmd_compare)

    train_parser = subparsers.add_parser(
        "train", help="Train the experience-table learner and inspect it."
    )
    train_parser.add_argument("--seed", type=int, default=1)
    train_parser.add_argument("--turns", type=int, default=20000)
    train_parser.add_argument("--epsilon", type=float, default=0.2)
    train_parser.add_argument("--show-table", action="store_true")
    train_parser.add_argument(
        "--save", type=str, default=None,
        help="Path to save the trained table as JSON."
    )
    train_parser.set_defaults(func=cmd_train)

    lvb_parser = subparsers.add_parser(
        "learn-vs-baseline",
        help="Train a learner, then compare it to a baseline over fresh games.",
    )
    lvb_parser.add_argument("--seed", type=int, default=1)
    lvb_parser.add_argument("--turns", type=int, default=20000)
    lvb_parser.add_argument("--epsilon", type=float, default=0.2)
    lvb_parser.add_argument("--games", type=int, default=2000)
    _add_strategy_help(
        lvb_parser, "--baseline", "bank_at_300", "Baseline strategy."
    )
    lvb_parser.set_defaults(func=cmd_learn_vs_baseline)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main(sys.argv[1:])
