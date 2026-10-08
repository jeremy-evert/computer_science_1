---
schema: concept-pipeline/v1
id: week-09-concept-1-objects-you-already-use
title: Objects You Already Use
course: COMSC-1033 Computer Science I
week: 9
objectives:
  - Describe a value as an object with a type, state, and behaviors.
  - Read dot notation for string and list methods.
  - Distinguish a string method that returns a new value from a list method that mutates in place.
  - Use type, dir, and help to investigate an unfamiliar object.
canvas:
  overview_page: /courses/comsc-1033/pages/week-09-concept-1-objects-you-already-use
sources:
  - id: S1
    url: https://github.com/jeremy-evert/computer_science_1/blob/main/planning/2026-10-05_strings_are_objects_lesson_map.md
    accessed: '2026-10-08'
  - id: S2
    url: https://github.com/jeremy-evert/computer_science_1/blob/main/lessons/06-strings.md
    accessed: '2026-10-08'
  - id: S3
    url: https://github.com/jeremy-evert/computer_science_1/blob/main/lessons/08-classes-and-modules.md
    accessed: '2026-10-08'
  - id: S4
    url: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
    accessed: '2026-10-08'
  - id: S5
    url: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    accessed: '2026-10-08'
---

## Claims

| id | claim | kind | checked_by | source |
| --- | --- | --- | --- | --- |
| C1 | A Python value is an object with a type, a current value or state, and behaviors supplied by its type. | model | doc citation: S2, “A first object model” | S2 |
| C2 | A string is an object of type str, and dot notation selects a named attribute; parentheses call it when that attribute is a method. | explanation | doc citation: S2, “The dot” and “A first object model” | S2 |
| C3 | String methods such as upper, strip, and replace return a new string, and strings are immutable, so the original string is not changed in place. | fact | doc citation: S2, “Immutability”; S4, “Text Sequence Type” and “String Methods” | S4 |
| C4 | The split method on a string returns a list of pieces rather than a string. | fact | code run: worked example string-new-value; doc citation: S2, “String Laboratory” | S2 |
| C5 | A list is a mutable sequence, and methods such as append, extend, remove, and reverse change the list in place. | fact | doc citation: S4, “Mutable Sequence Types” and “Lists”; S5, “Methods of List Objects” | S4 |
| C6 | A list mutation method such as append returns None while changing the list. | fact | code run: worked example list-in-place; doc citation: S4, “Mutable Sequence Types” | S4 |
| C7 | dir lists attribute names and help on a type or method provides focused documentation for investigation. | practice | doc citation: S2, “Discovering behavior rather than memorizing it” | S2 |
| C8 | A method can return a value that you save and use, or can mutate its receiver; the method’s type and documentation determine which behavior occurs. | principle | code run: worked examples string-new-value and list-in-place; doc citation: S2, “Immutability” and S4, “Mutable Sequence Types” | S2 |

## Script

<!-- slide id="terra" title="Start with a value" claims="C1" -->
Let’s begin on familiar ground: a name, a message, or a list of places. Each one is a value in a Python program. Now widen the question. Do not ask only what the value is called. Ask what kind of thing it is, what information it currently holds, and what it knows how to do. That three-part question is our object model. A value has a type. Its current text or items are its state. Its type supplies behaviors, including methods. A string is therefore more than characters sitting in a variable. A list is more than several values between brackets. Both are objects that Python can work with according to their types. This is not yet a lesson about writing your own class. It is a way to look at values you already use. The name on the left is a reference we use to reach an object; the name itself is not the type. Two different strings can have different text and still have the same type. As we travel from Terra, the familiar world, toward Luna, keep asking: what kind of object is this, what state does it hold, and what behavior can it offer?

<!-- slide id="luna-dot" title="Follow the dot" claims="C2" -->
The next clue is a dot. When you see a value followed by a dot and a name, Python is looking up something attached to that object. When the name identifies a method, parentheses call that method. In spoken language, you can hear it as: ask this object to use this behavior. A string can be asked to become uppercase, remove outside spaces, or replace one piece of text. The parentheses matter because they perform the call; without them, you are referring to the method itself rather than asking it to run. Not every name after a dot is a method. Some are attributes that hold information. Today we are concentrating on methods, because they make behavior visible. The dot is not decoration and it is not a universal command. It is a route from an object to a named part of what that object offers. This is why methods feel as though they belong to the string: the string’s type supplies them. Pause and translate a line like “message dot upper with parentheses” into ordinary language: ask the message object for its uppercase behavior and call it. That translation will help you read programs before you can write every line yourself.
<!-- show: code example="string-new-value" -->

