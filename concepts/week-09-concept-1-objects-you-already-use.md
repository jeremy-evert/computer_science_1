---
schema: concept-pipeline/v1
id: week-09-concept-1-objects-you-already-use
title: Objects You Already Use
course: COMSC-1033 Computer Science I
week: 9
objectives:
  - Describe a value as an object with a type, state, and behaviors.
  - Read dot notation for string and list methods.
  - Distinguish a string method that returns a value from a list method that mutates in place.
  - Use type, dir, and help to investigate an unfamiliar object.
canvas:
  overview_page: /courses/comsc-1033/pages/week-09-concept-1-objects-you-already-use
sources:
  - id: S1
    url: https://docs.python.org/3/reference/datamodel.html#objects-values-and-types
    accessed: '2026-10-08'
  - id: S2
    url: https://docs.python.org/3/tutorial/introduction.html#text
    accessed: '2026-10-08'
  - id: S3
    url: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    accessed: '2026-10-08'
  - id: S4
    url: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
    accessed: '2026-10-08'
  - id: S5
    url: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
    accessed: '2026-10-08'
  - id: S6
    url: https://docs.python.org/3/library/functions.html#dir
    accessed: '2026-10-08'
  - id: S7
    url: https://docs.python.org/3/library/functions.html#help
    accessed: '2026-10-08'
  - id: S8
    url: https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
    accessed: '2026-10-08'
  - id: S9
    url: https://docs.python.org/3/reference/executionmodel.html#naming-and-binding
    accessed: '2026-10-08'
---

## Claims

| id | claim | kind | checked_by | source |
| --- | --- | --- | --- | --- |
| C1 | A Python value is an object with a type, a current value or state, and behaviors supplied by its type. | model | doc citation: S1, “Objects, values and types” | S1 |
| C2 | A string is an object of type `str`, and dot notation selects a named attribute; parentheses call it when that attribute is a method. | explanation | doc citation: S1, “Objects, values and types”; S8, “The standard type hierarchy” | S1 |
| C3 | String methods such as `upper`, `strip`, and `replace` return a string result; the original is unchanged. CPython may hand back the same object when nothing changed, so compare values, not identity. | fact | code run: worked example string-new-value; doc citation: S2, “Text” and S4, “Text Sequence Type — str” | S4 |
| C4 | The `split` method on a string returns a list of pieces rather than a string. | fact | code run: worked example string-new-value; doc citation: S4, “Text Sequence Type — str” | S4 |
| C5 | A list is a mutable sequence, and methods such as `append`, `extend`, `remove`, and `reverse` change the list in place. | fact | doc citation: S3, “More on Lists”; S5, “Mutable Sequence Types” | S5 |
| C6 | A list mutation method such as `append` returns `None` while changing the list. | fact | code run: worked example list-in-place; doc citation: S3, “More on Lists” | S3 |
| C7 | `dir` lists attribute names and `help` on a type or method provides focused documentation for investigation. | practice | doc citation: S6, “dir()”; S7, “help()” | S6 |
| C8 | A method can return a value that you save and use, or can mutate its receiver; the method’s type and documentation determine which behavior occurs. | principle | code run: worked examples string-new-value and list-in-place; doc citation: S3, “More on Lists” and S4, “Text Sequence Type — str” | S3 |
| C9 | A variable name is a reference that is bound to an object; the name itself is not the object’s type. | fact | doc citation: S9, “Naming and binding” | S9 |
| C10 | `type` identifies the type of an object, including that a string value has type `str`. | fact | code run: worked example discover; doc citation: S1, “Objects, values and types” | S1 |
| C11 | Leaving off method-call parentheses refers to the method attribute instead of calling it. | fact | code run: worked example discover; doc citation: S8, “The standard type hierarchy” | S8 |
| C12 | `find` returns an integer position, while `startswith` returns a Boolean result. | fact | code run: worked example discover; doc citation: S4, “Text Sequence Type — str” | S4 |
| C13 | `list.copy` returns a list containing a shallow copy of the original list. | fact | code run: worked example list-in-place; doc citation: S3, “More on Lists” | S3 |
| C14 | `dir` lists names but does not explain every name or guarantee that every name is callable. | practice | doc citation: S6, “dir()” | S6 |
| C15 | `help` provides interactive documentation about a module, type, method, or other object. | practice | doc citation: S7, “help()” | S7 |
| C16 | A method call can return a value to save and use, while the receiver is the object before the dot whose state may or may not change. | principle | code run: worked examples string-new-value and list-in-place; doc citation: S3, “More on Lists” and S4, “Text Sequence Type — str” | S3 |
| C17 | String indexing starts at zero and `len` returns the number of characters; for `word = "code"`, `word[1]` is `"o"` and `len(word)` is `4`. | fact | doc citation: S2, “Text” | S2 |
| C18 | An f-string evaluates expressions inside braces and inserts their values into the surrounding text; `f"{place}: {count}"` with `place = "home"` and `count = 2` produces `"home: 2"`. | fact | doc citation: S2, “Text” | S2 |

