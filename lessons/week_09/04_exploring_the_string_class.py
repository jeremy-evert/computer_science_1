"""Lesson 04: Exploring the String Class

Learning goal: Connect a string instance to the built-in str class.
Prerequisites: Variables, strings, functions, print(), basic conditionals, and simple Python syntax. Complete lesson 3 first.
Three important ideas:
1. An instance has a class.
2. A class supplies shared behavior.
3. The public interface is not the implementation.
Connection to the previous lesson: Lesson 3 led us from exploring objects to this next experiment.

Original classroom scenes inspired by Wings of Fire by Tui T. Sutherland.
"""

# Predict: What kind of object is the roster entry "Glory"?
print("\n1. Glory examines the class behind her name")
print("The built-in class:", str)
print("Type of the string:", type("Glory"))
print("A str instance?", isinstance("Glory", str))
print("upper appears on the class?", "upper" in dir(str))
print("The class attribute str.upper:", str.upper)
print("A class defines a kind of object; an instance is an object of that kind.")

# Predict: Will these two calls return the same text?
print("\n2. Two routes to string behavior")
print("Through the class:", str.upper("Glory"))
print("Through the instance:", "Glory".upper())
print("Also available to Clay:", "Clay".upper())
print("For this str method, the class call explicitly supplies the string.")
print("The instance call supplies it through the object before the dot.")
print("Do not assume every Python method supports these exact call forms.")

# Predict: Does a list of names show how str was implemented?
print("\n3. Inspect the public interface")
public_names = [name for name in dir(str) if not name.startswith("_")]
print("A small class attribute sample:", public_names[:8])
print("First line of class documentation:", str.__doc__.splitlines()[0])
print("In the shell, use help(str) to explore the full class documentation.")
print("Attributes are named things accessed through an object or class.")
print("Methods are callable behavior; not every attribute is a method.")
print("We are examining str's public interface, not reading its implementation.")
print("If Python has a class for strings, can we make a class for dragons?")
