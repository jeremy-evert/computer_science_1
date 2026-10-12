"""
01_strings_are_objects.py
=========================
Week 9 -- Objects you use, classes you write.

IDEA OF THIS FILE
-----------------
Every string you have ever typed is an OBJECT.
An object is a bundle of two things:

    1. DATA      -- the information it holds   (the characters)
    2. BEHAVIOR  -- the things it can do       (methods like .upper())

We have been using objects since Week 1. We just never called them that.

Run it:   python 01_strings_are_objects.py
"""

# ---------------------------------------------------------------------------
# STEP 1: Make a string. This is an object.
# ---------------------------------------------------------------------------
# The right-hand side, "Jeremy", is a string LITERAL.
# Python builds a str object in memory and `name` becomes a label
# (a reference) pointing at that object.
name = "Jeremy"

print("name is:", name)

# ---------------------------------------------------------------------------
# STEP 2: Ask Python "what kind of thing is this?"  -> type()
# ---------------------------------------------------------------------------
# type() returns the CLASS that the object was built from.
# Read the output as: "name is an instance of the class str".
print("type of name:", type(name))

# ---------------------------------------------------------------------------
# STEP 3: Objects have behavior. Behavior is called with DOT NOTATION.
# ---------------------------------------------------------------------------
#   object.method()
#   ^^^^^^ ^^^^^^ ^^
#   |      |      parentheses CALL the method (do the work)
#   |      the name of the behavior
#   the object doing the work
print("upper:", name.upper())
print("lower:", name.lower())
print("length via len():", len(name))

# ---------------------------------------------------------------------------
# STEP 4: Methods RETURN new values. They do not change the string.
# ---------------------------------------------------------------------------
# Strings are IMMUTABLE: once built, the characters never change.
# .upper() builds a brand-new string and hands it back.
shout = name.upper()
print("shout:", shout)
print("name is still:", name)        # unchanged!

# ---------------------------------------------------------------------------
# STEP 5: The same is true for strings with messy spaces.
# ---------------------------------------------------------------------------
messy = "   moon station   "
print("messy (repr shows quotes and spaces):", repr(messy))
print("messy.strip() (outer spaces removed):", repr(messy.strip()))
print("messy.strip().title() (chained):    ", repr(messy.strip().title()))
print("messy is still (untouched):         ", repr(messy))

# ---------------------------------------------------------------------------
# TRY IT
# ---------------------------------------------------------------------------
# 1. Make a string with your own name and call .upper(), .lower(), .title().
# 2. Call .strip() on a string with spaces. Does the original change?
# 3. What does type(42) say? type(3.14)? type(True)? type([1, 2])?
