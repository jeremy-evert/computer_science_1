"""
07_state_and_methods.py
=======================
Week 9 -- Objects you use, classes you write.

IDEA OF THIS FILE
-----------------
An object is STATE (data) + BEHAVIOR (methods). In file 06 our beacon had
state, but nothing ever changed it. Here we add:

    - more instance variables (self.power, self.messages)
    - methods that CHANGE state (unlike str methods, which return new values)
    - methods that RETURN values
    - several instances, each with its OWN independent state
    - __str__, so print(beacon) is readable

Run it:   python 07_state_and_methods.py
"""


class SignalBeacon:
    """A beacon with a name, a power level, and a log of what it sent."""

    def __init__(self, name, power=100):
        # `power=100` is a DEFAULT argument: optional when creating a beacon.
        self.name = name
        self.power = power
        self.messages = []        # every beacon gets its OWN fresh list

    # -- a method that CHANGES state ---------------------------------------
    def transmit(self, message):
        # Guard: no power, no signal. We return early and change nothing.
        if self.power < 10:
            print(f"{self.name}: not enough power to transmit.")
            return False

        self.power -= 10                  # transmitting costs power
        self.messages.append(message)     # remember what was sent
        print(f"{self.name} transmitting: {message}")
        return True

    # -- a method that CHANGES state the other direction -------------------
    def recharge(self, amount):
        self.power = min(100, self.power + amount)   # cap at 100

    # -- a method that only READS state and returns it ---------------------
    def message_count(self):
        return len(self.messages)

    # -- __str__ : what print(beacon) and str(beacon) show -----------------
    # Same idea as the dunder methods we saw on str in file 04: Python
    # calls beacon.__str__() for us when it needs text for this object.
    def __str__(self):
        return f"Beacon {self.name} (power {self.power}, sent {self.message_count()})"


# ---------------------------------------------------------------------------
# Two instances. Same class, separate state.
# ---------------------------------------------------------------------------
alpha = SignalBeacon("Alpha")
bravo = SignalBeacon("Bravo", power=30)      # override the default

print("alpha at start:", alpha)
print("bravo at start:", bravo)
print()

alpha.transmit("Hello")
alpha.transmit("Anyone there?")
bravo.transmit("Low battery")
bravo.transmit("Still low")
bravo.transmit("Fading")
bravo.transmit("Last one")                   # power 30 -> 0 after three sends

print()
print("alpha after sends:", alpha)
print("bravo after sends:", bravo)            # alpha is untouched by bravo

bravo.recharge(50)
print("after recharge:", bravo)

print()
print("alpha messages:", alpha.messages)
print("bravo messages:", bravo.messages)

# ---------------------------------------------------------------------------
# COMPARE WITH STRINGS
# ---------------------------------------------------------------------------
#   "hi".upper()      -> returns a NEW string, original unchanged (immutable)
#   alpha.transmit()  -> CHANGES alpha's own state (mutable)
#   [1].append(2)     -> a list is mutable too: it changes itself
# Our class is more like a list than a string. We decide the rules.
#
# TRY IT
# 1. Add a method reset() that empties messages and restores power to 100.
# 2. What happens if two beacons shared ONE list? Try changing __init__ to
#    take a default argument  messages=[]  -- then search for "mutable
#    default argument" to find out why that is a famous bug.
