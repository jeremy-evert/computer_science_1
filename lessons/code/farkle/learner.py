"""learner.py -- a small, transparent "experience table" for Farkle.

What this IS: a dictionary. That's the whole trick.

The key is (a bucketed turn score, dice remaining, action) -- one entry
per situation the learner has seen, per choice it could make there. The
value is a running average of "how did it turn out, the times I tried
this?" After every training turn, we update that average using the
turn's actual result.

  average = average + (new_result - average) / times_seen

That line is the entire "learning rule." No gradient, no neural network,
no Bellman equation, no discount factor gamma. It is the same idea as
keeping a running batting average: every at-bat nudges the average a
little toward the most recent result, and the more times you've seen a
situation, the less any single new result moves the average.

What this is NOT: real-world reinforcement learning (the kind used in
game-playing AI, robotics, etc.) is usually more sophisticated than this
-- it credits each decision separately for how it changed the *future*,
using ideas like discounted future reward and temporal-difference
updates. We deliberately do not do that here. Instead, every decision
made during a turn shares the SAME credit or blame: the turn's final
result. If you rolled three times and then farkled, all three of those
"roll" decisions get blamed equally for the loss. If you rolled twice and
then banked successfully, both "roll" decisions and the "bank" decision
get credit for the win. This is easier to explain out loud than proper
per-step credit assignment, and it is still real learning from data --
just a simplified version. See docs/curriculum/cs2-farkle-ml-handoff.md
for what a more sophisticated version would add.

How a decision gets made: with probability `epsilon`, the learner tries
something at random instead of following the table (this is called
"exploration" -- without it, the learner could get permanently stuck
avoiding a good option it happened to try once and do poorly with, just
from bad luck). The rest of the time, it looks up its table and picks
whichever action ("roll" or "bank") has the better running average so
far (this is "exploitation" -- using what it already believes). A
typical `epsilon` like 0.2 means: about 1 time in 5, try something
random and see what happens; the other 4 times, go with the best-known
choice.
"""

import json
import random


