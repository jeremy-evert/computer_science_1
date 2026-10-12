"""
08_explore_our_own_class.py
===========================
Week 9 -- Objects you use, classes you write.

IDEA OF THIS FILE
-----------------
Close the loop. In files 01-04 we used type(), dir(), help() and __doc__
to explore str. Those tools work on OUR classes in exactly the same way,
because our class is built by the same machinery as str.

We also meet one new exploration tool:

    vars(obj)   -> the instance's own data as a dict

Run it:   python 08_explore_our_own_class.py
"""


class SignalBeacon:
    """A beacon that has a name and a power level, and can transmit.

    This docstring is stored in SignalBeacon.__doc__ and is what
    help(SignalBeacon) displays -- just like str's docs in file 03.
    """

    def __init__(self, name, power=100):
        self.name = name
        self.power = power

    def transmit(self, message):
        """Send a message and spend 10 power. Returns True on success."""
        if self.power < 10:
            return False
        self.power -= 10
        print(f"{self.name} transmitting: {message}")
        return True


beacon = SignalBeacon("Alpha")

# ---------------------------------------------------------------------------
# type() -- what class is this?
# ---------------------------------------------------------------------------
print("=== type ===")
print(type(beacon))
print("isinstance of SignalBeacon?", isinstance(beacon, SignalBeacon))

# ---------------------------------------------------------------------------
# dir() -- what can it do?
# ---------------------------------------------------------------------------
# Look: the same dunder plumbing a str has, plus OUR names.
print()
print("=== dir ===")
print("public names:", [n for n in dir(beacon) if not n.startswith("__")])
print("dunder count:", len([n for n in dir(beacon) if n.startswith("__")]))


# Which names did WE add, compared with a blank class?
class Plain:
    pass


ours = sorted(set(dir(beacon)) - set(dir(Plain())))
print("names we added over a blank class:", ours)
# Note: `name` and `power` appear even though they are not in the class body.
# __init__ creates them on each instance when the instance is built.

# ---------------------------------------------------------------------------
# help() and __doc__ -- how do I use it?
# ---------------------------------------------------------------------------
print()
print("=== __doc__ ===")
print(SignalBeacon.transmit.__doc__)

print()
print("=== help(SignalBeacon.transmit) ===")
help(SignalBeacon.transmit)

# ---------------------------------------------------------------------------
# vars() -- what data does THIS instance hold?
# ---------------------------------------------------------------------------
# dir() lists names from the class AND the instance.
# vars() shows only the instance's own stored data: its STATE.
print()
print("=== vars ===")
print(vars(beacon))

beacon.transmit("Hello")
print(vars(beacon))          # power dropped from 100 to 90

# ---------------------------------------------------------------------------
# Python lets us add attributes on the fly. Convenient, but be careful:
# a typo silently makes a NEW attribute instead of raising an error.
# ---------------------------------------------------------------------------
beacon.colour = "red"
print(vars(beacon))

# ---------------------------------------------------------------------------
# THE FULL PICTURE
# ---------------------------------------------------------------------------
#   Using:   name = "Jeremy"             type(name)    -> str
#   Writing: beacon = SignalBeacon(...)  type(beacon)  -> SignalBeacon
#
#   Both:    dir(), help(), __doc__ explore them.
#            .attribute and .method() use them.
#
# TRY IT
# 1. Write your own class (Pet, Book, Rover ...) with __init__, two
#    instance variables, and two methods, one with a docstring.
# 2. Explore it with type, dir, vars, and help. What did you add?
