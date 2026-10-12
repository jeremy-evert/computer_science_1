"""
03_exploring_with_type_dir_help.py
==================================
Week 9 -- Objects you use, classes you write.

IDEA OF THIS FILE
-----------------
You do NOT need to memorize what a string can do. Python will tell you.
Built-in tools let you explore ANY object:

    type(x)       -> what class is x an instance of?
    dir(x)        -> what names (attributes and methods) does x have?
    help(x)       -> read the documentation for x

Then we meet the "dunder" names that dir() shows. A dunder name
(double-underscore, like __doc__) is a hook Python uses behind the
scenes. You almost never type them -- you type everyday syntax, and
Python quietly calls the dunder for you:

    what you write      what Python actually calls
    ------------------  ------------------------------
    str(x), print(x)    x.__str__()
    repr(x)             x.__repr__()
    len(x)              x.__len__()
    x + y               x.__add__(y)
    x == y              x.__eq__(y)
    x[0]                x.__getitem__(0)
    "a" in x            x.__contains__("a")
    SomeClass(...)      SomeClass.__init__(new_object, ...)

When we write our own classes (files 06-08), THESE are the methods we
define so that our objects work with print(), len(), +, == and friends.

Run it:   python 03_exploring_with_type_dir_help.py
"""

name = "Jeremy"

# ===========================================================================
# PART 1: THE THREE EXPLORATION TOOLS
# ===========================================================================

# ---------------------------------------------------------------------------
# TOOL 1: type()  -- "what are you?"
# ---------------------------------------------------------------------------
print("=== type() ===")
print("type(name):", type(name))
print("type(name) is str:", type(name) is str)   # the class is the object `str`

# ---------------------------------------------------------------------------
# TOOL 2: dir()  -- "what can you do?"
# ---------------------------------------------------------------------------
# dir() returns a LIST of strings: every name available on the object.
# It is long, so we only peek at the size and a few entries.
print()
print("=== dir() ===")
everything = dir(name)
print("how many names does a str have?", len(everything))
print("first ten names:", everything[:10])
print("last five names:", everything[-5:])
# The names that start and end with __ are the dunders. The rest are the
# everyday methods (.upper(), .strip(), ...). Part 2 is all about dunders.

# ---------------------------------------------------------------------------
# TOOL 3: help()  -- "how do I use that?"
# ---------------------------------------------------------------------------
# help(str.upper) prints the documentation for ONE method.
# Notice we ask the CLASS (str.upper) rather than a particular string.
print()
print("=== help(str.upper) ===")
help(str.upper)


# ===========================================================================
# PART 2: A TOUR OF THE USEFUL DUNDERS
# ===========================================================================
# Every dunder below is already inside a str (and most are inside list,
# int, dict ...). For each one we show BOTH spellings side by side:
#     the everyday syntax   vs.   the dunder it secretly calls.
# They produce the same answer. That is the whole lesson.

print()
print("=== dunder tour ===")

# ---------------------------------------------------------------------------
# __doc__  -- the documentation string
# ---------------------------------------------------------------------------
# Every documented object stores its docs in __doc__.
# help() is basically a friendly pager wrapped around this.
print()
print("--- __doc__ : the documentation text ---")
print("str.upper.__doc__:", str.upper.__doc__)
print("first line of str.__doc__:", str.__doc__.splitlines()[0])

# ---------------------------------------------------------------------------
# __init__  -- the INITIALIZER: sets up a brand-new object
# ---------------------------------------------------------------------------
# When you write list("abc"), Python builds an empty list and then calls
# list.__init__ on it to fill it in. We rarely call __init__ by hand,
# but we can SEE it work. (Do not do this in real code -- it is a demo.)
print()
print("--- __init__ : runs when an object is created ---")
letters = list("abc")                      # the normal way
print("list('abc'):          ", letters)

rebuilt = [1, 2, 3]
rebuilt.__init__("xyz")                    # re-run the initializer by hand
print("[1, 2, 3].__init__('xyz'):", rebuilt)
# In file 06 YOU will write an __init__ for your own class.

# ---------------------------------------------------------------------------
# __str__  -- the friendly, human-readable text
# __repr__ -- the precise, developer-readable text
# ---------------------------------------------------------------------------
# print(x) and str(x) call __str__.
# repr(x) (and the interactive prompt) call __repr__.
# For strings the difference is easy to see: repr keeps the quotes.
print()
print("--- __str__ and __repr__ : how an object turns into text ---")
print("print(name)       ->", name)
print("name.__str__()    ->", name.__str__())
print("repr(name)        ->", repr(name))
print("name.__repr__()   ->", name.__repr__())