<!-- slide id="luna-return" title="A string method gives back a value" claims="C3,C4,C8" -->
Strings give us a useful surprise. A string method such as uppercase does not edit the original string in place. Strings are immutable, which means their contents cannot be changed in place. The method gives back another string. If you call the method and throw away its result, the original reference still leads to the original text. If you assign the result back to the same variable, that variable now refers to the new string. The important habit is to ask what came back. Some string methods return another string. The split method returns a list of pieces. Search methods can return numbers, and checks can return true or false. A method call is not automatically an instruction that changes the object you started with. It may be a computation that produces a new value. This distinction explains a common beginner error: saying that an uppercase call changes the string, then being surprised when printing the string shows the old text. Nothing mysterious happened. The call produced a result, and no one saved it. If you do save it, you have not repaired the old string; you have made your variable refer to the returned string. Think of a string method as sending a request to a text object and receiving a new piece of text in reply.
<!-- show: code example="string-new-value" -->

<!-- slide id="luna-list" title="A list can change in place" claims="C5,C6,C8" -->
Now compare a list. Lists are also objects, but a list is a mutable sequence. Mutable means the list can be changed in place. A method such as append adds an item to the existing list. The list after the call contains the new item. The return value is a different question: append returns None. That is why the useful result is usually the changed list, not a new list stored from append. The same pattern appears with other list methods that add, remove, or rearrange items. They act on the list itself. This is a place where type matters. The string method upper gives back a new string because strings are immutable. The list method append changes a mutable list. Neither behavior is the definition of all methods. It is a property you check for the particular type and method. A safe routine is: predict the object’s state before the call, predict whether the call returns a value, run it, and inspect both. If you assign the result of append to a variable, that variable holds None while the original list has changed. The list and the returned value are two separate things to keep track of.
<!-- show: code example="list-in-place" -->

<!-- slide id="sol-check" title="Use the return value as evidence" claims="C3,C4,C5,C6" -->
Let’s make the contrast concrete. With a string, call the method and print both the returned value and the original. You will see two different strings: the new uppercase text and the old lowercase text. With a list, call append, keep the returned value, and then print both. You will see None in the saved result and the added item in the original list. That pair of observations is more useful than memorizing a slogan such as strings return and lists mutate. It teaches a question: what does this method return, and does it change its receiver? The word receiver simply means the object before the dot, the object receiving the request. The answer comes from the type’s rules and the method’s documentation. A string can also return a list from split, so even a method on an immutable object may return a different type. A list can have methods such as copy that return a list, and it also has methods that change the list. Types set the menu of behaviors, but individual methods determine the details. Use the examples as tiny experiments. Predict first. Run second. Explain the printed lines in plain language. That loop turns an accidental result into object knowledge.
<!-- show: code example="string-new-value" -->
<!-- show: code example="list-in-place" -->

<!-- slide id="sol-discover" title="Ask Python what is available" claims="C7" -->
You do not need to memorize every method. Python can help you investigate. Type asks what kind of object you have. Dir lists names of attributes and methods available on that object. It is a menu, not a promise that every name is a method or that every method takes the same arguments. Help gives more focused documentation about a type or a method. A practical loop is: identify the type, look through the available names, ask for help on a promising method, predict a small result, and run a tiny experiment. Start with a familiar object such as a string or list, then try the same investigation on something new. If you see a method name in the list, read its help before guessing what it changes or returns. This is a professional programming habit. The goal is not to know the whole library in your head. The goal is to know how to ask a good question of the language and then test the answer. Documentation and experiments work together: documentation tells you the contract, while a small run helps you connect that contract to a value you can see.
<!-- show: code example="discover" -->

<!-- slide id="sol-circuit" title="Carry the object question forward" claims="C1,C2,C5,C7,C8" -->
The circuit is complete. On Terra, we met values we already use. On Luna, we followed the dot and compared what string and list methods do. At Sol, the bright center is a reusable habit: when Python gives you a thing, ask what type it has, what state it holds, what behavior it offers, what it returns, and whether it changes in place. Strings and lists are not merely containers for syntax practice. They are early examples of a much larger way to organize software. Later, objects may represent files, paths, game entities, or connections. The exact methods will come from their types and documentation, so do not assume that a conceptual example is a real API. For today, keep the contrast sharp. Uppercase on a string returns new text, and the old string remains unchanged unless you save the new result. Append on a list changes the list and returns None. Dir and help make unfamiliar behavior discoverable. If you can explain those observations, you already have a working first model of objects. The next time a method surprises you, do not guess that all objects behave like strings or all methods behave like append. Identify the type, read the method’s contract, and run the smallest useful check.