## Script

<!-- slide id="start-with-a-value" title="Start with a value" claims="C1,C9,C10" -->
Let’s begin with values already present in ordinary Python code: a name, a message, or a list of items. Each one is a value in a Python program. Now widen the question. Do not ask only what the value is called. Ask what kind of thing it is, what information it currently holds, and what it knows how to do. That three-part question is our object model. A value has a type. Its current text or items are its state. Its type supplies behaviors, including methods. A string is therefore more than characters sitting in a variable. A list is more than several values between brackets. Both are objects that Python can work with according to their types. This is not yet a lesson about writing your own class. It is a way to look at values you already use. The name on the left is a reference we use to reach an object; the name itself is not the type. Two different strings can have different text and still have the same type. As you inspect each value, keep asking: what kind of object is this, what state does it hold, and what behavior can it offer?

<!-- slide id="follow-the-dot" title="Follow the dot" claims="C2,C11" -->
The next clue is a dot. When you see a value followed by a dot and a name, Python is looking up something attached to that object. When the name identifies a method, parentheses call that method. In spoken language, you can hear it as: ask this object to use this behavior. A string can be asked to become uppercase, remove outside spaces, or replace one piece of text. The parentheses matter because they perform the call; without them, you are referring to the method itself rather than asking it to run. Not every name after a dot is a method. Some are attributes that hold information. Today we are concentrating on methods, because they make behavior visible. The dot is not decoration and it is not a universal command. It is a route from an object to a named part of what that object offers. This is why methods feel as though they belong to the string: the string’s type supplies them. Pause and translate a line like “message dot upper with parentheses” into ordinary language: ask the message object for its uppercase behavior and call it. That translation will help you read programs before you can write every line yourself.
<!-- show: code example="string-new-value" -->

<!-- slide id="string-returns-value" title="A string method gives back a value" claims="C3,C4,C8,C9,C10,C12,C16" -->
Strings give us a useful surprise. A string method such as uppercase does not edit the original string in place. Strings are immutable, which means their contents cannot be changed in place. The method returns a string; the original is unchanged. CPython may hand back the same object when nothing changed, so compare values, not identity. If you call the method and throw away its result, the original reference still leads to the original text. If you assign the result back to the same variable, that variable now refers to the returned string. The important habit is to ask what came back. Some string methods return a string. The split method returns a list of pieces. The find method returns an integer position, while startswith returns a Boolean. A method call is not automatically an instruction that changes the object you started with. It may be a computation that produces a value. This distinction explains a common beginner error: saying that an uppercase call changes the string, then being surprised when printing the string shows the old text. Nothing mysterious happened. The call produced a result, and no one saved it. If you do save it, you have not repaired the old string; you have made your variable refer to the returned string. Think of a string method as sending a request to a text object and receiving a result in reply, then check the result's type instead of guessing from the receiver's type.
<!-- show: code example="string-new-value" -->

<!-- slide id="list-in-place" title="A list can change in place" claims="C3,C5,C6,C8,C9,C13,C16" -->
Now compare a list. Lists are also objects, but a list is a mutable sequence. Mutable means the list can be changed in place. A method such as append adds an item to the existing list. The list after the call contains the new item. The return value is a different question: append returns None. That is why the useful result is usually the changed list, not a new list stored from append. The same pattern appears with other list methods that add, remove, or rearrange items. They act on the list itself. This is a place where type matters. The string method upper returns a string; the original is unchanged because strings are immutable. The list method append changes a mutable list. Neither behavior is the definition of all methods. It is a property you check for the particular type and method. A safe routine is: predict the object’s state before the call, predict whether the call returns a value, run it, and inspect both. If you assign the result of append to a variable, that variable holds None while the original list has changed. The list and the returned value are two separate things to keep track of.
<!-- show: code example="list-in-place" -->

