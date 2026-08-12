# Week 16 — Farkle and a machine that learns to play it

## Objectives

- Play Farkle well enough to have and defend an opinion about strategy.
- Name the state, the action, and the reward/outcome in a decision you
  already understand (bank or roll again).
- Run a program that tries many strategies automatically and improves
  one of its own, using nothing but a dictionary and a loop.
- Compare a human strategy to a machine strategy using evidence from
  thousands of simulated games, not a handful of lucky rounds.
- Say, in your own words, what the machine paid attention to, what
  changed after a lot of practice, and one thing it still doesn't
  understand.

## Key content

Farkle rules and scoring, the roll/bank decision, human strategies as
functions, a transparent "experience table" learner, simulation and
comparison, and honest interpretation of evidence.

This week does **not** require anything new about calculus, probability
theory, discount factors, or neural networks. If you've made it through
CS1 -- variables, branching, loops, functions, strings, lists,
dictionaries -- you already have every tool this week uses.

---

## 1. The game: Farkle

Farkle is a dice game about a single repeated tension:

> **Do I bank what I have, or risk another roll for a bigger score?**

Here is the exact rule set our simulator uses (some real-world Farkle
house rules differ -- this is the one version we're all playing):

- Six dice, standard six-sided.
- A single **1** is worth **100 points**. A single **5** is worth **50
  points**.
- **Three of a kind** is worth more: three 1s = **1000**; three of any
  other value V = **V × 100** (three 6s = 600, three 2s = 200, etc.).
- **Four, five, or six of a kind** doubles the three-of-a-kind value for
  each extra matching die: four of a kind = 2×, five of a kind = 4×, six
  of a kind = 8× the three-of-a-kind value.
- We do **not** use straights or three-pairs bonuses. Real Farkle rule
  sheets disagree about these enough that leaving them out keeps the
  scoring rule small enough to trace by hand.
- If a roll has **no scoring dice at all**, that's a **Farkle**: your
  turn ends immediately and you lose every point you'd built up *this
  turn* (points already banked from earlier turns are safe).
- **Hot dice**: if every die you just rolled scored, you get to roll all
  six again, keeping your turn score. Best possible outcome of a roll.
- Whichever dice score on a roll are automatically kept -- there's no
  "which dice do I set aside" puzzle in our version. The only decision is:
  **after seeing your turn score, do you ROLL again or BANK it?**
- First player to reach **4000 total points** wins the game. (Real
  Farkle is often played to 10,000 -- we use a smaller target so a
  simulation of thousands of games finishes in under a second.)

### Try it by hand first

Before touching any code, play a few rounds with real dice (or roll six
dice using any dice-roller you like) and keep a running turn score on
paper. Farkle a couple of times on purpose by rolling too greedily.
Notice how it feels different from *reading about* the risk.

Then answer, out loud or in your notes, **before reading further**:

- What turn score would make you stop and bank, most of the time?
- Does your answer change if you're way behind? Way ahead? Close to
  winning?

You now have a strategy. Hang on to it -- Part 3 asks you to write it
down as actual Python.

---

## 2. The vocabulary: state, action, reward

Machine learning uses three words for exactly the situation you just
lived through:

| ML word | What it means here | What it looks like in our code |
|---|---|---|
| **State** | Everything you know right now, before deciding | a dictionary: `{"turn_score": 250, "dice_remaining": 3, "total_score": 1400, "target_score": 4000, "opponent_score": 900}` |
| **Action** | The choice available to you | the string `"roll"` or `"bank"` |
| **Reward / outcome** | What actually happened because of that choice | the points you banked (good) or the points you lost to a Farkle (bad) |

That's the whole vocabulary. A "strategy" -- yours or the machine's -- is
just a function that looks at a state and returns an action:

```python
def bank_at_300(state):
    if state["turn_score"] >= 300:
        return "bank"
    return "roll"
```

If you can read that function, you can read every strategy in this
week's code, including the one the machine builds for itself.

---

## 3. Run the baseline simulator

All the code for this week lives in `lessons/code/farkle/`. Open these
three files in this order and read them like a story, not line by line:

1. `engine.py` -- the dice, the scoring rule, and one full turn.
2. `strategies.py` -- three or four human strategies, each one a
   plain-language sentence turned into an `if` statement.
3. `simulate.py` -- code that plays a strategy against another strategy
   thousands of times and adds up the results.

From `lessons/code/`, run:

```
python3 -m farkle.cli play --seed 1 --strategy bank_at_300
```

This plays and prints **one full turn**, roll by roll, so you can watch
a strategy make decisions in real time. Run it again with a different
`--seed` and notice the dice are different but the strategy's *reasoning*
is identical every time -- the strategy doesn't change, only the luck
does.

Now run a real comparison:

```
python3 -m farkle.cli compare --seed 1 --games 5000 \
    --strategy-a bank_at_300 --strategy-b bank_at_800
```

This plays 5000 full games (not turns -- games, first to 4000) between a
strategy that banks early (300) and one that holds out for a big score
(800), and reports win rate, average score, and how often each strategy
Farkles.

**Write down what you predicted before running it, then compare.** Most
people expect the aggressive strategy to win more often. Does it?

---

## 4. A strategy that changes itself

Now open `learner.py`. Read its module docstring first -- it explains,
in plain language, exactly what the "learning" is:

> A dictionary. That's the whole trick.

The learner keeps a running average of "how did it turn out, the times I
tried this?" for every (turn score, dice remaining, action) situation it
has seen. After a training turn ends, it updates that average with the
turn's real result. No calculus is involved -- the update is one line:

```python
average = average + (new_result - average) / times_seen
```

That's the same idea as a running batting average: each new result nudges
the average a little, and the more times you've seen a situation, the
less any one new result moves it.

**One more idea before you train it: exploration.** If the table always
did whatever currently looks best, it could get stuck: maybe "roll"
looked bad the first time purely from bad luck, and the table would
never try it again to find out that was a fluke. So during training,
the table has a setting called `epsilon` (a fraction like 0.2, meaning
"about 1 time in 5"): that often, it ignores its own table and tries a
random action instead, just to keep gathering evidence on both choices.
The rest of the time, it plays whatever currently has the better average.
You can change this with `--epsilon` on the command line (default 0.2)
if you want to see how more or less exploration changes what the table
learns.

Train it and look inside:

```
python3 -m farkle.cli train --seed 1 --turns 20000 --show-table
```

This prints the entire table -- every situation the learner has an
opinion about, both actions' running averages, and which one it
currently prefers. **This is the whole "brain."** There is nothing
hidden. Scroll through a few rows and answer:

- Find a row where `dice_remaining` is 1 or 2. What does the table
  prefer there? Does that match your own instinct?
- Find a row where `dice_remaining` is 6 (that only happens right after
  hot dice). What does the table prefer there? Why might that make sense?
- Pick one row and explain, in one sentence, why the numbers point the
  way they do.

---

## 5. Test the learner on fresh games

A model that's only ever been checked against the exact games it trained
on hasn't proven anything -- it might just be memorizing, or you might be
fooling yourself. Run the full experiment, which trains the learner and
**then** evaluates it on a completely different batch of games:

```
python3 -m farkle.cli learn-vs-baseline --seed 1 --turns 20000 \
    --games 5000 --baseline bank_at_300
```

Read the output. It reports the learned strategy's win rate, average
score, and Farkle rate against a fixed baseline over 5000 fresh games.

Run it again with a different `--seed`. Does the story hold up, or was
the first result a fluke?

---

## 6. Interpretation questions (answer for your evidence receipt)

1. What information did the machine pay attention to? What did it
   deliberately ignore, and would ignoring that hurt it?
2. Pick one specific state/action pair from your trained table. What did
   the machine learn to do there, and does that match your own human
   strategy from Part 1?
3. What changed in the win-rate/Farkle-rate numbers between the untrained
   baseline-vs-baseline comparison and the learned-vs-baseline
   comparison?
4. Is "different" the same as "better"? What in your printed results is
   the actual evidence that it's better, not just different?
5. What is one thing about Farkle the machine still doesn't understand
   or account for? (Hint: what's in a state dictionary, and what human
   strategies in Part 1 might use that isn't there?)

---

## 7. Submit your evidence receipt

Use `assignments/W16-farkle-ml-experiment-receipt.md` as your template.
It is short on purpose -- this is the fun week, not another giant
project.

---

## A note on what this is and isn't

This experience table is a real, working example of a machine changing
its behavior because of repeated experience with feedback. It is a
deliberately simplified relative of a family of techniques called
**reinforcement learning**, which includes the ideas that power
game-playing and robotics systems you may have heard of. Real
reinforcement learning usually credits each individual decision
separately for its effect on the future (using ideas like discounted
future reward), which this version does not do -- every decision in a
turn shares the same final grade, win or lose. That's a real
simplification, not a trick, and it's exactly the trade CS1 makes on
purpose: you leave this week able to explain *how* a machine can improve
from data, without needing a semester of probability and calculus first.
If this genuinely interests you, `docs/curriculum/cs2-farkle-ml-handoff.md`
lists what a deeper version would add.
