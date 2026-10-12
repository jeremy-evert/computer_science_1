"""Lesson 05: Building a Dragon Class

Learning goal: Define a small class and initialize one Dragon instance.
Prerequisites: Variables, strings, functions, print(), basic conditionals, and simple Python syntax. Complete lesson 4 first.
Three important ideas:
1. A class defines a kind of object.
2. __init__ initializes an instance.
3. self refers to the instance receiving the method call.
Connection to the previous lesson: Lesson 4 led us from exploring the string class to this next experiment.

Original classroom scenes inspired by Wings of Fire by Tui T. Sutherland.
"""

class Dragon:
    """A dragon on our classroom training roster."""

    def __init__(self, name, tribe):
        self.name = name
        self.tribe = tribe

    def introduce(self):
        return f"Hello! I am {self.name}, a {self.tribe}."


# Predict: Does defining the class alone create a dragon named Clay?
print("\n1. Build one roster member")
clay = Dragon("Clay", "MudWing")
print("Name stored on Clay:", clay.name)
print("Tribe stored on Clay:", clay.tribe)
print("Dragon is the class definition; Dragon(...) creates an instance.")
print("__init__ initializes that instance with name and tribe data.")
print("self refers to the instance being initialized or receiving a method call.")

# Predict: Will introduce() print by itself, or return text for print()?
print("\n2. Give our object behavior")
message = clay.introduce()
print(message)
print("introduce() returns text; print(message) displays that text.")
print("name and tribe are data attributes. introduce is a method.")

# Predict: What do these two dot calls have in common?
print("\n3. Connect our discovery to strings")
print('"Clay".upper():', "Clay".upper())
print("clay.introduce():", clay.introduce())
print("Both calls access behavior through an object, then return a string.")
print("Now that we have a Dragon class, can we create different dragons?")