<!-- slide id="check-yourself" title="Use the return value as evidence" claims="C3,C4,C5,C6,C8,C13,C16" -->
Let’s make the contrast concrete. With a string, call the method and print both the returned value and the original. You will see two different strings: the new uppercase text and the old lowercase text. With a list, call append, keep the returned value, and then print both. You will see None in the saved result and the added item in the original list. That pair of observations is more useful than memorizing a slogan such as strings return and lists mutate. It teaches a question: what does this method return, and does it change its receiver? The word receiver simply means the object before the dot, the object receiving the request. The answer comes from the type’s rules and the method’s documentation. A string can also return a list from split, so even a method on an immutable object may return a different type. A list can have methods such as copy that return a list, and it also has methods that change the list. Types set the menu of behaviors, but individual methods determine the details. Use the examples as tiny experiments. Predict first. Run second. Explain the printed lines in plain language. That loop turns an accidental result into object knowledge.
<!-- show: code example="string-new-value" -->
<!-- show: code example="list-in-place" -->

<!-- slide id="debug-the-missing-result" title="Debug the missing result" claims="C9,C11,C3,C4,C5,C6,C8,C10,C13,C16" -->
Here is a small live debugging session. I start with `label = " python "` and write `clean = label.strip()`. Then I write `clean.upper()` and print `clean`. The output is still `python`, in lowercase. My first thought might be, “upper did not work,” but the evidence says something more precise: the call produced a string result, and I did not save it. I also used the parentheses correctly, so this is not the missing-parentheses bug. The repair is `clean = clean.upper()`, followed by `print(clean)`, which displays `PYTHON`. The first assignment changes what the name `clean` refers to after `strip` returns a string; the second assignment does the same after `upper` returns a string. The original string object was never edited in place.

Now I make a neighboring list bug. I start with `route = ["red", "green"]`, write `saved = route.append("blue")`, and print `saved`. The output is `None`, but printing `route` shows `['red', 'green', 'blue']`. That is not a failed append and not a new list hidden in `saved`. The list receiver changed in place, while append deliberately returned `None`. If I wanted a separate list value, I would use `copy`, as in `backup = route.copy()`, and then check that `backup` is a list. These two debugging cases look similar because both use a dot and parentheses, but their method contracts differ. I inspect the receiver, the saved return value, and the post-call state separately. That three-part check usually tells me whether I forgot to save a returned value, incorrectly expected a mutation, or simply called the wrong method.

Before moving on, notice the variable names in this debugging story. `label`, `clean`, `route`, `saved`, and `backup` are references used to reach objects. They are not labels for permanent types. A name can be rebound to a returned string or a copied list, while the type of the object it reaches is determined by that current value. This is why printing a result and checking `type` can be more informative than reasoning from a variable's name.

<!-- slide id="ask-python" title="Ask Python what is available" claims="C7,C10,C14,C15" -->
You do not need to memorize every method. Python can help you investigate. Type asks what kind of object you have. Dir lists names of attributes and methods available on that object. It is a menu, not a promise that every name is a method or that every method takes the same arguments. Help gives more focused documentation about a type or a method. A practical loop is: identify the type, look through the available names, ask for help on a promising method, predict a small result, and run a tiny experiment. Start with a familiar object such as a string or list, then try the same investigation on something new. If you see a method name in the list, read its help before guessing what it changes or returns. This is a professional programming habit. The goal is not to know the whole library in your head. The goal is to know how to ask a good question of the language and then test the answer. Documentation and experiments work together: documentation tells you the contract, while a small run helps you connect that contract to a value you can see.
<!-- show: code example="discover" -->

<!-- slide id="recap" title="Recap the evidence" claims="C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16" -->
Let’s collect the evidence before the final review. An object is a value with a type, state, and available behavior. A variable name is a reference to the current object, so the name does not tell us the whole story. A dot performs attribute lookup, and parentheses call a method; without the parentheses we have only referred to the method attribute. For strings, immutability means methods such as `upper`, `strip`, and `replace` return a string; the original is unchanged. CPython may hand back the same object when nothing changed, so compare values, not identity. `split` is a useful reminder that the result can be a list, while `find` gives an integer position and `startswith` gives a Boolean. For lists, mutability allows in-place changes. `append` changes the receiver and returns `None`; `copy` returns a list. There is no universal “all methods return” or “all methods mutate” rule. The method’s documentation is the contract.

