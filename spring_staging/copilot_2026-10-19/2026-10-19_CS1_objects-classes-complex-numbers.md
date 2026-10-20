**A durable CS1 conversation artifact \| Week 9 \| October 19, 2026**

*Course context: COMSC-1033, Fall 2026*

# Purpose

This artifact preserves and organizes a conversation about the Week 9 transition from using built-in Python objects to writing first classes. It also captures a short Claude Code installation troubleshooting exchange and develops complex numbers, AC electricity, and power as a concrete example of attributes and methods.

# 1. Week 9 Course Context

Week 9 is framed as an evolution: students move from familiar objects such as strings and lists to a first small class. The planned sequence is:

- Monday: use familiar string and list objects, then compare methods with attributes.

- Wednesday: write a first small class with \_\_init\_\_, state, self, and one method.

- Friday: no class because of Fall Break.

The active gate is Reasoning Odyssey Checkpoint 2, one graded submission worth 25 points: 15 points for the working result and 10 points for process. Students provide a working extension, an explanation, run evidence, and a reflection. A custom class is optional, not required.

# 2. Condensed Prompt for the Lesson

Full compact version:

> We already use objects like strings and lists every day. Show us how strings are objects, how to explore them with type(), dir(), and help(), and then guide us through creating our own class with \_\_init\_\_, instance variables, self, and methods. Help us connect “objects we use” to “classes we write.”

Ultra-condensed version:

> How are strings objects? How can we inspect them? How do we create our own class and object? Show us the path from using objects to writing them.

# 3. Suggested Learning Path

1.  Strings are objects: inspect type(name) and use methods such as upper(), lower(), and strip().

2.  Explore an object with type(), dir(), help(), and \_\_doc\_\_.

3.  Recognize that students have already created instances, even before writing a class.

name = "Jeremy"  
items = \["flour", "bandages"\]

4.  Create a first class with state and behavior.

class SignalBeacon:  
def \_\_init\_\_(self, name):  
self.name = name  
  
def transmit(self):  
print(f"{self.name} transmitting signal.")

5.  Create and use an instance.

beacon = SignalBeacon("Alpha")  
beacon.transmit()

6.  Make the connection: str, list, and SignalBeacon are classes; specific strings, lists, and beacons are objects.

> Week 1-8: We used objects. Week 9: We discover those objects came from classes. Week 9+: We start writing classes of our own.

# 4. Claude Code Installation Troubleshooting

The repository was clean and synchronized, but PowerShell reported that claude was not recognized. That message indicates the command was not available in the current shell, commonly because Claude Code is not installed or its install directory is not yet on PATH.

git status  
\# On branch main  
\# Your branch is up to date with 'origin/main'.  
\# nothing to commit, working tree clean

Copy-and-run installation and verification block:

winget --version  
winget search Claude  
winget install -e --id Anthropic.ClaudeCode  
claude --version  
where.exe claude

If installation succeeds but the command remains unavailable, close PowerShell completely, open a new terminal, and run claude --version again so the new session reloads PATH.

# 5. Complex Numbers as Python Objects

A Python complex number stores two pieces of data: a real component and an imaginary component. Python exposes them as attributes, so they are read without parentheses. The object also provides behavior through methods, which are called with parentheses.

z = 3 + 4j  
print("z:", z)  
print("z.real:", z.real)  
print("z.imag:", z.imag)  
print("z.conjugate():", z.conjugate())

Here, z.real and z.imag are attributes. The expression z.conjugate() calls a method and returns 3 - 4j.

# 6. Imaginary Numbers, Electronics, and Power

## Why engineers use j

In mathematics, the imaginary unit is usually written i, where i² = -1. Electrical engineering normally uses j because i is already widely used for electric current. Therefore, 3 + 4j contains a real part of 3 and an imaginary part of 4.

## AC electricity adds phase

Direct-current quantities can be steady. Alternating-current voltage and current vary as waves, and their peaks may not occur at the same time. That timing offset is phase. Complex numbers conveniently package a magnitude-like pair of components that can represent both size and phase relationships.

A useful physical picture is two people pushing a merry-go-round. One pushes at the ideal moment; the other pushes later. Both apply force, but their timing differs. In an AC circuit, voltage and current can similarly lead or lag one another.

## Real, reactive, and apparent power

- Real power, P, performs net work and is measured in watts (W).

- Reactive power, Q, represents energy exchanged with electric or magnetic fields and is measured in volt-amperes reactive (VAR).

- Complex power, S, combines them: S = P + jQ. Its magnitude is apparent power and is measured in volt-amperes (VA).

power = 1000 + 500j  
print("real power:", power.real, "W")  
print("reactive power:", power.imag, "VAR")  
print("apparent power magnitude:", abs(power), "VA")

For this example, the object stores 1000 W as its real component and 500 VAR as its imaginary component. Python’s abs(power) computes the magnitude: approximately 1118 VA.

## Why the conjugate matters

Conjugation reverses the sign of the imaginary component. For z = 3 + 4j, the conjugate is 3 - 4j. In AC analysis, complex conjugates are especially useful in power calculations. A common relationship is complex power S = V × I\*, where I\* is the complex conjugate of current. The conjugate gives the phase relationship the correct sign when combining voltage and current.

# 7. The OOP Teaching Connection

The complex-number example makes the attributes-versus-methods distinction visible:

- z.real: stored data, accessed as an attribute.

- z.imag: stored data, accessed as an attribute.

- z.conjugate(): behavior supplied by the complex class, invoked as a method.

The same pattern appears throughout Python:

name.upper() \# method on a string object  
items.append("flour") \# method on a list object  
z.conjugate() \# method on a complex object  
  
name.real \# not a string attribute  
z.real \# valid complex-number attribute

> Python’s authors wrote the str, list, and complex classes. Students have been creating and using their objects all semester. Week 9 is when students begin writing classes of their own.

# 8. Classroom-Ready Exploration

A short predict-test-observe sequence:

z = 3 + 4j  
  
print(type(z))  
print(z.real)  
print(z.imag)  
print(z.conjugate())  
print(abs(z))  
  
print(dir(z))  
help(z.conjugate)

7.  Predict the output of real, imag, conjugate(), and abs(z).

8.  Run the code and compare the prediction with the evidence.

9.  Use dir(z) to locate available attributes and methods.

10. Use help(z.conjugate) to investigate one method.

11. Explain why real has no parentheses but conjugate() does.

# Key Takeaway

> An object combines state and behavior. Complex numbers make that concrete: .real and .imag expose state, while .conjugate() supplies behavior. Once students recognize that familiar values already come from classes, writing a first class becomes an extension of what they already know rather than a completely new world.
