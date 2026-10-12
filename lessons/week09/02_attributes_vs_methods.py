"""
02_attributes_vs_methods.py
===========================
Week 9 -- Objects you use, classes you write.

IDEA OF THIS FILE
-----------------
After the dot, an object can give us one of two kinds of things:

    ATTRIBUTE  -- a piece of stored information   (no parentheses)
    METHOD     -- an action we can perform        (parentheses CALL it)

Strings keep their data hidden, so they have no public data attributes.
Python's built-in complex numbers are a nice place to SEE a real
data attribute, so we use one for contrast.

Run it:   python 02_attributes_vs_methods.py
"""

# ---------------------------------------------------------------------------
# PART A: methods on a string
# ---------------------------------------------------------------------------
word = "banana"

# .count("a") is a METHOD: the parentheses run it, "a" is its argument.
print("count of 'a':", word.count("a"))

# .replace(old, new) is a METHOD with TWO arguments.
print("replace a->o:", word.replace("a", "o"))

# .startswith(prefix) is a METHOD that returns a bool (True / False).
print("starts with 'ban':", word.startswith("ban"))

# ---------------------------------------------------------------------------
# PART B: what happens if we forget the parentheses?
# ---------------------------------------------------------------------------
# Without (), we do not run the method. We get the METHOD OBJECT itself.
# Methods are objects too!  This is a very common beginner surprise.
print("forgot parentheses:", word.upper)
print("with parentheses:  ", word.upper())

# ---------------------------------------------------------------------------
# PART C: a real data attribute
# ---------------------------------------------------------------------------
# A complex number stores two pieces of data: .real and .imag.
# They are ATTRIBUTES. No parentheses. Reading them just gives the value.
z = 3 + 4j
print("z:", z)
print("z.real:", z.real)
print("z.imag:", z.imag)

# And complex numbers ALSO have methods:
print("z.conjugate():", z.conjugate())

# ---------------------------------------------------------------------------
# PART D: how to tell them apart in code -> callable()
# ---------------------------------------------------------------------------
# callable(x) answers: "could I put parentheses after x?"
print("is word.upper callable?", callable(word.upper))    # True  -> method
print("is z.real callable?    ", callable(z.real))        # False -> attribute

# ---------------------------------------------------------------------------
# RULE OF THUMB
# ---------------------------------------------------------------------------
#   object.something      -> read stored information   (attribute)
#   object.something()    -> ask the object to DO a thing (method)
#
# TRY IT
# 1. Call .find("n") on "banana". What does it return? What about .find("z")?
# 2. Call .split() on "to be or not to be". What type comes back?