When a line surprises you, debug it in a fixed order. Identify the receiver and its type. Read the call carefully, including its parentheses. Save the return value if you need it. Inspect the receiver after the call. Then use `dir` to discover names, `help` to read focused documentation, and a tiny run to test one prediction. This routine makes the invisible parts of a method call visible: the object before the dot, the result sent back, and the state that remains afterward. You are not memorizing isolated tricks. You are building a repeatable way to learn an unfamiliar object.

<!-- slide id="carry-object-question-forward" title="Carry the object question forward" claims="C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16" -->
The review is complete. We met values we already use, followed the dot, and compared what string and list methods do. The reusable habit is this: when Python gives you a thing, ask what type it has, what state it holds, what behavior it offers, what it returns, and whether it changes in place. Strings and lists are not merely containers for syntax practice. They are early examples of a much larger way to organize software. Later, objects may represent files, paths, game entities, or connections. The exact methods will come from their types and documentation, so do not assume that a conceptual example is a real API. For today, keep the contrast sharp. Uppercase on a string returns a string; the original is unchanged. Append on a list changes the list and returns None. Dir and help make unfamiliar behavior discoverable. If you can explain those observations, you already have a working first model of objects. The next time a method surprises you, do not guess that all objects behave like strings or all methods behave like append. Identify the type, read the method’s contract, and run the smallest useful check.

## Podcast

<!-- claims: C1,C9,C10 -->
**DANA:** I thought an object was something we had to create with a class. But this lesson says I have already been using objects. What exactly counts as an object here?

**MARCUS:** A value Python can work with is an object. For this lesson, use three questions. What type of thing is it? What value or state does it currently hold? What behaviors does its type make available? A string such as a message is an object, and a list of places is an object. You do not need to write a new class before you can think this way.

**DANA:** So the variable name is not the object’s type?

**MARCUS:** Right. A variable name is a reference we use to reach a value. The type describes the kind of object. Two variables can refer to strings with different text, but both objects still have the string type. Their current text is the useful state we can observe. Their type supplies behaviors such as changing case, removing outside spaces, or splitting text.

<!-- claims: C2,C11 -->
**DANA:** The behavior part is where the dot comes in, I think. When I read a string followed by a dot and a method name, what should I hear in my head?

**MARCUS:** Hear a request. Ask the object to use a named behavior. The dot looks up a name attached to the object. If that name is a method, the parentheses call it. Saying “message dot upper with parentheses” is a spoken way to say “ask the message object for its uppercase behavior and call it.” The parentheses are what make the call happen.

**DANA:** And if I leave off the parentheses, I am not actually asking it to run?

**MARCUS:** Correct. Without the parentheses, you are referring to the method itself. Also remember that not every name after a dot is a method. A dot can reach an attribute holding information. For this first model, focus on the common pattern of an object, a dot, a method name, and a call. The type tells you which names make sense for that object.

<!-- claims: C3,C9 -->
**DANA:** Last week’s strings lesson showed an uppercase method. I used the call, printed my string, and it looked unchanged. I assumed the method had failed.

**MARCUS:** That is the classic misconception. String objects are immutable. Their contents cannot be changed in place. The uppercase method returns a string; the original is unchanged. If you call it and discard the returned value, your original variable still refers to the original text. If you assign the returned value back to the variable, the variable now refers to the returned uppercase text. If nothing changes, CPython may hand back the same object, so compare values, not identity.

**DANA:** So the call did work, but I did not keep the answer?

**MARCUS:** Exactly. Think of the method as a request that sends back a result. The old string is not edited. This is why it helps to print both values. One print can show the returned uppercase string, and another can show that the original lowercase string remains. Saving the result gives your variable a new reference; it does not alter the old string.

<!-- claims: C3,C4,C12 -->
**DANA:** Does every string method return another string?

**MARCUS:** No. That is another useful caution. Uppercase, strip, and replace return a string; the original is unchanged. Split returns a list of pieces. Search methods can return numbers, and checks can return true or false. A method belongs to the string object, but its result can have a different type. Always ask what came back instead of assuming the result has the same type as the receiver.

