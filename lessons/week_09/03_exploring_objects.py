"""Lesson 03: Exploring Objects

Learning goal: Find, inspect, and try an object’s public attributes.
Prerequisites: Variables, strings, functions, print(), basic conditionals, and simple Python syntax. Complete lesson 2 first.
Three important ideas:
1. dir lists names, not explanations.
2. help and experiments supply evidence.
3. An attribute is not necessarily callable.
Connection to the previous lesson: Lesson 2 led us from objects have behavior to this next experiment.

Original classroom scenes inspired by Wings of Fire by Tui T. Sutherland.
"""

dragon_name = "Clay"

# Predict: Does dir() tell us how to use each name?
print("\n1. Starflight searches for clues")
all_names = dir(dragon_name)
public_names = [name for name in dir(dragon_name) if not name.startswith("_")]
print("Total names found:", len(all_names))
print("A small public sample:", public_names[:8])
print("upper listed?", "upper" in all_names)
print("The filter hides underscore names to reduce clutter, not their importance.")

# Predict: Is an attribute retrieved by getattr() already a result?
print("\n2. Find a name, retrieve its value, then try it")
print("Has upper?", hasattr(dragon_name, "upper"))
print("Has breathe_fire?", hasattr(dragon_name, "breathe_fire"))
upper_method = getattr(dragon_name, "upper")
print("Is the retrieved attribute callable?", callable(upper_method))
print("Call it:", upper_method())
print("Is the name string callable?", callable(dragon_name))
print("getattr retrieved the method; () called it and produced a result.")

# Predict: What extra evidence can documentation give us?
print("\n3. Inspect before experimenting")
print("upper documentation:", str.upper.__doc__)
print("First line of replace documentation:", str.replace.__doc__.splitlines()[0])
print('replace experiment:', dragon_name.replace("a", "o"))
print("In the Python shell, try help(str.upper) and help(str.replace).")
print("dir is a useful list, not a guarantee of every possible attribute.")
print("hasattr tests access to a name, not whether it is callable or suitable.")
print("How do we inspect a name? Read help, then try a small experiment.")
print("If these methods belong to a string, where are they defined?")
