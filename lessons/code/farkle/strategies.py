"""strategies.py -- human, rule-based Farkle strategies.

A "strategy" in this package is nothing fancy: it is a function that takes
a state dictionary (see engine.build_state) and returns "roll" or "bank".
That's it. Every strategy below is a plain-language rule turned directly
into an if-statement, on purpose -- so you can look at the Python and the
English sentence side by side. If you can read the first one, you can
read every strategy in this file, including the learned one in
learner.py -- these are all just functions with an if-statement inside.

These are the strategies students write BEFORE meeting the learner in
learner.py. The whole point of Week 16 is to compare a rule you invented
against a strategy a program built for itself out of experience.
"""


def bank_at_300(state):
    """Bank once my turn score reaches 300; otherwise keep rolling."""
    if state["turn_score"] >= 300:
        return "bank"
    return "roll"


bank_at_300.description = "Bank once turn score reaches 300, else roll."


def bank_at_500(state):
    """Bank once my turn score reaches 500; otherwise keep rolling."""
    if state["turn_score"] >= 500:
        return "bank"
    return "roll"


bank_at_500.description = "Bank once turn score reaches 500, else roll."


def bank_at_800(state):
    """Bank once my turn score reaches 800; otherwise keep rolling."""
    if state["turn_score"] >= 800:
        return "bank"
    return "roll"


bank_at_800.description = "Bank once turn score reaches 800, else roll."


def cautious_near_target(state):
    """Use my normal threshold (500) -- but once I'm close to winning
    (within 500 points of the target score), play it safer and bank at
    half my normal threshold so I don't blow a winning position."""
    threshold = 500
    safety_margin = 500
    distance_to_win = state["target_score"] - state["total_score"]
    if distance_to_win <= safety_margin:
        return "bank" if state["turn_score"] >= threshold // 2 else "roll"
    return "bank" if state["turn_score"] >= threshold else "roll"


cautious_near_target.description = (
    "Bank at 500 normally; bank at 250 once within 500 points of the target score."
)


def aggressive_when_behind(state):
    """Use my normal threshold (500) -- but if I'm far behind my
    opponent (more than 1000 points), take more risk and require a
    bigger turn score (1500) before banking."""
    threshold = 500
    gap = 1000
    opponent_score = state["opponent_score"] or 0
    behind_by = opponent_score - state["total_score"]
    local_threshold = threshold + gap if behind_by > gap else threshold
    return "bank" if state["turn_score"] >= local_threshold else "roll"


aggressive_when_behind.description = (
    "Bank at 500 normally; require 1500 if more than 1000 points behind the opponent."
)


def always_bank_first_score(state):
    """Take the very first points I earn and stop. The most timid
    possible strategy -- a useful low bar for comparison."""
    return "bank"


always_bank_first_score.description = "Bank the instant any points are on the board."


BUILT_IN_STRATEGIES = {
    "bank_at_300": bank_at_300,
    "bank_at_500": bank_at_500,
    "bank_at_800": bank_at_800,
    "cautious_near_target": cautious_near_target,
    "aggressive_when_behind": aggressive_when_behind,
    "always_bank_first_score": always_bank_first_score,
}
