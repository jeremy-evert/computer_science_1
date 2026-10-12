"""Lesson 06: Creating Dragon Objects

Learning goal: Compare independent instance data with shared class behavior.
Prerequisites: Variables, strings, functions, print(), basic conditionals, and simple Python syntax. Complete lesson 5 first.
Three important ideas:
1. Each instance stores its own data.
2. Instances share methods defined by their class.
3. Dragon state can change while string contents cannot.
Connection to the previous lesson: Lesson 5 led us from building a dragon class to this next experiment.

Original classroom scenes inspired by Wings of Fire by Tui T. Sutherland.
"""

class Dragon:
    """A dragon with an independent energy supply for classroom training."""

    def __init__(self, name, tribe):
        self.name = name
        self.tribe = tribe
        self.energy = 3

    def introduce(self):
        return f"Hello! I am {self.name}, a {self.tribe}."

    def train(self):
        if self.energy > 0:
            self.energy = self.energy - 1
        return self.energy


# Predict: Do instances of the same class need to have the same name?
print("\n1. Three dragons join the roster")
clay = Dragon("Clay", "MudWing")
tsunami = Dragon("Tsunami", "SeaWing")
glory = Dragon("Glory", "RainWing")
print(clay.introduce())
print(tsunami.introduce())
print(glory.introduce())
print("Clay's attributes:", clay.name, clay.tribe)
print("Tsunami's attributes:", tsunami.name, tsunami.tribe)
print("Each instance stores its own data and uses methods defined by Dragon.")

# Predict: Will their classes match? Will their identities match?
print("\n2. Same kind, different objects")
print("Clay's type:", type(clay))
print("Tsunami's type:", type(tsunami))
print("Clay is a Dragon?", isinstance(clay, Dragon))
print("Same class?", type(clay) is type(tsunami))
print("Clay's identity:", id(clay))
print("Tsunami's identity:", id(tsunami))
print("Same identity?", id(clay) == id(tsunami))
print("These objects live at the same time, so their identities are distinct.")

# Predict: Will training Clay also use Tsunami's energy?
print("\n3. Clay practices; Tsunami watches")
print("Before: Clay", clay.energy, "Tsunami", tsunami.energy)
print("Clay's train() returns:", clay.train())
print("After:  Clay", clay.energy, "Tsunami", tsunami.energy)
print("train() assigns a new energy value on this instance: its state changes.")
print("The integers themselves are not mutated; Clay's energy attribute changes.")
print("Energy is a classroom rule, not a claim about the books.")

# Predict: Does upper() change the name attribute?
print("\n4. Mutable dragon, immutable string")
print("Uppercase result:", clay.name.upper())
print("Name afterward:", clay.name)
print("Dragon state can change; the string's existing contents cannot.")
print("How can another programmer discover what our Dragon objects can do?")
