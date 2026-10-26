# Week 11 example: Rock-Paper-Scissors as a dictionary of dictionaries

File: `rps_dict_of_dicts.py` (plain Python 3, no installs).

```
python3 rps_dict_of_dicts.py          # guided demo, same output every time
python3 rps_dict_of_dicts.py play     # play the computer; type quit to stop
```

## The idea in one sentence

Store the rules of the game as data: `rules[player][opponent]` gives
`"win"`, `"lose"`, or `"tie"`.

## Walkthrough (about 10 minutes live)

1. **Look at the shape.** `rules` is a dictionary. Each value is itself a
   dictionary. `rules["rock"]` is the whole row for "I played rock".
2. **Two lookups.** `rules["rock"]["scissors"]` means "I played rock, the
   opponent played scissors". The first key picks the row, the second picks
   the column. Ask the class to predict `rules["paper"]["rock"]` before running.
3. **Compare with if/elif.** The same game as `if` statements needs nine
   branches (or a tangle of `or`). With the dictionary, `judge()` is one line,
   and changing a rule means changing data, not logic.
4. **Loop over it.** `for player_move in rules:` visits the outer keys;
   `for opponent_move in rules[player_move]:` visits the inner keys. That
   prints the whole table.
5. **A second dictionary keeps score.** `{"win": 0, "lose": 0, "tie": 0}`;
   `scoreboard[result] += 1` is the update. Same idea as counting in a
   list, but the labels are the keys.
6. **Guard the lookup.** A move that is not a key raises `KeyError`. The
   `in` check in `play()` keeps the game from crashing.

## Connect it to this week

- **Lookup by key, not by hand-searching.** This is the Week 11 gate skill.
- **Decide/Compare #1.** A good discussion question: why a dictionary of
  dictionaries here, and not nine if statements, a list of lists, or one
  dictionary keyed by a pair like `("rock", "scissors")`? What does each make
  easier or harder when you add "lizard" and "spock"?
- **Verify (AI Lens 11).** Edge cases to try: an empty string, a capital
  letter, a move that is not in the table. What does the code do for each?

## Try it yourself (beginner extensions)

- Add `"lizard"` and `"spock"`. How many places must change?
- Print the scoreboard after every round.
- Make a different small game table: a vending machine, a crew roster, or a
  case file from your own Odyssey world.
