class SignalBeacon:
    def __init__(self, label, strength):
        self.label = label
        self.strength = strength

    def boost(self, amount):
        self.strength += amount
        return f"{self.label}: {self.strength}"


beacon = SignalBeacon("North", 3)
print(beacon.label)
print(beacon.strength)
print(beacon.boost(2))
print(beacon.strength)
