"""
05_classes_and_instances.py
===========================
Week 9 -- Objects you use, classes you write.

IDEA OF THIS FILE  (the big realization)
----------------------------------------
We have been using INSTANCES all semester.

    CLASS     = the blueprint   (str, list, int, dict)
    INSTANCE  = one object built from the blueprint  ("Jeremy", [1, 2, 3])

    str   is a class.          "Jeremy"   is an object (an instance).
    list  is a class.          [1, 2, 3]  is an object (an instance).

We USED classes before. Next file, we WRITE one.

Run it:   python 05_classes_and_instances.py
"""

# ---------------------------------------------------------------------------
# PART A: literals are shortcuts for calling the class
# ---------------------------------------------------------------------------
# These two lines build an equivalent string. The class itself is callable,
# just like a function. Calling a class MAKES AN INSTANCE.
a = "42"
b = str(42)
print("a:", repr(a), " b:", repr(b), " equal?", a == b)

# Same for lists: [...] is a friendly shortcut for list(...).
items = ["flour", "bandages"]
same_items = list(("flour", "bandages"))      # build from any sequence
print("items:", items, " same_items:", same_items, " equal?", items == same_items)

# ---------------------------------------------------------------------------
# PART B: one class, many instances
# ---------------------------------------------------------------------------
first = "ping"
second = "pong"

print()
print("same class? ", type(first) is type(second))   # True: both are str
print("same object?", first is second)               # False: two instances
print("same value? ", first == second)               # False: different text

# Each instance carries its own data, but they share one set of methods
# (the methods live on the class, not inside every string).
print(first.upper(), second.upper())

# ---------------------------------------------------------------------------
# PART C: isinstance() -- "was this built from that class?"
# ---------------------------------------------------------------------------
print()
print("isinstance('hi', str)  ->", isinstance("hi", str))
print("isinstance('hi', list) ->", isinstance("hi", list))

# ---------------------------------------------------------------------------
# PART D: even classes are objects, and they have a type too
# ---------------------------------------------------------------------------
print()
print("type('Jeremy') ->", type("Jeremy"))      # <class 'str'>
print("type(str)      ->", type(str))           # <class 'type'>
# `type` is the class that builds classes. You do not need this yet --
# just notice: in Python, "everything is an object" goes all the way down.

# ---------------------------------------------------------------------------
# PART E: the evolution of the semester
# ---------------------------------------------------------------------------
#   Weeks 1-8 : we USED objects.
#   Week  9   : we discover those objects came from CLASSES.
#   Week  9+  : we WRITE classes of our own.
#
# TRY IT
# 1. Build a list with list("hello"). What do you get?
# 2. What does isinstance(3, int) say? isinstance(True, int)? Surprised?
