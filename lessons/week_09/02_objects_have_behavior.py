"""Lesson 02: Objects Have Behavior

Learning goal: Use string behavior and separate returned values from changes to data.
Prerequisites: Variables, strings, functions, print(), basic conditionals, and simple Python syntax. Complete lesson 1 first.
Three important ideas:
1. Methods are accessed through objects.
2. A returned value does not reassign a variable.
3. Strings are immutable; reassignment changes a reference.
Connection to the previous lesson: Lesson 1 led us from strings are objects to this next experiment.

Original classroom scenes inspired by Wings of Fire by Tui T. Sutherland.
"""

dragon_name = "Clay"

# Predict: Will upper() change the name stored in dragon_name?
print("\n1. Sunny tries a loud announcement")
print("Returned by upper():", dragon_name.upper())
print("Original afterward:", dragon_name)
print("Returned by lower():", dragon_name.lower())
print("Returned by replace():", dragon_name.replace("Clay", "Sunny"))
print("Original still:", dragon_name)
print("These methods return strings; the calls do not reassign dragon_name.")

# Predict: Do all methods return strings?
print("\n2. Questions about the roster entry")
print("Starts with C?", dragon_name.startswith("C"))
print("Number of a characters:", dragon_name.count("a"))
print("Length:", len(dragon_name))
print("object.method(arguments): upper() is a method; len(object) calls a function.")
print("Methods are functions accessed through objects; their results can have different types.")

# Predict: What will each variable show after reassignment?
print("\n3. Keep the old name, then reassign")
original_name = dragon_name
# Strings cannot have their existing contents changed: they are immutable.
dragon_name = dragon_name.upper()
print("Reassigned dragon_name:", dragon_name)
print("original_name still refers to:", original_name)
print("We assigned the returned string; we did not modify the original string.")
print("How do we discover methods without somebody telling us their names?")
