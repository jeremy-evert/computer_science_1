"""Rock-Paper-Scissors, the if/elif way (version 1 of 3).

CS1 Week 11, step 2 of the lesson arc:
    1. logic map  ->  2. if/elif (this file)  ->  3. dictionary of dictionaries
    4. refactor discussion  ->  5. scale up (rps_advanced_dict.py)

Every outcome is spelled out as a decision.  It works.  Count the branches.

Run it:
    python3 rps_if_elif.py          # guided demo, same output every time
    python3 rps_if_elif.py play     # play against the computer
"""

import random
import sys


def judge(player, opponent):
    """Return "win", "lose", or "tie" for the player's move."""
    if player == opponent:
        return "tie"
    elif player == "rock" and opponent == "scissors":
        return "win"
    elif player == "scissors" and opponent == "paper":
        return "win"
    elif player == "paper" and opponent == "rock":
        return "win"
    else:
        return "lose"


def new_scoreboard():
    return {"win": 0, "lose": 0, "tie": 0}


def play_round(player, opponent, scoreboard):
    result = judge(player, opponent)
    scoreboard[result] += 1
    print(f"You: {player:<8} Opponent: {opponent:<8} -> {result}")
    return result


def show_scoreboard(scoreboard):
    print(
        f"Score -> win: {scoreboard['win']}, "
        f"lose: {scoreboard['lose']}, tie: {scoreboard['tie']}"
    )


def demo():
    print("Step 1: one decision")
    print('judge("rock", "scissors") =', judge("rock", "scissors"))
    print()

    print("Step 2: all nine matchups")
    for player_move in ["rock", "paper", "scissors"]:
        for opponent_move in ["rock", "paper", "scissors"]:
            print(f"  {player_move:<8} vs {opponent_move:<8} -> "
                  f"{judge(player_move, opponent_move)}")
    print()

    print("Step 3: play a few scripted rounds and keep score")
    scoreboard = new_scoreboard()
    for player_move, opponent_move in [
        ("rock", "scissors"),
        ("paper", "paper"),
        ("scissors", "rock"),
        ("paper", "rock"),
    ]:
        play_round(player_move, opponent_move, scoreboard)
    show_scoreboard(scoreboard)
    print()

    print("Step 4: count the branches in judge()")
    print("  1 tie check + 3 winning pairs + 1 else = 5 branches")
    print("  Add lizard and spock and this function needs many more.")


def play():
    scoreboard = new_scoreboard()
    moves = ["rock", "paper", "scissors"]
    print("Rock-Paper-Scissors. Type rock, paper, or scissors. Type quit to stop.")
    while True:
        player_move = input("Your move: ").strip().lower()
        if player_move == "quit":
            break
        if player_move not in moves:
            print("Not a valid move. Try rock, paper, or scissors.")
            continue
        play_round(player_move, random.choice(moves), scoreboard)
    show_scoreboard(scoreboard)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "play":
        play()
    else:
        demo()
