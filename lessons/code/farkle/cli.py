"""cli.py -- the runnable Week 16 experiment.

Usage (from computer_science_1/lessons/code/):

    python3 -m farkle.cli play --seed 1
    python3 -m farkle.cli compare --seed 1 --games 2000
    python3 -m farkle.cli train --seed 1 --turns 20000 --show-table
    python3 -m farkle.cli learn-vs-baseline --seed 1 --turns 20000 --games 2000

Every command takes --seed so results are reproducible. Run the same
command with the same seed twice and you will get identical numbers --
that is what "deterministic" means and why it matters for trusting a demo.

You are not expected to read this file closely -- it is command-line
plumbing (argparse), not part of this week's ideas. Read engine.py,
strategies.py, and learner.py instead; this file just wires them
together so you can run experiments from the terminal.
"""

import argparse
import random
import sys

from . import engine, learner, simulate, strategies


def cmd_play(args):
    """Play and print one full turn, showing every roll and decision."""
    rng = random.Random(args.seed)
    strategy = strategies.BUILT_IN_STRATEGIES[args.strategy]
    print(f"Playing one turn with strategy '{args.strategy}' "
          f"({strategy.description}), seed={args.seed}")
    trace = []
    points = engine.take_turn(rng, strategy, total_score=0, trace=trace)
    for line in trace:
        print(line)
    print(f"Turn result: {points} points banked")


def cmd_compare(args):
    """Compare two built-in strategies over many games."""
    strategy_a = strategies.BUILT_IN_STRATEGIES[args.strategy_a]
    strategy_b = strategies.BUILT_IN_STRATEGIES[args.strategy_b]
    summary = simulate.run_many_games(strategy_a, strategy_b, args.games, args.seed)
    print(simulate.format_comparison(summary))


def cmd_train(args):
    """Train the experience-table learner and optionally show its table."""
    table = learner.ExperienceTable(epsilon=args.epsilon, seed=args.seed)
    learner.train(table, args.turns, seed=args.seed)
    print(f"Trained on {args.turns} solo turns (seed={args.seed}, "
          f"epsilon={args.epsilon}).")
    print(f"The table has learned about {table.situations_seen()} "
          f"(situation, action) pairs.")
    if args.save:
        table.save(args.save)
        print(f"Saved table to {args.save}")
    if args.show_table:
        print()
        print(f"{'turn score':>10} {'dice left':>9} {'roll avg (n)':>16} "
              f"{'bank avg (n)':>16}  prefers")
        for row in table.table_rows():
            roll_cell = f"{row['roll_average']:.0f} ({row['roll_seen']})"
            bank_cell = f"{row['bank_average']:.0f} ({row['bank_seen']})"
            print(f"{row['turn_score_bucket']:>10} {row['dice_remaining']:>9} "
                  f"{roll_cell:>16} {bank_cell:>16}  {row['current_preference']}")


def cmd_learn_vs_baseline(args):
    """The full Week 16 experiment: train a learner, then compare it to a
    baseline strategy over fresh games it never trained on."""
    table = learner.ExperienceTable(epsilon=args.epsilon, seed=args.seed)
    learner.train(table, args.turns, seed=args.seed)
    learned_strategy = table.as_strategy()

    baseline = strategies.BUILT_IN_STRATEGIES[args.baseline]

    print(f"Step 1: trained the experience table on {args.turns} solo turns "
          f"(seed={args.seed}).")
    print(f"        {table.situations_seen()} (situation, action) pairs now have data.\n")

    print(f"Step 2: comparing the learned strategy to baseline "
          f"'{args.baseline}' over {args.games} FRESH games "
          f"(none of these games were used in training).\n")

    # A different seed for evaluation than for training, so the comparison
    # is not accidentally reusing the exact dice sequence the table trained on.
    eval_seed = args.seed + 1
    summary = simulate.run_many_games(learned_strategy, baseline, args.games, eval_seed)
    print(simulate.format_comparison(summary))


def build_parser():
    parser = argparse.ArgumentParser(
        description="CS1 Week 16 Farkle / machine-learning experiment runner.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    play_parser = subparsers.add_parser("play", help="Play and print one turn.")
    play_parser.add_argument("--seed", type=int, default=1)
    play_parser.add_argument("--strategy", choices=strategies.BUILT_IN_STRATEGIES,
                              default="bank_at_300")
    play_parser.set_defaults(func=cmd_play)

    compare_parser = subparsers.add_parser(
        "compare", help="Compare two built-in strategies over many games.")
    compare_parser.add_argument("--seed", type=int, default=1)
    compare_parser.add_argument("--games", type=int, default=1000)
    compare_parser.add_argument("--strategy-a", choices=strategies.BUILT_IN_STRATEGIES,
                                 default="bank_at_300")
    compare_parser.add_argument("--strategy-b", choices=strategies.BUILT_IN_STRATEGIES,
                                 default="bank_at_800")
    compare_parser.set_defaults(func=cmd_compare)

    train_parser = subparsers.add_parser(
        "train", help="Train the experience-table learner and inspect it.")
    train_parser.add_argument("--seed", type=int, default=1)
    train_parser.add_argument("--turns", type=int, default=20000)
    train_parser.add_argument("--epsilon", type=float, default=0.2)
    train_parser.add_argument("--show-table", action="store_true")
    train_parser.add_argument("--save", type=str, default=None,
                               help="Path to save the trained table as JSON.")
    train_parser.set_defaults(func=cmd_train)

    lvb_parser = subparsers.add_parser(
        "learn-vs-baseline",
        help="Train a learner, then compare it to a baseline over fresh games.")
    lvb_parser.add_argument("--seed", type=int, default=1)
    lvb_parser.add_argument("--turns", type=int, default=20000)
    lvb_parser.add_argument("--epsilon", type=float, default=0.2)
    lvb_parser.add_argument("--games", type=int, default=2000)
    lvb_parser.add_argument("--baseline", choices=strategies.BUILT_IN_STRATEGIES,
                             default="bank_at_300")
    lvb_parser.set_defaults(func=cmd_learn_vs_baseline)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main(sys.argv[1:])