class ExperienceTable:
    """A transparent, table-based Farkle learner.

    Attributes:
        values: dict mapping (state_key, action) -> [running_average, count]
        epsilon: probability of trying a random action instead of the
            table's current favorite (exploration rate)
        bucket_size: how coarsely turn_score is grouped (smaller = more
            situations to learn, more data needed per situation)
    """

    def __init__(self, epsilon=0.2, bucket_size=50, seed=None):
        self.values = {}
        self.epsilon = epsilon
        self.bucket_size = bucket_size
        self.rng = random.Random(seed)

    def _state_key(self, state):
        """Turn a full state dictionary into the small key our table uses.

        We deliberately only look at turn_score and dice_remaining -- the
        two things the historical Farkle/Q-learning assignment this
        exercise is descended from used as the minimum state. Ignoring
        total_score/opponent_score keeps the table small enough to print
        and read in full (see cli.py's `train --show-table` command).
        """
        bucketed_turn_score = min(state["turn_score"] // self.bucket_size, 20) * self.bucket_size
        return (bucketed_turn_score, state["dice_remaining"])

    def _average(self, state_key, action):
        return self.values.get((state_key, action), [0.0, 0])[0]

    def choose_action(self, state, explore=True):
        """Pick "roll" or "bank" for this state.

        With `explore=True` (used during training), occasionally picks a
        random action so the table gets data on both choices. With
        `explore=False` (used once training is done), always picks
        whichever action currently has the higher average -- this is
        "playing what I've learned."
        """
        if explore and self.rng.random() < self.epsilon:
            return self.rng.choice(["roll", "bank"])

        state_key = self._state_key(state)
        roll_average = self._average(state_key, "roll")
        bank_average = self._average(state_key, "bank")
        return "bank" if bank_average >= roll_average else "roll"

    def update(self, state, action, outcome):
        """Fold one new result into the running average for (state, action)."""
        key = (self._state_key(state), action)
        average, count = self.values.get(key, [0.0, 0])
        count += 1
        average += (outcome - average) / count
        self.values[key] = [average, count]

    def as_strategy(self):
        """Wrap this learner as a strategy function, for use with
        engine.take_turn / simulate.py, exactly like a hand-written
        strategy from strategies.py. Uses explore=False: once training
        is over, the learner plays its best-known move every time.
        """
        def learned_strategy(state):
            return self.choose_action(state, explore=False)

        learned_strategy.description = "Whatever the experience table currently believes is best."
        return learned_strategy

    def situations_seen(self):
        """How many distinct (state, action) pairs have at least one data point."""
        return len(self.values)

    def table_rows(self):
        """Return the table as a sorted list of readable rows, one per
        (turn_score bucket, dice remaining) situation, for printing or
        for a student to inspect by hand."""
        state_keys = []
        for key in self.values.keys():
            state_key, action = key
            if state_key not in state_keys:
                state_keys.append(state_key)
        state_keys.sort()
        rows = []
        for state_key in state_keys:
            turn_score_bucket, dice_remaining = state_key
            roll_avg, roll_n = self.values.get((state_key, "roll"), [0.0, 0])
            bank_avg, bank_n = self.values.get((state_key, "bank"), [0.0, 0])
            preferred = "bank" if bank_avg >= roll_avg and bank_n > 0 else "roll"
            rows.append({
                "turn_score_bucket": turn_score_bucket,
                "dice_remaining": dice_remaining,
                "roll_average": round(roll_avg, 1),
                "roll_seen": roll_n,
                "bank_average": round(bank_avg, 1),
                "bank_seen": bank_n,
                "current_preference": preferred,
            })
        return rows

    def save(self, path):
        """Save the table to a small, human-readable JSON file."""
        serializable = {}
        for key, value in self.values.items():
            state_key, action = key
            turn_score_bucket, dice_remaining = state_key
            text_key = f"{turn_score_bucket}|{dice_remaining}|{action}"
            serializable[text_key] = value

        with open(path, "w", encoding="utf-8") as handle:
            json.dump({
                "epsilon": self.epsilon,
                "bucket_size": self.bucket_size,
                "values": serializable,
            }, handle, indent=2, sort_keys=True)


def load_table(path):
    """Load a table previously saved with ExperienceTable.save(path)."""
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)

    table = ExperienceTable(epsilon=data["epsilon"], bucket_size=data["bucket_size"])
    for key_str, value in data["values"].items():
        turn_score_bucket, dice_remaining, action = key_str.split("|")
        key = ((int(turn_score_bucket), int(dice_remaining)), action)
        table.values[key] = value
    return table


def train_one_turn(rng, table):
    """Play one solo training turn, letting the table make every ROLL/BANK
    decision (with exploration on), and update the table with the result.

    Returns the points banked (0 if the turn farkled). This function is
    intentionally similar to engine.take_turn, but it also records every
    (state, action) pair visited so it can update the table once the
    turn's final outcome is known -- see the module docstring above for
    why every decision in a turn shares that one final outcome.
    """
    from . import engine

    dice_remaining = engine.NUM_DICE
    turn_score = 0
    visited = []

    while True:
        dice = engine.roll_dice(dice_remaining, rng)
        points, used = engine.score_roll(dice)

        if engine.is_farkle(points):
            outcome = -turn_score
            for state, action in visited:
                table.update(state, action, outcome)
            return 0

        turn_score += points
        dice_remaining -= used
        if dice_remaining == 0:
            dice_remaining = engine.NUM_DICE

        state = engine.build_state(turn_score, dice_remaining,
                                    total_score=0, target_score=0,
                                    opponent_score=None)
        action = table.choose_action(state, explore=True)
        visited.append((state, action))

        if action == "bank":
            outcome = turn_score
            for visited_state, visited_action in visited:
                table.update(visited_state, visited_action, outcome)
            return turn_score
        # action == "roll": loop and roll again


def train(table, num_turns, seed):
    """Train `table` for `num_turns` solo turns using the given seed."""
    rng = random.Random(seed)
    for _ in range(num_turns):
        train_one_turn(rng, table)