## Podcast

**DANA:** I thought an object was something we had to create with a class. But this lesson says I have already been using objects. What exactly counts as an object here?

**MARCUS:** A value Python can work with is an object. For this lesson, use three questions. What type of thing is it? What value or state does it currently hold? What behaviors does its type make available? A string such as a message is an object, and a list of places is an object. You do not need to write a new class before you can think this way.

**DANA:** So the variable name is not the object’s type?

**MARCUS:** Right. A variable name is a reference we use to reach a value. The type describes the kind of object. Two variables can refer to strings with different text, but both objects still have the string type. Their current text is the useful state we can observe. Their type supplies behaviors such as changing case, removing outside spaces, or splitting text.

**DANA:** The behavior part is where the dot comes in, I think. When I read a string followed by a dot and a method name, what should I hear in my head?

**MARCUS:** Hear a request. Ask the object to use a named behavior. The dot looks up a name attached to the object. If that name is a method, the parentheses call it. Saying “message dot upper with parentheses” is a spoken way to say “ask the message object for its uppercase behavior and call it.” The parentheses are what make the call happen.

**DANA:** And if I leave off the parentheses, I am not actually asking it to run?

**MARCUS:** Correct. Without the parentheses, you are referring to the method itself. Also remember that not every name after a dot is a method. A dot can reach an attribute holding information. For this first model, focus on the common pattern of an object, a dot, a method name, and a call. The type tells you which names make sense for that object.

**DANA:** Last week’s strings lesson showed an uppercase method. I used the call, printed my string, and it looked unchanged. I assumed the method had failed.

**MARCUS:** That is the classic misconception. String objects are immutable. Their contents cannot be changed in place. The uppercase method returns a new string. If you call it and discard the returned value, your original variable still refers to the original text. If you assign the returned value back to the variable, the variable now refers to the new uppercase string.

**DANA:** So the call did work, but I did not keep the answer?

**MARCUS:** Exactly. Think of the method as a request that sends back a result. The old string is not edited. This is why it helps to print both values. One print can show the returned uppercase string, and another can show that the original lowercase string remains. Saving the result gives your variable a new reference; it does not alter the old string.

**DANA:** Does every string method return another string?

**MARCUS:** No. That is another useful caution. Uppercase, strip, and replace return strings. Split returns a list of pieces. Search methods can return numbers, and checks can return true or false. A method belongs to the string object, but its result can have a different type. Always ask what came back instead of assuming the result has the same type as the receiver.

**DANA:** Then a list gives us a contrast. Lists can change, right?

**MARCUS:** A list is a mutable sequence. A method such as append changes the existing list in place. If the list starts with Terra and Luna, appending Sol leaves the same list containing all three items. The return value is separate: append returns None. So assigning the result of append gives you None, while the list itself has been updated.

**DANA:** That sounds backwards at first. I might write a new variable from append and expect that variable to hold the expanded list.

**MARCUS:** Many beginners make that assumption. The experiment corrects it. Keep the result of append in one variable, then print the result and the original list. You will see None for the saved return value and the added item in the list. Methods that add, remove, or rearrange a mutable list commonly act on the list itself. The list documentation tells you which method does what.

**DANA:** Is it fair to memorize “strings return and lists mutate”?

**MARCUS:** It is a useful first contrast, but it is too broad as a permanent rule. A string method can return a list, as split does. A list method such as copy can return a list, while append mutates. The better rule is to ask two questions for the particular method: what does it return, and does it change the receiver? The type and the method documentation answer those questions.

**DANA:** You keep saying receiver. Is that just the object before the dot?

**MARCUS:** Yes. In a call on a string, the string before the dot is receiving the request. In a call on a list, the list before the dot is receiving it. This word is useful because it reminds you to inspect both sides of the call: the object that receives the method and the value the method sends back.

**DANA:** What if I do not know which methods exist? I definitely cannot memorize all of them.

**MARCUS:** You do not have to. Ask Python. Type identifies the kind of object. Dir lists attribute names available on the object. It is a menu of names, not an explanation of every name and not a guarantee that every name is callable. Then use help on the type or on a promising method to read focused documentation.

