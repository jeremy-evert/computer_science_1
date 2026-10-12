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
    x.__doc__     -> the raw documentation string (what help() shows)

Run it:   python 03_exploring_with_type_dir_help.py
"""

name = "Jeremy"

# ---------------------------------------------------------------------------
# TOOL 1: type()  -- "what are you?"
# ---------------------------------------------------------------------------
print("=== type() ===")
print(type(name))
print(type(name) is str)       # True: the class is literally the object `str`

# ---------------------------------------------------------------------------
# TOOL 2: dir()  -- "what can you do?"
# ---------------------------------------------------------------------------
# dir() returns a LIST of strings: every name available on the object.
# It is long, so we only peek at the size and the first few entries.
print()
print("=== dir() ===")
everything = dir(name)
print("how many names does a str have?", len(everything))
print("first ten:", everything[:10])
# Names starting and ending with __ are "dunder" (double-underscore)
# names. They are Python's internal plumbing. We look at them in file 04.

# ---------------------------------------------------------------------------
# TOOL 3: help()  -- "how do I use that?"
# ---------------------------------------------------------------------------
# help(str.upper) prints the documentation for ONE method.
# Notice we ask the CLASS (str.upper) rather than a particular string.
print()
print("=== help(str.upper) ===")
help(str.upper)

# ---------------------------------------------------------------------------
# TOOL 4: __doc__  -- the same text, as a plain string
# ---------------------------------------------------------------------------
# Every documented object stores its docs in a special attribute: __doc__.
# help() is basically a friendly pager wrapped around this.
print("=== __doc__ ===")
print(str.upper.__doc__)
print()
print("first line of the str class docs:")
print(str.__doc__.splitlines()[0])

# ---------------------------------------------------------------------------
# WORKFLOW YOU CAN USE FOREVER
# ---------------------------------------------------------------------------
#   1. type(thing)        -> learn the class name
#   2. dir(thing)         -> scan for a method that sounds right
#   3. help(thing.method) -> read how it works
#
# TRY IT
# 1. Run dir("") and look for a method that sounds like it checks digits.
# 2. Use help(str.isdigit) to read about it, then test it on "123" and "12a".
# 3. Do the same three steps with a list: dir([]) and help(list.append).
