"""Rock-Paper-Scissors-Lizard-Spock-Batman-Glock: the dictionary scales (step 5).

CS1 Week 11.  Same idea as rps_dict_of_dicts.py, seven moves instead of three.

The data is a dictionary of dictionaries again, but this time the inner value
is the VERB, so the game can explain itself:

    beats["rock"]["scissors"]  ->  "crushes"      (rock crushes scissors)

From that one table we build the full rules[a][b] -> "win"/"lose"/"tie" table.
Adding an eighth move means adding data.  The judge() function never changes.

Fairness check: with 7 moves, every move beats exactly 3 others and loses to 3.

Run it:
    python3 rps_advanced_dict.py          # guided demo, same output every time
    python3 rps_advanced_dict.py play     # play against the computer
"""

import random
import sys

# ---------------------------------------------------------------------------
# The data: who beats whom, and how.  beats[winner][loser] -> verb.
# ---------------------------------------------------------------------------
beats = {
    "rock":     {"scissors": "crushes", "lizard": "crushes", "glock": "jams"},
    "paper":    {"rock": "covers", "spock": "disproves", "glock": "jams"},
    "scissors": {"paper": "cut", "lizard": "decapitate", "batman": "snip the cape of"},
    "lizard":   {"paper": "eats", "spock": "poisons", "batman": "bites"},
    "spock":    {"scissors": "smashes", "rock": "vaporizes", "batman": "nerve-pinches"},
    "batman":   {"rock": "outsmarts", "paper": "out-detects", "glock": "disarms"},
    "glock":    {"scissors": "shoots", "lizard": "shoots", "spock": "shoots"},
}

# ---------------------------------------------------------------------------
# Build rules[a][b] -> "win" / "lose" / "tie" from the data above.
# ---------------------------------------------------------------------------
rules = {}
for a in beats:
    rules[a] = {}
    for b in beats:
        if a == b:
            rules[a][b] = "tie"
        elif b in beats[a]:
            rules[a][b] = "win"
        else:
            rules[a][b] = "lose"


def judge(player, opponent):
    """The same one line as before, no matter how many moves exist."""
    return rules[player][opponent]


def explain(player, opponent):
    """Say why, using the verb table."""
    if player == opponent:
        return f"{player} vs {opponent}: tie"
    if opponent in beats[player]:
        return f"{player} {beats[player][opponent]} {opponent}"
    return f"{opponent} {beats[opponent][player]} {player}"


def new_scoreboard():
    return {"win": 0, "lose": 0, "tie": 0}


def play_round(player, opponent, scoreboard):
    result = judge(player, opponent)
    scoreboard[result] += 1
    print(f"You: {player:<8} Opponent: {opponent:<8} -> {result:<4} ({explain(player, opponent)})")
    return result


def show_scoreboard(scoreboard):
    print(
        f"Score -> win: {scoreboard['win']}, "
        f"lose: {scoreboard['lose']}, tie: {scoreboard['tie']}"
    )


def old_way_branch_count(move_count):
    """Branches an if/elif judge needs: 1 tie check, one per winning pair, 1 else."""
    winning_pairs = move_count * (move_count - 1) // 2
    return 1 + winning_pairs + 1


def demo():
    print("Step 1: seven moves, one lookup")
    print('rules["batman"]["glock"] =', rules["batman"]["glock"])
    print('explain("batman", "glock") ->', explain("batman", "glock"))
    print()

    print("Step 2: fairness check (each move should beat 3 and lose to 3)")
    for move in rules:
        wins = sum(1 for result in rules[move].values() if result == "win")
        losses = sum(1 for result in rules[move].values() if result == "lose")
        print(f"  {move:<8} wins: {wins}  losses: {losses}")
    print()

    print("Step 3: play a few scripted rounds and keep score")
    scoreboard = new_scoreboard()
    for player_move, opponent_move in [
        ("lizard", "spock"),
        ("glock", "batman"),
        ("rock", "rock"),
        ("scissors", "batman"),
        ("spock", "glock"),
    ]:
        play_round(player_move, opponent_move, scoreboard)
    show_scoreboard(scoreboard)
    print()

    print("Step 4: how the two approaches scale")
    print("  moves | if/elif branches | dictionary entries | judge() lines")
    for count in (3, 5, 7, 9):
        print(f"  {count:>5} | {old_way_branch_count(count):>16} | {count * count:>18} | {'1':>13}")
    print("  The if/elif function keeps growing. The dictionary is just data.")


def play():
    scoreboard = new_scoreboard()
    moves = list(rules)
    print("Moves:", ", ".join(moves), "(type quit to stop)")
    while True:
        player_move = input("Your move: ").strip().lower()
        if player_move == "quit":
            break
        if player_move not in rules:
            print("Not a valid move.")
            continue
        play_round(player_move, random.choice(moves), scoreboard)
    show_scoreboard(scoreboard)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        play()
    else:
        demo()
