"""Rock-Paper-Scissors with a dictionary of dictionaries.

CS1 Week 11: lists and dictionaries continued.

The big idea: instead of a pile of if/elif statements, store the rules of the
game as DATA.  One dictionary answers "what happens if I play X and the
opponent plays Y?"

    rules[player][opponent]  ->  "win", "lose", or "tie"

The outer dictionary is keyed by YOUR move.  Each value is another
dictionary, keyed by the OPPONENT's move.  Two lookups, one answer.

Run it:
    python3 rps_dict_of_dicts.py          # guided demo, no typing needed
    python3 rps_dict_of_dicts.py play     # play against the computer
"""

import random
import sys

# ---------------------------------------------------------------------------
# 1. The rules: a dictionary whose values are dictionaries.
# ---------------------------------------------------------------------------
rules = {
    "rock": {"rock": "tie", "paper": "lose", "scissors": "win"},
    "paper": {"rock": "win", "paper": "tie", "scissors": "lose"},
    "scissors": {"rock": "lose", "paper": "win", "scissors": "tie"},
}


# ---------------------------------------------------------------------------
# 2. Looking up a result is two keys in a row.
# ---------------------------------------------------------------------------
def judge(player, opponent):
    """Return "win", "lose", or "tie" for the player's move."""
    return rules[player][opponent]


# ---------------------------------------------------------------------------
# 3. A second dictionary keeps score.  Keys are results, values are counts.
# ---------------------------------------------------------------------------
def new_scoreboard():
    return {"win": 0, "lose": 0, "tie": 0}


def play_round(player, opponent, scoreboard):
    """Judge one round, update the scoreboard, and return the result."""
    result = judge(player, opponent)
    scoreboard[result] += 1
    print(f"You: {player:<8} Opponent: {opponent:<8} -> {result}")
    return result


def show_scoreboard(scoreboard):
    print(
        f"Score -> win: {scoreboard['win']}, "
        f"lose: {scoreboard['lose']}, tie: {scoreboard['tie']}"
    )


# ---------------------------------------------------------------------------
# 4. Guided demo: runs the same every time, so you can predict the output.
# ---------------------------------------------------------------------------
def demo():
    print("Step 1: one lookup, two keys")
    print('rules["rock"]            =', rules["rock"])
    print('rules["rock"]["scissors"] =', rules["rock"]["scissors"])
    print()

    print("Step 2: loop over the outer dictionary to print the whole table")
    for player_move in rules:
        for opponent_move in rules[player_move]:
            print(f"  {player_move:<8} vs {opponent_move:<8} -> "
                  f"{rules[player_move][opponent_move]}")
    print()

    print("Step 3: play a few scripted rounds and keep score")
    scoreboard = new_scoreboard()
    scripted_rounds = [
        ("rock", "scissors"),
        ("paper", "paper"),
        ("scissors", "rock"),
        ("paper", "rock"),
    ]
    for player_move, opponent_move in scripted_rounds:
        play_round(player_move, opponent_move, scoreboard)
    show_scoreboard(scoreboard)
    print()

    print("Step 4: what happens with a move that is not in the dictionary?")
    print('  "lizard" in rules ->', "lizard" in rules)
    print("  Check with `in` first, or you get a KeyError.")


# ---------------------------------------------------------------------------
# 5. Interactive play.  The `in` check keeps a bad move from crashing us.
# ---------------------------------------------------------------------------
def play():
    scoreboard = new_scoreboard()
    moves = list(rules)
    print("Rock-Paper-Scissors. Type rock, paper, or scissors. Type quit to stop.")
    while True:
        player_move = input("Your move: ").strip().lower()
        if player_move == "quit":
            break
        if player_move not in rules:
            print("Not a valid move. Try rock, paper, or scissors.")
            continue
        play_round(player_move, random.choice(moves), scoreboard)
    show_scoreboard(scoreboard)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        play()
    else:
        demo()
