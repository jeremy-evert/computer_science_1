import random
import matplotlib.pyplot as plt

number_of_games = 10
number_of_rounds = 3
choices = ["rock", "paper", "scissors"]

figure, axes = plt.subplots(number_of_rounds, 1, figsize=(12, 12), sharex=True)

for pass_number in range(number_of_rounds):

    # Start each pass with fresh counts.
    wins = 0
    losses = 0
    ties = 0

    games_played = [0]

    # No probability estimate exists before the first game.
    win_estimates = [float("nan")]
    loss_estimates = [float("nan")]
    tie_estimates = [float("nan")]

    for game_number in range(1, number_of_games + 1):

        player = random.choice(choices)
        computer = random.choice(choices)

        # Determine the result from the player's perspective.
        if player == "rock":
            if computer == "rock":
                ties += 1
            elif computer == "paper":
                losses += 1
            else:
                wins += 1

        elif player == "paper":
            if computer == "rock":
                wins += 1
            elif computer == "paper":
                ties += 1
            else:
                losses += 1

        else:  # Player chose scissors.
            if computer == "rock":
                losses += 1
            elif computer == "paper":
                wins += 1
            else:
                ties += 1

        # Update our estimates after EVERY game.
        win_probability = wins / game_number
        loss_probability = losses / game_number
        tie_probability = ties / game_number

        games_played.append(game_number)
        win_estimates.append(win_probability)
        loss_estimates.append(loss_probability)
        tie_estimates.append(tie_probability)

    # Draw one graph for this pass.
    graph = axes[pass_number]

    graph.plot(games_played, win_estimates, label="Player wins")
    graph.plot(games_played, loss_estimates, label="Player loses")
    graph.plot(games_played, tie_estimates, label="Tie")

    graph.axhline(
        y=1 / 3,
        color="black",
        linestyle="--",
        label="Expected probability: 1/3"
    )

    graph.set_title(f"Pass {pass_number + 1}")
    graph.set_ylabel("Estimated probability")
    graph.set_xlim(0, number_of_games)
    graph.set_ylim(0, 1)
    graph.legend()
    graph.grid(True)

    # Print a final summary, not 100,000 individual lines.
    print(f"\nPass {pass_number + 1}: {number_of_games:,} games")
    print(f"Wins:   {wins:6,}  Estimated probability: {win_probability:.4%}")
    print(f"Losses: {losses:6,}  Estimated probability: {loss_probability:.4%}")
    print(f"Ties:   {ties:6,}  Estimated probability: {tie_probability:.4%}")

axes[-1].set_xlabel("Games played")

figure.suptitle("Rock Paper Scissors: Estimates After Every Game")
plt.tight_layout()
plt.show()