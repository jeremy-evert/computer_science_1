"""
06_our_first_class.py
=====================
Week 9 -- Objects you use, classes you write.

IDEA OF THIS FILE
-----------------
Time to write a class. We build a SignalBeacon: a tiny object that has
a name (DATA) and can transmit (BEHAVIOR).

The new pieces of vocabulary:

    class         -- keyword that defines a new blueprint
    __init__      -- special method that runs when an instance is created
    self          -- "this particular instance"
    self.name     -- an INSTANCE VARIABLE: data stored on that instance

Run it:   python 06_our_first_class.py
"""


# ---------------------------------------------------------------------------
# THE CLASS DEFINITION
# ---------------------------------------------------------------------------
# By convention, class names use CapitalizedWords (str, list, int are old
# built-ins that break this habit; yours should follow it).
class SignalBeacon:
    """A beacon that has a name and can transmit a signal."""

    # __init__ is the INITIALIZER. Python calls it automatically, right
    # after it builds a new empty instance. Its job: set up the data.
    #
    # `self` is the first parameter of EVERY method. Python passes it
    # for us: it is the instance the method is being called on.
    # `name` is a normal parameter -- we supply it when we create the beacon.
    def __init__(self, name):
        # self.name = name   -> store the value ON this instance.
        # The left side, self.name, is the instance variable (an attribute).
        # The right side, name, is the parameter that was passed in.
        self.name = name

    # A METHOD is just a function defined inside a class.
    # It uses `self` to reach the data that belongs to this instance.
    def transmit(self):
        print(f"{self.name} transmitting signal.")


# ---------------------------------------------------------------------------
# MAKING AN INSTANCE
# ---------------------------------------------------------------------------
# SignalBeacon("Alpha") does three things:
#   1. builds a new, empty SignalBeacon object
#   2. calls __init__(that_object, "Alpha")  <- self is filled in for us
#   3. returns the finished object, which `beacon` now refers to
beacon = SignalBeacon("Alpha")

# ---------------------------------------------------------------------------
# USING IT -- exactly like the str and list objects we already know
# ---------------------------------------------------------------------------
beacon.transmit()                       # method call: parentheses
print("name attribute:", beacon.name)   # attribute read: no parentheses
print("type:", type(beacon))            # <class '__main__.SignalBeacon'>

# `beacon.transmit()` is shorthand for `SignalBeacon.transmit(beacon)`.
# This reveals what `self` really is: the object before the dot.
SignalBeacon.transmit(beacon)

# ---------------------------------------------------------------------------
# THE CONNECTION
# ---------------------------------------------------------------------------
#   str          is a class.      "Jeremy"   is an object.
#   list         is a class.      [1, 2, 3]  is an object.
#   SignalBeacon is a class.      beacon     is an object.
#
# Python lets us write classes just like the ones we have been using.
#
# TRY IT
# 1. Create a second beacon named "Bravo" and call transmit() on it.
# 2. Add a method called describe() that prints "Beacon <name> is online."
# 3. What error do you get if you write def transmit(): with no self?