**DANA:** So the investigation loop is type, dir, help, predict, and run?

**MARCUS:** That is a strong loop. First identify the type. Look through the available names. Read help for the method that interests you. Predict a small result. Run the smallest experiment that can check your prediction. Documentation gives you the method’s contract, and the experiment helps you connect that contract to a value you can see.

**DANA:** Does dir tell me what the method accepts and returns?

**MARCUS:** No. Dir mainly lists names. It does not explain arguments or promise that a listed name is callable. That is why help matters. If you see a promising name in dir, ask for help about that method before guessing. Then test a small case. You are learning how to investigate instead of relying on memory.

**DANA:** This seems bigger than strings and lists. Is that the point?

**MARCUS:** Yes. Strings and lists are safe, visible examples of a general object model. Later, an object may represent a path, a file, a game entity, or a connection. It will have a type, state, and behaviors, but the actual names and side effects will come from its documentation. Do not assume a conceptual object has a real method until its API says so.

**DANA:** Let me try the whole explanation. A string is an object with type, text state, and methods. The dot selects a named behavior, and parentheses call it. Uppercase returns new text because strings are immutable. A list is mutable, so append changes the list and returns None. Then type, dir, and help let me investigate.

**MARCUS:** That is the circuit. When a method surprises you, return to the questions: what type is the receiver, what state does it hold, what does the method return, and does it mutate in place? Run a tiny example and read the documentation. You do not need to memorize everything to work effectively with objects.

## Worked examples

### string-new-value

```python
text = "luna"
upper_text = text.upper()
print(upper_text)  # expect: LUNA
print(text)  # expect: luna
print(type(upper_text).__name__)  # expect: str
```

### list-in-place

```python
route = ["Terra", "Luna"]
returned = route.append("Sol")
print(route)  # expect: ['Terra', 'Luna', 'Sol']
print(returned)  # expect: None
```

### discover

```python
signal = "Terra to Luna"
print(type(signal).__name__)  # expect: str
print("upper" in dir(signal))  # expect: True
print(signal.replace("Luna", "Sol"))  # expect: Terra to Sol
```

## Misconception

Calling the uppercase method changes the original string, so `s.upper()` should make later uses of `s` uppercase even when its result was not saved. In fact, strings are immutable: the call returns a new string, and the original stays the same unless a variable is assigned the returned value.

claims: C3

## Quiz

### Q1

- prompt: Which description best fits a value such as a string or list in Python?
- choices:
  - A: An object with a type, state or value, and behaviors
  - B: A variable name that has no type
  - C: A method that must always change itself
  - D: A comment that Python ignores
- answer: A
- rationale: The first object model asks what kind of thing a value is, what it holds, and what it can do.
- claims: C1

### Q2

- prompt: What does this call do to the original string when its result is not saved: `s.upper()`?
- choices:
  - A: It changes the original string in place
  - B: It returns a new uppercase string and leaves the original unchanged
  - C: It changes the original list in place
  - D: It deletes the string
- answer: B
- rationale: Strings are immutable, and uppercase returns a new string. The misconception is the tempting claim that the original changes.
- claims: C3

### Q3

- prompt: After `items.append("Sol")`, which statement is correct?
- choices:
  - A: The list is unchanged and append returns a new list
  - B: The list changes in place and append returns None
  - C: The list becomes an uppercase string
  - D: The list is immutable, so Python always raises an error
- answer: B
- rationale: Lists are mutable sequences; append adds to the existing list and returns None. The other choices confuse list mutation with string immutability or the misconception about returned values.
- claims: C5,C6

### Q4

- prompt: What kind of value does a string split method return?
- choices:
  - A: Always the original string
  - B: A list of pieces
  - C: None, while changing the string in place
  - D: A method object that must be printed
- answer: B
- rationale: Split is a string method whose result is a list, so a method on an immutable string can still return a different type.
- claims: C4

### Q5

- prompt: Which investigation sequence is the best way to explore an unfamiliar object?
- choices:
  - A: Guess a method, assume it changes the object, and skip the documentation
  - B: Use type, inspect names with dir, read focused help, then run a small test
  - C: Call every name from dir and save every return value
  - D: Assume every object behaves like a string and every method returns text
- answer: B
- rationale: Type identifies the object, dir helps discover names, help explains a type or method, and a small experiment checks a prediction. The distractors repeat the misconception that methods automatically mutate or return strings.
- claims: C7,C8

## Sources

- S1
- S2
- S3
- S4
- S5
