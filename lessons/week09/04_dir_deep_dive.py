"""
04_dir_deep_dive.py
===================
Week 9 -- Objects you use, classes you write.

IDEA OF THIS FILE
-----------------
dir() gives us a big noisy list. Because it is just a list of strings,
we can use everything we know (loops, filters, comprehensions) to make it
useful.

We will:
    - split the "dunder" names from the everyday names
    - see that dunder names are the plumbing behind len() and +
    - separate methods from attributes using callable()
    - compare two classes (str and list) with set math

Run it:   python 04_dir_deep_dive.py
"""

name = "Jeremy"
names = dir(name)

# ---------------------------------------------------------------------------
# PART A: separate the "dunder" plumbing from the everyday methods
# ---------------------------------------------------------------------------
# A dunder name starts with two underscores: __init__, __len__, __add__ ...
# Python calls these behind the scenes. For example, len(name) secretly
# calls name.__len__(), and name + "!" secretly calls name.__add__("!").
dunders = [n for n in names if n.startswith("__")]
public = [n for n in names if not n.startswith("__")]

print("dunder names:", len(dunders))
print("public names:", len(public))
print()
print("public str methods:")
print(public)

# ---------------------------------------------------------------------------
# PART B: the plumbing is really there
# ---------------------------------------------------------------------------
# Each pair of lines below means exactly the same thing.
print()
print("len(name)         ->", len(name))
print("name.__len__()    ->", name.__len__())

print('name + "!"        ->', name + "!")
print('name.__add__("!") ->', name.__add__("!"))

# ---------------------------------------------------------------------------
# PART C: which names are methods and which are plain data?
# ---------------------------------------------------------------------------
# getattr(obj, "text") is the same as obj.text, but the name is a string,
# so we can loop over it.
methods = [n for n in public if callable(getattr(name, n))]
print()
print("callable public names on a str:", len(methods))
print("same as public count? ", len(methods) == len(public))
print("(a str has no public data attributes -- every public name is a method)")

# ---------------------------------------------------------------------------
# PART D: compare two classes with sets
# ---------------------------------------------------------------------------
# A set throws away order and duplicates, and gives us & (in both)
# and - (in the first only).
str_public = {n for n in dir(str) if not n.startswith("_")}
list_public = {n for n in dir(list) if not n.startswith("_")}

print()
print("methods BOTH str and list have:", sorted(str_public & list_public))
print("only str has (first 8):        ", sorted(str_public - list_public)[:8])
print("only list has:                 ", sorted(list_public - str_public))

# ---------------------------------------------------------------------------
# PART E: hasattr() -- ask before you use
# ---------------------------------------------------------------------------
print()
print("does a str have .upper?  ", hasattr(name, "upper"))
print("does a str have .append? ", hasattr(name, "append"))

# TRY IT
# 1. Do the set comparison for int and float. What do they share?
# 2. Which public methods does a dict have that a list does not?
