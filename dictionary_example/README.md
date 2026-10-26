# Week 11 example: Rock-Paper-Scissors, from if/elif to a dictionary of dictionaries

Plain Python 3, no installs. One lesson arc, five steps, in this order.

| Step | What | File |
|---|---|---|
| 1 | Logic map: how the game decides a winner | `rps_logic_map.png` (source `rps_logic_map.tex`) |
| 2 | Solve it with if/elif | `rps_if_elif.py` |
| 3 | Solve it with a dictionary of dictionaries | `rps_dict_of_dicts.py` |
| 4 | Refactoring discussion | slides, slide 4 |
| 5 | Scale up: Rock, Paper, Scissors, Lizard, Spock, Batman, Glock | `rps_advanced_dict.py` |

Each program runs two ways:

```
python3 rps_if_elif.py          # guided demo, same output every time
python3 rps_if_elif.py play     # play the computer; type quit to stop
```

## Walkthrough (about 25 minutes live)

1. **Draw the logic first.** Same move? Tie. Otherwise does my move beat
   theirs? Three winning pairs (rock-scissors, scissors-paper, paper-rock);
   everything else is a loss. Ask students to predict three matchups from the map.
2. **if/elif.** `judge()` has five branches and mirrors the map line by line.
   It works. Ask: what would lizard and spock cost us?
3. **Dictionary of dictionaries.** `rules[player][opponent]` returns the
   result. First key picks the row, second picks the column. `judge()` is one
   line. Run both files: the demo scores are identical. That is how you check a
   refactor.
4. **Refactoring discussion.** What got simpler (one-line judge, readable
   table)? What got easier to extend (new move = new data)? What stayed the same
   (inputs, outputs, scoreboard)? Refactoring changes structure, not behavior,
   and you prove it by comparing old and new results on every case.
5. **Scale up.** `rps_advanced_dict.py` stores a `beats[winner][loser]` table
   of verbs for seven moves and builds `rules[a][b]` from it. Every move beats
   exactly three and loses to three (the script checks). Branches the old way
   needs: 1 tie check, one per winning pair, 1 else: 5 for 3 moves, 12 for 5,
   23 for 7, 38 for 9. The dictionary needs more data, and `judge()` stays one
   line.

## Connect it to this week

- **Lookup by key, not hand-searching:** the Week 11 gate skill.
- **Decide/Compare #1:** why a dict of dicts, and not nine ifs, a list of
  lists, or one dict keyed by a pair like `("rock", "scissors")`? What does each
  make easier or harder when you add moves?
- **Verify (AI Lens 11):** try an empty string, a capital letter, a move not
  in the table. What does each version do? What test would catch a wrong rule?

## Try it yourself

- Add an eighth move to `beats` (and one more to keep it fair: odd counts only).
  How many places change?
- Print the scoreboard after every round.
- Make a different table for your own world: crew roster, case files, customers.
