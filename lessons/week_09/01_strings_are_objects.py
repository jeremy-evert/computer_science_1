"""Lesson 01: Strings Are Objects

Learning goal: Discover the object behind a familiar string variable.
Prerequisites: Variables, strings, functions, print(), basic conditionals, and simple Python syntax.
Three important ideas:
1. A variable refers to an object.
2. str is the class of string objects.
3. id identifies an object during its lifetime.
Connection to the previous lesson: Begin with the familiar string "Clay".

Original classroom scenes inspired by Wings of Fire by Tui T. Sutherland.
"""

dragon_name = "Clay"

# Predict: Will the variable print differently from the literal "Clay"?
print("\n1. A name on the training roster")
print(dragon_name)
print("Variable's type:", type(dragon_name))
print("Literal's type:", type("Clay"))
print("Same type?", type("Clay") is type(dragon_name))
print("A string instance?", isinstance(dragon_name, str))
print('"Clay" is a string object; dragon_name refers to it. Its class is str.')

# Predict: Can you predict the exact number printed by id()?
print("\n2. Identity during an object's lifetime")
print("Object identity:", id(dragon_name))
print("Identity again:", id(dragon_name))
print("The identity stays the same while this object lives; the number can vary by run.")
print("If Clay is an object, what can Clay do?")
