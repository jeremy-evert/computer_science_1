"""Lesson 07: Making Objects Discoverable

Learning goal: Make Dragon objects easy for another programmer to explore.
Prerequisites: Variables, strings, functions, print(), basic conditionals, and simple Python syntax. Complete lesson 6 first.
Three important ideas:
1. Docstrings explain the interface.
2. __str__ supplies readable text and __repr__ developer text.
3. Discoverable objects use clear names and documented behavior.
Connection to the previous lesson: Lesson 6 led us from creating dragon objects to this next experiment.

Original classroom scenes inspired by Wings of Fire by Tui T. Sutherland.
"""

class Dragon:
    """A classroom training-roster dragon with a name, tribe, and energy.

    Each dragon starts with three energy points. train() spends one point
    when energy is available. These training rules are invented for the lab.
    """

    def __init__(self, name: str, tribe: str):
        """Initialize this dragon's name, tribe, and three energy points."""
        self.name = name
        self.tribe = tribe
        self.energy = 3

    def introduce(self) -> str:
        """Return a friendly introduction without changing this dragon."""
        return f"Hello! I am {self.name}, a {self.tribe}."

    def train(self) -> int:
        """Spend one energy point if available; return the remaining energy."""
        if self.energy > 0:
            self.energy = self.energy - 1
        return self.energy

    def __str__(self) -> str:
        """Return readable roster text for people."""
        return f"{self.name} the {self.tribe} (energy: {self.energy})"

    def __repr__(self) -> str:
        """Return developer text showing this dragon's current data."""
        return (f"Dragon(name={self.name!r}, tribe={self.tribe!r}, "
                f"energy={self.energy!r})")


# Predict: Will print(clay) and repr(clay) show the same text?
print("\n1. Give the roster a readable voice")
clay = Dragon("Clay", "MudWing")
print(clay)
print("Developer representation:", repr(clay))
print("__str__ supplies readable text; __repr__ supplies useful developer text.")
print("Our repr shows state; it is not promised to be an executable constructor call.")

# Predict: Will all names returned by dir(clay) be methods?
print("\n2. Starflight writes a discovery note for Sunny")
public_names = [name for name in dir(clay) if not name.startswith("_")]
print("Public attributes:", public_names)
public_methods = [name for name in public_names if callable(getattr(clay, name))]
print("Public methods:", public_methods)
print("Has energy?", hasattr(clay, "energy"))
print("Is energy callable?", callable(getattr(clay, "energy")))
print("Has introduce?", hasattr(clay, "introduce"))
method = getattr(clay, "introduce")
print("Is introduce callable?", callable(method))
print("Try the discovered method:", method())
print("For this simple class, getattr safely retrieves these known public attributes.")

# Predict: What can help() explain that dir() cannot?
print("\n3. Leave useful documentation")
print("Class documentation:", Dragon.__doc__)
print("Initialization documentation:", Dragon.__init__.__doc__)
print("Introduction documentation:", Dragon.introduce.__doc__)
print("Training documentation:", Dragon.train.__doc__)
print("In the shell, try help(Dragon) and help(Dragon.introduce).")
print("Type hints describe intended types; Python does not enforce them here.")
print("We now explore Dragon with the same tools we used for the built-in str class.")
print("Clear names and docstrings make discovery part of good software design.")
print("From a string object to our own objects: what will you build next?")
