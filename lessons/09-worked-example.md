# Worked Example: Signal Beacon

Let us trace a small object from creation to a method call.

## 1. Name the object

The class is `SignalBeacon`. Near the bottom, `beacon` becomes one instance of
that class:

`beacon = SignalBeacon("North", 3)`

This particular beacon starts with the label `"North"` and a strength of `3`.

## 2. Find the state

The constructor stores two pieces of state:

`self.label = label`

`self.strength = strength`

`self` means “this particular beacon.” When `beacon` is created, these become
`beacon.label` and `beacon.strength`.

## 3. Trace the method

The `boost` method receives an amount. It adds that amount to this beacon's
strength, then returns a readable report. Because the method changes
`self.strength`, the new value is still there after the method call.

Read the complete example, predict every line, and then run it:

```python
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
```
<!-- expected-output
North
3
North: 5
5
-->

Why does the last line print `5` instead of `3`? Explain which line changed
the object's state and which line returned the report. Then make a prediction
about what would happen if the boost amount were `4`.