<!-- claims: C5,C6,C8 -->
**DANA:** Then a list gives us a contrast. Lists can change, right?

**MARCUS:** A list is a mutable sequence. A method such as append changes the existing list in place. If the list starts with red and green, appending blue leaves the same list containing all three items. The return value is separate: append returns None. So assigning the result of append gives you None, while the list itself has been updated.

**DANA:** That sounds backwards at first. I might write a new variable from append and expect that variable to hold the expanded list.

**MARCUS:** Many beginners make that assumption. The experiment corrects it. Keep the result of append in one variable, then print the result and the original list. You will see None for the saved return value and the added item in the list. Methods that add, remove, or rearrange a mutable list commonly act on the list itself. The list documentation tells you which method does what.

<!-- claims: C3,C4,C5,C6,C8,C9,C10,C13,C16 -->
**DANA:** Let me try a check. If I run the string and list examples together, can I predict every printed line?

**MARCUS:** Start with `text = "python"`, then save `pieces = text.split("h")`. For the list, use `items = ["red"]` and `returned = items.append("blue")`. Predict the pieces, their type, the returned value, and the changed list. Keep the two receivers separate.

**DANA:** The pieces should be `['pyt', 'on']`, with type `list`, because split returns a list. Append should return `None`, while `items` should contain red and blue. Is that the contrast?

**MARCUS:** Exactly. Split returns a list for `pieces`; it does not turn the original string into a list. Append changes the list receiver and gives back `None`. The four observations are `['pyt', 'on']`, `list`, `None`, and `['red', 'blue']`.

**DANA:** If I instead wrote `items = items.append("blue")`, would I still have the expanded list in `items`?

**MARCUS:** No. It would bind `items` to the return value, `None`, after changing the original list. The method changes the receiver, but the assignment replaces the name’s reference with the returned value. Inspect both effects separately.

**DANA:** Back in the version where `returned = items.append("blue")` left `items` alone as a list: if I wanted another list value after the append, I could use `backup = items.copy()` and check that `backup` is a list?

**MARCUS:** Exactly. Copy returns a list containing a shallow copy. That is why “list methods mutate” is too broad: append mutates and returns `None`, while copy returns a list. You predicted the result, ran the check, and identified the receiver.

<!-- claims: C4,C5,C6,C8,C13,C16 -->
**DANA:** Is it fair to memorize “strings return and lists mutate”?

**MARCUS:** It is a useful first contrast, but it is too broad as a permanent rule. A string method can return a list, as split does. A list method such as copy can return a list, while append mutates. The better rule is to ask two questions for the particular method: what does it return, and does it change the receiver? The type and the method documentation answer those questions.

**DANA:** You keep saying receiver. Is that just the object before the dot?

**MARCUS:** Yes. In a call on a string, the string before the dot is receiving the request. In a call on a list, the list before the dot is receiving it. This word is useful because it reminds you to inspect both sides of the call: the object that receives the method and the value the method sends back.

<!-- claims: C3,C4,C5,C6,C8,C9,C13,C16 -->
**DANA:** Can we walk through one bug slowly? I want to see how those two sides help.

**MARCUS:** Start with `label = " python "`. You call `clean = label.strip()`, then write `clean.upper()`, then print `clean`. The output is `python`, not `PYTHON`. The call did run, but its string result was discarded. Save it with `clean = clean.upper()`, and the next print is `PYTHON`. The receiver was the string reached through `clean`; the result was a string, and the original remained unchanged; the assignment rebound the name to the result.

**DANA:** So if I see the old text, I should ask whether I saved the return value before blaming the method.

**MARCUS:** Exactly. Now compare `route = ["red", "green"]` and `saved = route.append("blue")`. Printing `saved` gives `None`; printing `route` gives `['red', 'green', 'blue']`. Append changed the list receiver and returned `None`. If you need another list value, `backup = route.copy()` returns a list. Same dot syntax, different contract.

<!-- claims: C7,C8,C10,C14,C15 -->
**DANA:** What if I do not know which methods exist? I definitely cannot memorize all of them.

**MARCUS:** You do not have to. Ask Python. Type identifies the kind of object. Dir lists attribute names available on the object. It is a menu of names, not an explanation of every name and not a guarantee that every name is callable. Then use help on the type or on a promising method to read focused documentation.

**DANA:** So the investigation loop is type, dir, help, predict, and run?

