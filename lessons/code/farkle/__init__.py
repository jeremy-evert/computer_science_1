"""farkle -- a small, transparent Farkle simulator and learner for CS1 Week 16.

This package is intentionally simple. Every file is meant to be readable by
a student who has finished CS1: variables, branching, loops, functions,
strings, lists, dictionaries, and a little bit of classes/objects. There is
no machine-learning library dependency and no reinforcement-learning math
(no Bellman equation, no discount factor, no neural network). The "learner"
in learner.py is a dictionary that keeps a running average of what happened
after each decision -- see its docstring for the plain-language explanation.

Modules:
    engine.py      -- dice, scoring, and one turn of Farkle
    strategies.py  -- human-readable, rule-based strategies (functions)
    learner.py     -- the transparent "experience table" learner
    simulate.py    -- run many turns/games and summarize results
    cli.py         -- runnable command-line entry point for the Week 16 lab
"""