tab_text = "a\tb"                          # contains a real tab character
print("print(tab_text)   ->", tab_text)
print("repr(tab_text)    ->", repr(tab_text))   # shows \t instead of a gap

# ---------------------------------------------------------------------------
# __len__  -- how many items does this have?
# ---------------------------------------------------------------------------
print()
print("--- __len__ : powers len() ---")
print("len(name)       ->", len(name))
print("name.__len__()  ->", name.__len__())
print("len([1, 2, 3])  ->", len([1, 2, 3]))   # lists have it too

# ---------------------------------------------------------------------------
# __add__ and __mul__  -- what + and * mean for this kind of object
# ---------------------------------------------------------------------------
# The SAME symbol means different things for different classes,
# because each class supplies its own __add__.
print()
print("--- __add__ and __mul__ : powers + and * ---")
print('name + "!"             ->', name + "!")
print('name.__add__("!")      ->', name.__add__("!"))
print("name * 2               ->", name * 2)
print("name.__mul__(2)        ->", name.__mul__(2))
print("2 + 3                  ->", 2 + 3, "(ints add numerically)")
print("[1] + [2]              ->", [1] + [2], "(lists join)")

# ---------------------------------------------------------------------------
# __eq__ and __lt__  -- comparison: == and <
# ---------------------------------------------------------------------------
print()
print("--- __eq__ and __lt__ : power == and < ---")
print('name == "Jeremy"        ->', name == "Jeremy")
print('name.__eq__("Jeremy")   ->', name.__eq__("Jeremy"))
print('"apple" < "banana"      ->', "apple" < "banana")
print('"apple".__lt__("banana")->', "apple".__lt__("banana"))

# ---------------------------------------------------------------------------
# __getitem__  -- indexing with [ ]
# ---------------------------------------------------------------------------
print()
print("--- __getitem__ : powers name[0] and slicing ---")
print("name[0]               ->", name[0])
print("name.__getitem__(0)   ->", name.__getitem__(0))
print("name[1:4]             ->", name[1:4])

# ---------------------------------------------------------------------------
# __contains__  -- the `in` operator
# ---------------------------------------------------------------------------
print()
print("--- __contains__ : powers `in` ---")
print('"rem" in name               ->', "rem" in name)
print('name.__contains__("rem")    ->', name.__contains__("rem"))

# ---------------------------------------------------------------------------
# __class__ and __name__  -- an object knows what class it came from
# ---------------------------------------------------------------------------
# type(x) and x.__class__ are two ways to ask the same question.
print()
print("--- __class__ and __name__ : who made you? ---")
print("name.__class__           ->", name.__class__)
print("name.__class__.__name__  ->", name.__class__.__name__)
print("type(name) is name.__class__ ->", type(name) is name.__class__)


# ===========================================================================
# PART 3: SEE WHICH DUNDERS AN OBJECT HAS
# ===========================================================================
# dir() shows them all. Here we check for our favorites by name, and
# compare a str with a plain int to see that classes choose which
# dunders they support.
print()
print("=== which dunders does each class have? ===")
favorites = ["__init__", "__str__", "__repr__", "__len__", "__add__",
             "__eq__", "__lt__", "__getitem__", "__contains__"]

for dunder in favorites:
    print(f"{dunder:14} str: {hasattr('', dunder)!s:5}   int: {hasattr(0, dunder)}")
# Notice int has no __len__ or __getitem__ -- len(5) and 5[0] are errors
# because an int is not a collection. A class gets only the behavior
# it chooses to define.


# ===========================================================================
# WORKFLOW YOU CAN USE FOREVER
# ===========================================================================
#   1. type(thing)        -> learn the class name
#   2. dir(thing)         -> scan for a method that sounds right
#   3. help(thing.method) -> read how it works
#   4. spot a dunder?     -> it is the hook behind some everyday syntax
#
# TRY IT
# 1. Run dir("") and look for a method that sounds like it checks digits.
#    Use help(str.isdigit) to read about it, then test "123" and "12a".
# 2. Call len(5) and see the error. Which dunder is missing?
# 3. Compare name.__add__("!") with name.__add__(5). What comes back for 5?
# 4. Use help(str.__len__) and help(list.__len__). Same idea, two classes.
# 5. Which dunder would you guess powers `-` on ints? Check with dir(5).
