**CS1 — Object-Oriented Programming**

*Student Announcement: Let Your Digital Assistant Help You Learn OOP*

|                |                                                                        |
|----------------|------------------------------------------------------------------------|
| **Date**       | 2026-10-14                                                             |
| **Course**     | CS1 (Computer Science 1)                                               |
| **Instructor** | Jeremy Evert, SWOSU                                                    |
| **Topic**      | Designing a class: class → objects → data → behavior, with an AI tutor |
| **Source**     | Microsoft Copilot conversation, archived as a durable course artifact  |

1\. What We Asked For

The instructor asked for an announcement to share with all students built around four questions:

1.  What is your class?

2.  What is the object or objects?

3.  What is the data you are going to manage?

4.  What is the behavior you want to provide?

The announcement should also tell students to have their digital assistant hold their hand, build the design slowly, and then ask them questions that test their understanding, so they can convince themselves the work is actually helping them learn.

2\. The Announcement (Ready to Share)

📣 Let Your Digital Assistant Help You Learn OOP

This week, I want you to **learn Object-Oriented Programming by building something that belongs in your world**.

Start with four questions:

1\. What is your class?

*What thing in your world deserves to be represented in code?*

Student, Spaceship, SupplyRequest, Monster, BankAccount, Potion, Order, Robot…

2\. What are your objects?

If the class is the **blueprint**, what individual things could you create from it? If the class is Spaceship, perhaps your objects are:

- *The Rust Bucket*

- *Odyssey*

- *Definitely Not Stolen*

Those are individual spaceships made from the same general blueprint.

3\. What data do you need to manage?

What does each object need to **remember about itself**? A spaceship might remember:

- its name

- fuel

- hull strength

- cargo

These become the object’s **attributes**.

4\. What behavior should it provide?

What should your object actually be able to **do**? Maybe our spaceship can:

- fly()

- refuel()

- take_damage()

- load_cargo()

These behaviors become **methods**.

🤖 Now Make Your Digital Assistant Hold Your Hand

**Do not ask the AI to simply do the assignment for you.** Instead, give it this prompt:

> **I am learning Object-Oriented Programming. I want you to act as my tutor, not simply write the solution for me.**
>
> Help me slowly design one class that fits my imaginary world.
>
> Start by asking me:
>
> 1\. What is my class?
>
> 2\. What objects could be created from that class?
>
> 3\. What data should each object manage?
>
> 4\. What behaviors should the objects provide?
>
> Help me turn my answers into a simple Python class, **one small step at a time**. Explain each new piece of code before moving on.
>
> Don’t immediately give me the finished program.
>
> As we work, stop occasionally and ask me questions about what we just built. Ask me to explain things like:
>
> – What is the class?
>
> – What is an object?
>
> – What does self mean here?
>
> – Which pieces are attributes?
>
> – Which pieces are methods?
>
> – What information belongs inside the object?
>
> – What happens when I create two objects from the same class?
>
> – What would I change if I wanted the object to have a new behavior?
>
> If I don’t understand something, slow down and give me another example.
>
> **The goal isn’t for you to prove that you know OOP. The goal is for me to convince myself that I understand what I am building.**

Your Goal

By the end, you shouldn’t just have code that runs. You should be able to point at your program and say:

> **This is my class. These are my objects. This is the data they manage. These are the behaviors they provide. And I can explain why I designed them this way.**

**That’s learning OOP.**

3\. Design Notes for the Instructor

- The original four questions were tightened into a clean progression: class → objects → data → behavior.

- Each question maps to a real Python concept: class = blueprint, object = instance, data = attributes, behavior = methods.

- The Spaceship example fits the course’s imaginary-world metaphors and gives students a concrete model before they invent their own.

- The tutor prompt is reusable as-is: students copy it into any AI assistant (Copilot, ChatGPT, Claude, etc.).

- The prompt gives the assistant explicit permission to slow down, explain, and quiz, so the AI acts as a tutor rather than a code vending machine.

- The closing “point at your program and say…” line is a self-check students can use as an exit ticket.

4\. Student Worksheet: Design Your Class

Fill this in before (or while) you work with your AI tutor. Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1. My class</p>
<p><em>What thing in my world am I modeling?</em></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>2. My objects</p>
<p><em>Name at least two individual things made from this class.</em></p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>3. The data (attributes)</p>
<p><em>What does each object remember about itself?</em></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>4. The behavior (methods)</p>
<p><em>What can each object do?</em></p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>5. My explanation</p>
<p><em>In my own words: why did I design it this way?</em></p></td>
<td></td>
</tr>
</tbody>
</table>

Check Yourself

- I can explain the difference between a class and an object.

- I can point to every attribute in my code and say what it stores.

- I can point to every method in my code and say what it does.

- I can explain what self means in my class.

- I can predict what happens when I create two objects from my class.

- I can describe how I would add one new behavior.