**MARCUS:** That is a strong loop. First identify the type. Look through the available names. Read help for the method that interests you. Predict a small result. Run the smallest experiment that can check your prediction. Documentation gives you the method’s contract, and the experiment helps you connect that contract to a value you can see.

**DANA:** Does dir tell me what the method accepts and returns?

**MARCUS:** No. Dir mainly lists names. It does not explain arguments or promise that a listed name is callable. That is why help matters. If you see a promising name in dir, ask for help about that method before guessing. Then test a small case. You are learning how to investigate instead of relying on memory.

<!-- claims: C2,C3,C8,C9,C11,C12,C16 -->
**DANA:** Can we test the difference between finding a method and calling it? I sometimes forget the parentheses.

**MARCUS:** Sure. With `signal = "red to green"`, `signal.find` refers to the method attribute, but `signal.find("green")` calls it and returns the integer `7`. Likewise, `signal.startswith("red")` calls the method and returns `True`. The parentheses are not decoration: they supply the call's arguments and request the result. If you only look at `signal.find`, you have not asked Python to search yet.

**DANA:** And if I save `position = signal.find("green")`, `position` is a reference to the integer result, not a new kind of signal object?

**MARCUS:** Right. The name is simply bound to the value returned by that call. This is the same reasoning as `upper_text = text.upper()` and `returned = route.append("blue")`; inspect the result instead of guessing from the receiver. The method's documentation tells you whether the result is a string, list, integer, Boolean, or `None`, and whether the receiver changed.

<!-- claims: C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C13,C14,C15,C16 -->
**DANA:** Here is my recap. A value is an object, so I ask about its type, current state, and available behaviors. A variable is a reference to the current object.

**MARCUS:** Good. A dot selects an attribute, and parentheses call it when it is a method. Without parentheses, you refer to the method instead of running it.

**DANA:** `upper` returns a string; the original is unchanged. `split` can return a list. A list is mutable, so `append` changes it in place and returns `None`, while `copy` returns a list.

**MARCUS:** Yes. Do not assume every method on a type behaves alike. Ask what the method returns and whether its receiver changes. Use `type`, `dir`, and focused `help` instead of guessing.

**DANA:** My routine is: identify the receiver and type, read the parentheses, predict the return, run a tiny check, inspect the receiver, and save the result when needed.

**MARCUS:** That is the working model: explain the object before the dot, the value sent back, and the state left afterward. Then you are using objects deliberately.

**DANA:** When output surprises me, I should not guess from a variable name or assume every method mutates. I should identify the type and receiver, read help, and run the smallest useful check.

**MARCUS:** Right. The result and the post-call state are evidence. They show whether you saved a returned value, observed `None` from a mutation, or received a different result type.

<!-- claims: C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16 -->
**DANA:** This seems bigger than strings and lists. Is that the point?

**MARCUS:** Yes. Strings and lists are safe, visible examples of a general object model. Later, an object may represent a path, a file, a game entity, or a connection. It will have a type, state, and behaviors, but the actual names and side effects will come from its documentation. Do not assume a conceptual object has a real method until its API says so.

**DANA:** Let me try the whole explanation. A string is an object with type, text state, and methods. The dot selects a named behavior, and parentheses call it. Uppercase returns a string; the original is unchanged because strings are immutable. A list is mutable, so append changes the list and returns None. Then type, dir, and help let me investigate.

**MARCUS:** That is the working model. When a method surprises you, return to the questions: what type is the receiver, what state does it hold, what does the method return, and does it mutate in place? Run a tiny example and read the documentation. You do not need to memorize everything to work effectively with objects.

## Worked examples

### string-new-value

```python
text = "python"
upper_text = text.upper()
print(upper_text)  # expect: PYTHON
print(text)  # expect: python
print(type(upper_text).__name__)  # expect: str
pieces = text.split("h")
print(pieces)  # expect: ['pyt', 'on']
print(type(pieces).__name__)  # expect: list
```

### list-in-place

```python
route = ["red", "green"]
returned = route.append("blue")
print(route)  # expect: ['red', 'green', 'blue']
print(returned)  # expect: None
backup = route.copy()
print(backup)  # expect: ['red', 'green', 'blue']
print(type(backup).__name__)  # expect: list
```

### discover

