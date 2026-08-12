"""engine.py -- dice, scoring, and one turn of our Farkle variant.

Our rules (documented here, and in lessons/10-farkle-ml.md, in the same
words -- read either one first):

- Six dice, standard six-sided.
- A single 1 scores 100 points. A single 5 scores 50 points.
- Three of a kind scores more: three 1s = 1000; three of any other
  value V scores V * 100 (three 2s = 200, three 6s = 600, and so on).
- Four, five, or six of the same value DOUBLES the three-of-a-kind score
  for each extra matching die (four of a kind = 2x, five of a kind = 4x,
  six of a kind = 8x the three-of-a-kind value). This is one common
  classroom Farkle variant; we picked it because it is a single clear
  rule to implement, test, and explain -- other tables you might find
  online use a flat lookup instead, and that is a fine variant too, just
  not the one this course uses.
- Straights (1-2-3-4-5-6) and three-pairs bonuses are NOT used in our
  variant. Real-world Farkle house rules disagree about these enough
  that leaving them out keeps the scoring function small enough for a
  CS1 student to read start to finish and hand-trace on paper.
- If a roll has NO scoring dice at all, that is a "Farkle": the turn
  ends immediately and every point banked *this turn* (but not already
  banked in earlier turns) is lost.
- "Hot dice": if every one of the dice you just rolled scored, you get
  to roll all six dice again on your next roll, keeping your turn score
  so far. This is the game's built-in reward for a great roll.
- Dice selection is automatic: whichever dice score on a given roll are
  always kept (there is no "hold back a scoring die" choice in this
  variant). The only decision a player or a strategy makes is: after
  seeing your running turn score, do you ROLL again or BANK it?
- Winning score: first player to reach or pass 4000 total points wins
  the game. (Real Farkle is often played to 10,000; we use a smaller
  target so a classroom simulation of thousands of games finishes fast.)

That last paragraph is the whole game, from a decision-making point of
view: you always have a running turn score you could lose, and a choice
between "cash it in" (BANK) and "go for more" (ROLL). Everything in this
package is about exploring that one choice.
"""

DEFAULT_TARGET_SCORE = 4000
NUM_DICE = 6


def roll_dice(count, rng):
    """Roll `count` six-sided dice using the given random number generator.

    Passing in `rng` (instead of using the global `random` module) is what
    makes every simulation in this package reproducible: the same seed
    always produces the same sequence of rolls.
    """
    dice = []
    for _ in range(count):
        dice.append(rng.randint(1, 6))
    return dice


def score_roll(dice):
    """Score one roll under our Farkle variant.

    Returns (points, dice_used) where dice_used is how many of the dice
    in `dice` contributed to the score. A roll with no scoring dice at
    all returns (0, 0) -- that is a Farkle.
    """
    counts = {}
    for value in range(1, 7):
        counts[value] = dice.count(value)

    points = 0
    dice_used = 0

    for value in range(1, 7):
        count = counts[value]
        if count >= 3:
            base = 1000 if value == 1 else value * 100
            extra_dice = count - 3
            points += base * (2 ** extra_dice)
            dice_used += count
            counts[value] = 0

    # Leftover single 1s and 5s still score individually.
    points += counts[1] * 100
    dice_used += counts[1]
    points += counts[5] * 50
    dice_used += counts[5]

    return points, dice_used


def is_farkle(points):
    return points == 0


def build_state(turn_score, dice_remaining, total_score, target_score,
                 opponent_score):
    """Build the dictionary that describes the current decision point.

    This dictionary IS the "state" in machine-learning language: it is
    everything a strategy is allowed to look at before deciding ROLL or
    BANK. Print one of these out during a demo -- it is not a black box.
    """
    return {
        "turn_score": turn_score,
        "dice_remaining": dice_remaining,
        "total_score": total_score,
        "target_score": target_score,
        "opponent_score": opponent_score,
    }


def take_turn(rng, strategy, total_score, target_score=DEFAULT_TARGET_SCORE,
              opponent_score=None, trace=None):
    """Play one full turn and return the points banked (0 if farkled).

    `strategy` is any function that takes a state dictionary (see
    build_state) and returns the string "roll" or "bank".

    If `trace` is a list, this function appends a short text line to it
    for every roll and decision, so a demo can print exactly what
    happened -- see cli.py's `play` command.
    """
    dice_remaining = NUM_DICE
    turn_score = 0

    while True:
        dice = roll_dice(dice_remaining, rng)
        points, used = score_roll(dice)

        if trace is not None:
            trace.append(f"  rolled {dice} -> scores {points} points "
                         f"using {used} of the dice")

        if is_farkle(points):
            if trace is not None:
                trace.append(f"  FARKLE -- turn ends, {turn_score} points lost")
            return 0

        turn_score += points
        dice_remaining -= used
        if dice_remaining == 0:
            dice_remaining = NUM_DICE
            if trace is not None:
                trace.append("  hot dice! rolling all 6 again")

        state = build_state(turn_score, dice_remaining, total_score,
                             target_score, opponent_score)
        action = strategy(state)

        if trace is not None:
            trace.append(f"  turn score now {turn_score}, "
                         f"{dice_remaining} dice left -> strategy says {action.upper()}")

        if action == "bank":
            return turn_score
        # action == "roll": loop and roll again