```python
signal = "red to green"
print(type(signal).__name__)  # expect: str
print("upper" in dir(signal))  # expect: True
print(signal.replace("green", "blue"))  # expect: red to blue
print(signal.find("green"))  # expect: 7
print(signal.startswith("red"))  # expect: True
```

## Misconception

Calling the uppercase method changes the original string, so `s.upper()` should make later uses of `s` uppercase even when its result was not saved. In fact, strings are immutable: the call returns a string; the original is unchanged, and the original name stays bound to the old text unless the returned value is assigned. If nothing changes, CPython may hand back the same object, so compare values, not identity. Related confusions: a name is the type; `dir` lists only methods you must call.

claims: C3,C9,C14

## Quiz

### Q1

- prompt: Which description best fits a value such as a string or list in Python?
- choices:
  - A: An object with a type, state or value, and behaviors
  - B: A variable name that permanently is the object's type
  - C: A value whose methods must change it in place and return nothing
  - D: A mutable container, because every object can change in place
- answer: A
- rationale: The first object model asks what kind of thing a value is, what it holds, and what it can do. B targets the related confusion that a name is the type. C and D target the misconception that methods must change objects in place or return nothing.
- claims: C1,C8,C9

### Q2

- prompt: What does this call do to the original string when its result is not saved: `s.upper()`?
- choices:
  - A: It changes the original string in place
  - B: It returns a string result and leaves the original unchanged
  - C: It returns `None` after changing the original string
  - D: It returns `None` and leaves the original unchanged
- answer: B
- rationale: Strings are immutable. The call returns a string; the original is unchanged. A targets the misconception that a method changes the original. C targets expecting an in-place change and no useful return value. D targets expecting a method to return nothing instead of a value; assigning the string result is what makes a name refer to the returned text.
- claims: C3,C9

### Q3

- prompt: After `items.append("blue")`, which statement is correct?
- choices:
  - A: The list is unchanged and append returns an expanded list
  - B: The list changes in place and append returns None
  - C: The list changes in place and append returns the changed list
  - D: The list changes in place, but append returns a new list
- answer: B
- rationale: Lists are mutable sequences; append adds to the existing list and returns None. A targets expecting no mutation and an expanded return value. C targets expecting the in-place method to return the changed list. D targets expecting a new list value instead of the documented no-value return.
- claims: C5,C6

### Q4

- prompt: What kind of value does a string split method return?
- choices:
  - A: The original string changes in place and becomes the pieces
  - B: A list of pieces
  - C: Nothing is returned; split only changes the original string
  - D: The original string changes in place and split returns `None`
- answer: B
- rationale: Split is a string method whose result is a list; the original string is unchanged. A targets expecting a method to mutate the original. C targets expecting a method to return nothing. D combines both parts of the misconception: it expects an in-place change and a `None` result.
- claims: C3,C4

### Q5

- prompt: Which investigation sequence is the best way to explore an unfamiliar object?
- choices:
  - A: Use `type`, inspect names with `dir`, read focused `help`, then run a small test
  - B: Use `type`, call every name from `dir` because `dir` lists only methods you must call, and skip `help`
  - C: Call every name from `dir` because `dir` lists only methods you must call; errors mean the object is broken
  - D: Assume every method changes the original and returns nothing
- answer: A
- rationale: `type` identifies the object, `dir` helps discover names, `help` explains a type or method, and a small experiment checks a prediction. B and C target the related confusion that `dir` lists only methods you must call. D targets the misconception that every method changes the original and returns nothing.
- claims: C7,C8,C10,C14,C15,C16

## Review

### R1

- prompt: Given `word = "code"`, which expression produces `"o"` while `len(word)` produces `4`?
- choices:
  - A: `word[1]`
  - B: `word[0]`
  - C: `word[4]`
  - D: `word[len(word)]`
- answer: A
- rationale: String indexing starts at zero, so index 1 selects the second character, `o`; the length is four.
- claims: C17

### R2

- prompt: If `place = "home"` and `count = 2`, what does `f"{place}: {count}"` produce?
- choices:
  - A: `"place: count"`
  - B: `"home: 2"`
  - C: `"home2"`
  - D: `"{place}: {count}"`
- answer: B
- rationale: An f-string evaluates the expressions inside braces and inserts their values into the surrounding text.
- claims: C18

## Sources

- S1
- S2
- S3
- S4
- S5
- S6
- S7
- S8
- S9
