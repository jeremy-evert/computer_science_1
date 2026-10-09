---
schema: concept-pipeline/v1
id: week-09-concept-2-your-first-class
title: Your First Class
course: COMSC-1033 Computer Science I
week: 9
objectives:
  - Explain why a class can define a new kind of object for a program.
  - Write a class with __init__, self, and an instance attribute.
  - Create two instances from one class and trace their separate state.
  - Read and change instance attributes with dot notation.
  - Write a first method that uses self to work with instance state.
canvas:
  overview_page: /courses/comsc-1033/pages/week-09-concept-2-your-first-class
sources:
  - id: S1
    url: https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes
    accessed: '2026-10-08'
  - id: S2
    url: https://docs.python.org/3/tutorial/classes.html#class-objects
    accessed: '2026-10-08'
  - id: S3
    url: https://docs.python.org/3/tutorial/classes.html#instance-objects
    accessed: '2026-10-08'
  - id: S4
    url: https://docs.python.org/3/tutorial/classes.html#method-objects
    accessed: '2026-10-08'
  - id: S5
    url: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
    accessed: '2026-10-08'
  - id: S6
    url: https://docs.python.org/3/reference/datamodel.html#object.__init__
    accessed: '2026-10-08'
  - id: S7
    url: https://docs.python.org/3/tutorial/introduction.html#text
    accessed: '2026-10-08'
  - id: S8
    url: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    accessed: '2026-10-08'
---

## Claims

| id | claim | kind | checked_by | source |
| --- | --- | --- | --- | --- |
| C1 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, a class definition creates a class object whose body supplies names such as methods and attributes; the class object can be used to create instances. | model | code run: class-object-basics; doc citation: S1, “A First Look at Classes” and S2, “Class Objects” | S1 |
| C2 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, calling a class object creates an instance of that class, and two separate calls create two separate instance objects. | fact | code run: separate-instance-state; doc citation: S2, “Class Objects” and S3, “Instance Objects” | S2 |
| C3 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, an `__init__` method is called automatically during a normal instance-creation call and can initialize that instance’s attributes from arguments. | fact | code run: class-object-basics; doc citation: S3, “Instance Objects” and S6, “object.__init__” | S6 |
| C4 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, in an instance method the first parameter conventionally named `self` receives the instance on which the method was called. | explanation | code run: class-object-basics; doc citation: S4, “Method Objects” | S4 |
| C5 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, an assignment such as `self.value = start` stores or updates an attribute on the current instance, and `instance.value` reads that attribute. | fact | code run: separate-instance-state; doc citation: S3, “Instance Objects” | S3 |
| C6 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, instance attributes can hold state that differs between instances of the same class; changing one instance’s attribute does not by itself change another instance’s corresponding attribute. | principle | code run: separate-instance-state; doc citation: S3, “Instance Objects” and S5, “Class and Instance Variables” | S5 |
| C7 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, a name assigned inside a method without `self.` is a local name for that method call, not an instance attribute; it is not available later as persistent instance state. | fact | code run: local-vs-instance; doc citation: S3, “Instance Objects” and S4, “Method Objects” | S4 |
| C8 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, dot assignment to an instance, such as `first.value = 9`, changes the attribute reached through that particular instance. | fact | code run: separate-instance-state; doc citation: S3, “Instance Objects” | S3 |
| C9 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, an instance method can read an attribute through `self`, compute with that state, and return a result to its caller. | explanation | code run: class-object-basics; doc citation: S4, “Method Objects” | S4 |
| C10 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, a method definition belongs to a class, while a call through an instance supplies that instance as the method’s first argument. | principle | code run: class-object-basics; doc citation: S4, “Method Objects” | S4 |
| C11 | A class is useful when a program needs a repeatable type with named state and behavior rather than unrelated variables and functions for each individual object. | model | doc citation: S1, “A First Look at Classes” and S2, “Class Objects” | S1 |
| C12 | For a string, `upper()` returns a string result and leaves the original string value unchanged when the result is not assigned back. | fact | code run: review-string-method; doc citation: S7, “Text” | S7 |
| C13 | For a list, `append` changes the list in place and returns `None`. | fact | code run: review-list-method; doc citation: S8, “More on Lists” | S8 |
| C14 | For ordinary multi-line user-defined classes and ordinary method bodies as taught here, the `class` statement uses a class name followed by an indented body containing the class definition. | fact | code run: class-object-basics; doc citation: S1, “A First Look at Classes” | S1 |

## Script

<!-- slide id="from-objects-to-your-type" title="From objects you use to a type you define" claims="C1,C2,C6,C11" -->
Strings and lists gave us a working object model: each has a type, current contents, and behaviors such as `upper` or `append`. Those types were supplied by Python. Now we need a way to describe an object belonging to our program: perhaps a counter, a map point, or a simulated dog. A class lets us define that repeatable kind of object.

Writing a class is useful when several objects need the same shape and the same operations. Without a class, we could keep unrelated variables for each counter and write separate functions that happen to work on them. That approach makes the connection between data and behavior easy to lose. For ordinary multi-line user-defined classes and ordinary method bodies as taught here, a class gives the program one named type, while its instances can carry their own current values and its methods give every instance the same vocabulary. The class is the definition; an instance is one object made from that definition. We are not claiming that every piece of data needs a class. We choose a class when a program needs a repeatable type with state and behavior together.

It gives us a vocabulary for questions that would otherwise be vague: which attribute belongs to this counter instance, and which method works with it. A class does not remove the need to understand names and assignments; it puts those ideas in a structure we can trace.

<!-- slide id="read-the-class-statement" title="Read the class statement" claims="C1,C2,C6,C11,C14" -->
For ordinary multi-line user-defined classes and ordinary method bodies as taught here, the basic shape is small:

`class Counter:`

followed by an indented body. The name `Counter` becomes the name of a class object. The body is where we place the definitions that describe what counters can do. At this point, the class definition has created the type we can use; it has not yet created a particular counter holding a particular count. That distinction is the first important separation in this lesson.

For ordinary multi-line user-defined classes and ordinary method bodies as taught here, when we write `first = Counter(3)`, we call the class object. Python makes an instance from that class and gives the resulting object to `first`. A later call, `second = Counter(3)`, makes another instance. The two objects come from the same class, so they have the same available design, but they are still two objects. Read the uppercase name after `class` as the type we are defining, and read each call to that name as a request for one instance of that type. The parentheses are not creating a shared bucket called `Counter`; they are producing one object for each call.

Track the name on the left: `first` refers to the first instance, `second` to the second, and the class name remains available for more instances. A type definition can be reused without requiring identical state.

<!-- slide id="initialize-an-instance" title="Initialize an instance with __init__ and self" claims="C3,C4,C5,C6,C7" -->
Most first classes need a starting state. We write an initializer:

`def __init__(self, start):`

and then store the argument with `self.value = start`. For ordinary multi-line user-defined classes and ordinary method bodies as taught here, Python calls `__init__` during a normal instance-creation call, so `Counter(3)` supplies `3` to `start` while `self` identifies the new counter being initialized. The first parameter is conventionally named `self`; it is the instance receiving the method call, not a separate counter or a value shared by all instances.

The two sides of `self.value = start` have different jobs. `start` is the parameter name available during this initializer call. `self` is the current instance. The dot selects the attribute named `value` on that instance, and assignment stores the starting number there. If we wrote only `value = start`, we would bind a local name during the initializer rather than store instance state. The class would still be defined, but the new object would not have the `value` attribute we meant to create. Keep reading the line as “put this argument into the current object’s value attribute.”

The initializer is a method, not a second class definition. Its `start` parameter can differ on calls: the same code stores `3` for one object and `8` for another because `self` identifies the object being prepared.

<!-- show: code example="class-object-basics" -->

<!-- slide id="state-belongs-to-an-instance" title="State belongs to the instance" claims="C2,C3,C4,C5,C6,C8,C10" -->
Now make two counters with different starting values:

`first = Counter(3)`

`second = Counter(8)`

For ordinary multi-line user-defined classes and ordinary method bodies as taught here, the initializer runs once for `first` and once for `second`. On the first run, `self` is `first`, so `self.value = start` stores `3` on `first`. On the second run, `self` is `second`, so the same line stores `8` on `second`. The method definition is shared as part of the class, but the `value` attributes reached through the two instances are separate state.

For ordinary multi-line user-defined classes and ordinary method bodies as taught here, this is the misconception to watch: same class does not mean one shared instance state. If we later write `first.value = 4`, reading `first.value` gives `4`, while reading `second.value` still gives `8`. The dot matters because it names the object through which we are reaching the attribute. We should say “the value on `first`” or “the value on `second`,” not just “the class’s value.” There can be two current values because there are two instance objects. The class supplies the common structure; each instance holds its own values assigned through `self`.

The fact that the source line is shared can hide the fact that its target changes. During one initializer call, `self` is the first instance; during the other call, `self` is the second. Ask “which object is self right now?” before asking whether the value is shared. The answer is tied to the current call, not merely to the class name.

<!-- show: code example="separate-instance-state" -->

<!-- slide id="use-dot-notation" title="Read and change state with dot notation" claims="C5,C6,C7,C8" -->
For ordinary multi-line user-defined classes and ordinary method bodies as taught here, dot notation works in both directions. An expression such as `first.value` reads the current attribute on `first`. An assignment such as `first.value = 9` changes the attribute reached through `first`. It does not select `second`, and it does not rewrite every object made from the class. To predict a line, identify the expression before the dot first. The object before the dot is the instance whose state is being read or changed.

This gives us a small experiment. Create `first` with value `3` and `second` with value `8`. Print both. Assign `first.value = 9`. Print both again. The first output pair is `3` and `8`; the second is `9` and `8`. Nothing in that assignment says “find all counters.” It says “store `9` in the `value` attribute reached through this one instance.” You can also assign another value to `second` and observe that the two histories remain independent. The attribute is state because it records information that can be read later, after the initializer call has ended.

Do not confuse `first.value` with the variable name `first`. The name refers to the instance; the dot access asks that instance for one attribute. This is the same basic route we practiced with strings and lists, now pointed at a type we defined.

After a method call, print the attribute through the same instance that called it. Another instance may show a correct but irrelevant value; a bare local name outside the method will not find the temporary binding.

<!-- slide id="write-a-method" title="Write a first method that uses self" claims="C4,C5,C9,C10" -->
An instance method is a function defined inside the class body. Suppose a counter should report its next value:

`def next_value(self):`

`    return self.value + 1`

For ordinary multi-line user-defined classes and ordinary method bodies as taught here, when we call `first.next_value()`, Python supplies `first` as the first argument, so inside the method `self` refers to `first`. The expression reads `first.value`, adds one, and returns the result. Calling `second.next_value()` performs the same method logic with `self` referring to `second`. One method definition can therefore operate on many instances, because the current instance arrives through the first parameter.

For ordinary multi-line user-defined classes and ordinary method bodies as taught here, this method computes and returns a value; it does not change the counter’s stored value. If we want an advancing counter, the method needs an assignment such as `self.value = self.value + 1`, followed by a return if we want to report the new state. The word `self` is a guide to which object’s state the method should use. Read `self.value` as “this call’s instance attribute,” not as a class-wide variable. A method can read state, change state, or do both, depending on the statements in its body.

The call syntax supplies the instance without requiring us to write it as an explicit argument. We write `first.next_value()`, not `Counter.next_value(first)` in ordinary use. The method definition still has a first parameter because its body needs a name for the receiving instance. That name lets one method body be reused while the object selected before the dot changes.

<!-- show: code example="class-object-basics" -->

<!-- slide id="find-the-missing-self" title="Find the missing self. before state" claims="C5,C6,C7,C9" -->
For ordinary multi-line user-defined classes and ordinary method bodies as taught here, here is the most useful first debugging contrast. In a method, `value = self.value + amount` creates or updates a local name called `value`. It does not update the instance attribute named `value`. That local name can help with a calculation during the call, but after the method returns, it is not persistent state that later dot notation can read. To keep the result on the object, write `self.value = self.value + amount`.

The punctuation is doing real work. The left side `value` means a local binding. The left side `self.value` means an attribute on the current instance. If a method runs without an error but the object still shows its old value, inspect the left side of every assignment. Did the line assign to `self.value`, or did it assign only to `value`? This is why omitting `self.` is more than a style difference: it sends the result to a different place.

For ordinary multi-line user-defined classes and ordinary method bodies as taught here, run the contrast with a counter starting at `5`. A method with `value = self.value + amount` leaves the counter at `5` after the call. A method with `self.value = self.value + amount` leaves it at `9` after adding `4`. The class is not sharing one state here; the first method simply stored its temporary result in a local name instead of the instance. The repair is to name the intended object explicitly with `self.`.

A local calculation is not useless; it can be returned, printed, or used for another calculation inside the method. The precise problem is expecting a bare local name to become an attribute automatically. Python does not infer that destination from the name `value`. The assignment target tells Python whether the result belongs to the call’s temporary work or to the instance’s lasting state.

<!-- show: code example="local-vs-instance" -->

<!-- slide id="trace-the-two-objects" title="Trace the objects, not a slogan" claims="C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11" -->
For ordinary multi-line user-defined classes and ordinary method bodies as taught here, let’s trace the complete pattern. The `class Counter:` statement defines one repeatable type. `first = Counter(3)` creates one instance and runs `__init__` with `self` bound to `first`. `second = Counter(8)` creates another instance and runs the same initializer with `self` bound to `second`. Each initializer stores a starting value on its current instance. A dot read selects the instance before the dot. A dot assignment changes that selected instance. A method call supplies that selected instance as `self`, so the method can read or update the right state.

When outputs surprise you, draw two records: `first.value` and `second.value`. Update only the record named by an assignment’s left side. Underline each `self.` access and bare local assignment. This makes class design, instance creation, attribute access, and local calculation visible.

The point of a class is not that it magically prevents mistakes. The point is that it gives related objects a common, named structure and common methods. Your job is still to ask which object a name reaches, where an assignment stores a value, and whether a method returns a result or changes state. Those are the same evidence-based habits we used with string and list methods.

<!-- slide id="recap-your-first-class" title="Recap your first class" claims="C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11" -->
For ordinary multi-line user-defined classes and ordinary method bodies as taught here, here is the working model. A class statement defines a class object: a repeatable type with named behavior and a place to describe its attributes. Calling the class creates an instance. `__init__` runs during a normal creation call so it can initialize that new instance. The first method parameter is conventionally `self`, which identifies the instance for that call. `self.value = start` stores state on that instance. `instance.value` reads it, and `instance.value = new_value` changes it.

For ordinary multi-line user-defined classes and ordinary method bodies as taught here, two instances made from one class can keep different values. The class gives them the same method definitions; it does not make their instance attributes one shared state. When a method needs to preserve a calculation on the object, use `self.attribute` on the assignment side. A bare name inside the method is local to that call and is not a persistent attribute. When a method uses `self`, it can work with whichever instance made the call.

Before you move on, explain each line in plain language: what type is being defined, which call creates which instance, what `self` refers to during the call, where the assignment stores its value, and which object a dot expression reaches. If those answers are clear, you have written your first class and have a reliable way to debug separate state.

## Podcast

<!-- claims: C1,C2,C11 -->
**DANA:** We already used string and list objects. Why do we need a class now?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, a program sometimes needs its own repeatable kind of object. A class lets us describe a named type with state and behavior together. Instead of keeping unrelated variables and separate functions for every counter, we can define what a counter object contains and what a counter object can do.

<!-- claims: C1,C2,C11 -->
**DANA:** Is a class just another variable, then?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, a class definition creates a class object. Its body supplies names such as methods and attributes, and the class object can be called to create instances. The class is the reusable definition; an instance is one object made from it. That distinction is why one definition can support many objects.

<!-- claims: C1,C2,C14 -->
**DANA:** What should I hear when I read `class Counter:`?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, hear “define a class named Counter,” followed by an indented body. The body is where the class’s methods and attribute-related setup go. At that moment you have defined the type; you have not yet made a particular counter with a particular value. The later call to `Counter(...)` makes that instance.

<!-- claims: C2,C3 -->
**DANA:** So what happens in `first = Counter(3)`?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, the class object is called, Python creates an instance of that class, and the resulting object is bound to `first`. If the class has an `__init__` method, Python calls it during that normal creation call. The argument `3` is available to that initializer so it can set the starting state.

<!-- claims: C2,C3,C4,C5 -->
**DANA:** I see `def __init__(self, start):` a lot. What does each name do?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, `start` is the argument carrying the requested starting value. `self` is conventionally the first parameter and receives the instance being initialized. A line such as `self.value = start` stores that argument in an attribute on that new instance. The initializer is where we give the object its initial state.

<!-- claims: C4,C10 -->
**DANA:** Is `self` a special object that exists once for the whole class?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, no. In an instance method, the first parameter is conventionally called `self`, and the call supplies the particular instance there. If `first.next_value()` runs, `self` refers to `first` during that call. If `second.next_value()` runs, `self` refers to `second`. The method definition is shared; the current instance is supplied for each call.

<!-- claims: C4,C5,C6 -->
**DANA:** Then `self.value` means the value belonging to the current instance?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, yes. The `self` part identifies the current instance, and the dot reaches its `value` attribute. When the initializer runs for `first`, `self.value = start` stores on `first`. When it runs for `second`, the same source line stores on `second`. The line is the same, but the instance named by `self` is different.

<!-- claims: C2,C6,C8 -->
**DANA:** Let’s make two counters with the same starting number. What should we expect?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, `first = Counter(3)` and `second = Counter(3)` are two calls, so they create two instance objects. They begin with equal values, but equal starting values do not turn them into one object. If you later assign `first.value = 4`, the attribute reached through `second` remains `3` unless you change it separately.

<!-- claims: C5,C6,C8 -->
**DANA:** That is the misconception I would make about ordinary multi-line user-defined classes and ordinary method bodies as taught here: same class means one shared value.

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, the class supplies common structure and method definitions. Attributes assigned through `self` are instance state, so corresponding attributes can differ between instances. To trace an assignment, look at the object before the dot. `first.value = 4` targets `first`; it does not announce a change to every instance made from the class.

<!-- claims: C5,C6,C8 -->
**DANA:** Does reading work the same way as changing?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, yes. `first.value` reads the current value on `first`. `second.value` reads the current value on `second`. An assignment such as `second.value = 10` stores through `second` and leaves `first.value` at its current value. The dot is the route to the selected object’s attribute in both the expression and the assignment.

<!-- claims: C4,C5,C9,C10 -->
**DANA:** How does a method know which counter it should use?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, the instance call supplies it. With `def next_value(self): return self.value + 1`, calling `first.next_value()` supplies `first` as `self`. The method reads the value through that `self`, adds one, and returns the result. Calling it through `second` uses the same method body with `second` as `self`.

<!-- claims: C5,C9 -->
**DANA:** Does `return self.value + 1` change the stored value?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, no. That line reads the attribute, computes a result, and returns it. It does not assign to the attribute. If the method should advance the stored value, it needs an assignment such as `self.value = self.value + 1`. A method can compute a result, update state, or do both; its statements determine which happens.

<!-- claims: C5,C7,C9 -->
**DANA:** What is the missing-`self.` bug?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, compare `value = self.value + amount` with `self.value = self.value + amount`. The first line assigns to a local name called `value` during the method call. The second line assigns to the current instance’s attribute. If you want a later dot read to see the new state, the left side must name the instance attribute with `self.`.

<!-- claims: C5,C7 -->
**DANA:** Does the local value disappear immediately?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, it is available to the method while that call is running. It is not stored as an instance attribute, so later code such as `counter.value` cannot see that local binding. If the method does not return the local value or store it through `self`, the calculation has no persistent place in the object. That is why the missing dot can look like a method that did nothing.

<!-- claims: C5,C7,C8 -->
**DANA:** Can we diagnose it from the output?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, yes. Start with a counter whose `value` is `5`. Run a method containing `value = self.value + 4`, then print `counter.value`; it is still `5`. Run a method containing `self.value = self.value + 4`, then print the attribute; it is `9`. The difference is the assignment target, not whether the arithmetic ran.

<!-- claims: C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11 -->
**DANA:** Let me trace the full sequence: class, two calls, initializer, attributes, then a method.

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, the class statement defines the repeatable type. Each call creates an instance and runs `__init__` for that instance. `self` identifies the current object during the call. An assignment through `self` stores state there. A dot read or assignment names the instance first, and a method call supplies that instance as its first argument.

<!-- claims: C4,C5,C6,C8 -->
**DANA:** What should I write down when I am unsure whether state is shared?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, write one row for each instance: `first.value` and `second.value`. Record their starting values. For every later assignment, update only the row named before the dot. If the code assigns through `self`, ask which instance is `self` during that call. This small trace makes separate state visible instead of relying on a vague picture of the class.

<!-- claims: C4,C5,C7,C9 -->
**DANA:** What if a method uses a bare name in one line and `self.value` in another?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, treat them as different destinations. A bare `value` is a local name for the method call. `self.value` is an attribute on the current instance. The first can support a temporary calculation or be returned. The second is where persistent object state lives for this example. Inspect the left side of the assignment before deciding what later code can read.

<!-- claims: C1,C6,C11 -->
**DANA:** Is every group of variables a reason to write a class?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, no. A class earns its place when several objects need the same named state and behavior. It gives those objects a common type and methods, which keeps the data-and-behavior relationship visible. For a one-line calculation, a class would add needless structure. For many counters, points, or similar objects, the repeatable definition is useful.

<!-- claims: C2,C3,C4,C5,C6 -->
**DANA:** What is the cleanest sentence for `Counter(3)`?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, say: “Call the Counter class to create one Counter instance initialized with a starting value of 3.” The call creates one object. The initializer receives that object as `self` and the number as `start`, then `self.value = start` stores the number on that instance. A second call repeats the process for a different object.

<!-- claims: C4,C5,C9,C10 -->
**DANA:** And for `first.next_value()`?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, say: “Call the instance method through first, supplying first as self.” The method then reads `self.value`, so it reads the value on `first`. If the body returns `self.value + 1`, the call sends back a computed result. If the body assigns to `self.value`, the call also changes the stored state.

<!-- claims: C2,C5,C6,C7,C8 -->
**DANA:** What final check should I use before I trust my class?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, create two instances with visibly different starting values. Print both attributes. Change one through dot notation and print both again. Then call a method on each. If one change appears in both objects, inspect whether you deliberately used shared class-level data; assignments through `self` should be instance state. If a change vanishes, inspect for a missing `self.` on the assignment target.

<!-- claims: C1,C2 -->
**DANA:** Why call the class a class object instead of just saying it is a type?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, the class name refers to an object that represents the defined type. We can call that class object to create an instance, and the class object has the definitions from its body. Saying “class object” helps us keep the definition itself separate from each object created by calling it.

<!-- claims: C2,C3,C4,C5 -->
**DANA:** Does `__init__` run once when the class is defined?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, no. It runs during each normal instance-creation call. If the program calls `Counter(3)` and then `Counter(8)`, the initializer runs for the first new object and then for the second new object. Each call supplies its own argument and its own current instance for `self`.

<!-- claims: C2,C3,C4,C5,C6 -->
**DANA:** If two counters start at `3`, are their values linked because they match?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, no. Equal values are an observation about two objects, not proof that there is one object. Each initializer call assigns through its own `self`, so the two instances have separate `value` attributes. Change one attribute and then read the other to test that independence.

<!-- claims: C5,C8 -->
**DANA:** How should I read `first.value = 9` aloud?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, say, “store `9` in the `value` attribute reached through `first`.” The expression before the dot identifies the target instance. This is different from saying “set the Counter value everywhere.” Dot assignment is specific to the object named before the dot in this example.

<!-- claims: C3,C4,C5,C9 -->
**DANA:** How should I read `self.value = start` inside `__init__`?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, say, “store the `start` argument in the `value` attribute of the instance receiving this initializer call.” `self` names that current instance inside the method. The parameter and attribute have related values, but they are not the same name or the same storage location.

<!-- claims: C4,C9,C10 -->
**DANA:** Why does the method definition need `self` if the call already has `first` before the dot?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, the call syntax is how Python supplies the receiving instance. The method body still needs a parameter name through which to access that instance. Conventionally that name is `self`, so the body can use `self.value` regardless of which instance made the call.

<!-- claims: C5,C7,C9 -->
**DANA:** Could I write `value = self.value + amount` and then expect `counter.value` to find it?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, no. The bare left side names a local binding for the method call. `counter.value` looks for an attribute on the instance, not for a local variable that belonged to a completed call. Use `self.value = self.value + amount` when the result should become persistent instance state.

<!-- claims: C5,C7 -->
**DANA:** Is a local variable always an error in a method?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, no. A local variable is useful for temporary work, and a method can return it. The error is expecting a bare local name to update an attribute automatically. Decide whether the value is temporary or part of the object’s state, then choose a bare name or a `self.` attribute as the assignment target.

<!-- claims: C5,C6,C8 -->
**DANA:** What evidence would show that I accidentally changed the wrong object?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, print both `first.value` and `second.value` before and after the assignment. If only the value reached through the named target changes, the dot assignment is behaving as expected. If you expected both to change, you need to identify an explicit shared design; ordinary instance attributes assigned through `self` are separate in this lesson.

<!-- claims: C2,C3,C4,C5,C6 -->
**DANA:** Could the initializer use a different starting argument for each object without changing its code?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, yes. The same initializer definition can receive `3` in one call and `8` in another. The argument goes to `start`, while the instance supplied as `self` changes with the call. That is how one class definition prepares instances with different starting state.

<!-- claims: C5,C9,C10 -->
**DANA:** What is the difference between a method that returns and one that updates?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, a return statement sends a result back to the caller. An assignment through `self`, such as `self.value = ...`, updates the instance attribute. A method can do either one or both. `return self.value + 1` computes and sends back a number but does not update the stored value by itself.

<!-- claims: C1,C2,C6,C8 -->
**DANA:** Why is testing two objects better than testing only one?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, one object can show that a class works at all, but two objects test whether state is kept separately. Give them different starting values, change one, and read both. That sequence makes a mistaken assumption about one shared state visible in the output.

<!-- claims: C5,C7,C8 -->
**DANA:** What is the fastest place to look when a method seems not to save a change?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, inspect the assignment target. `self.value` names instance state, while `value` names a local binding in the method. Then print the attribute through the same instance that made the call. Those two checks distinguish a missing `self.` from a change made to a different object.

<!-- claims: C1,C6,C11 -->
**DANA:** So the class is mainly a way to keep a design reusable?

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, yes. It packages a named type with the methods and attribute setup its instances need. The benefit appears when several objects share that design but hold different current values. You write the structure once, then create and inspect each instance separately.

<!-- claims: C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11 -->
**DANA:** So my first-class checklist is: define the type, initialize each instance, use `self`, trace the dot, and test two objects.

**MARCUS:** For ordinary multi-line user-defined classes and ordinary method bodies as taught here, exactly. A class gives you a repeatable type. Calling it creates instances. `__init__` establishes starting state. `self` identifies the current instance for a method call. Dot notation reads or changes the selected attribute. Two instances can keep separate state, and a bare local name is not a substitute for `self.attribute` when the result must persist.

## Worked examples

### class-object-basics

```python
class Dog:
    def __init__(self, label):
        self.label = label

    def greeting(self):
        return f"{self.label} says hi"

one = Dog("small")
print(type(Dog).__name__)  # expect: type
print(type(one).__name__)  # expect: Dog
print(one.label)  # expect: small
print(one.greeting())  # expect: small says hi
```

### separate-instance-state

```python
class Counter:
    def __init__(self, start):
        self.value = start

    def add(self, amount):
        self.value = self.value + amount

first = Counter(3)
second = Counter(8)
print(first.value)  # expect: 3
print(second.value)  # expect: 8
first.add(2)
print(first.value)  # expect: 5
print(second.value)  # expect: 8
second.value = 11
print(first.value)  # expect: 5
print(second.value)  # expect: 11
```

### local-vs-instance

```python
class Counter:
    def __init__(self, start):
        self.value = start

    def wrong_add(self, amount):
        value = self.value + amount

    def add(self, amount):
        self.value = self.value + amount

counter = Counter(5)
counter.wrong_add(4)
print(counter.value)  # expect: 5
counter.add(4)
print(counter.value)  # expect: 9
```

### review-string-method

```python
word = "code"
upper_word = word.upper()
print(upper_word)  # expect: CODE
print(word)  # expect: code
```

### review-list-method

```python
items = ["red"]
result = items.append("blue")
print(items)  # expect: ['red', 'blue']
print(result)  # expect: None
```

## Misconception

Instances made from the same class all use one shared state, so changing `first.value` should change `second.value` too. In fact, for ordinary multi-line user-defined classes and ordinary method bodies as taught here, attributes assigned through `self` are state on the current instance: two calls to the class create two instance objects, and each initializer stores its argument on the instance passed as `self`. A dot assignment targets the instance before the dot. Related confusions: equal starting values mean one object; the class object, current instance, and `self` are the same thing; a method argument goes into `self`; every assignment in a method becomes persistent state; and a bare local name is an attribute. The related trap is writing `value = ...` when the intended destination is `self.value`; the bare name is local to that call and is not persistent instance state.

claims: C1,C2,C3,C4,C5,C6,C7,C8,C10

## Quiz

### Q1

- prompt: What does a class definition primarily provide in this lesson?
- choices:
  - A: A repeatable type whose instances can have named state and behavior
  - B: One shared state record that every object made from the class must use
  - C: A variable that permanently stores the value for every future instance
  - D: One instance whose state all future instances must share
- answer: A
- rationale: A class definition provides a repeatable type and class body for methods and attributes; calling the class later creates instances. B targets the shared-instance-state confusion. C targets the sibling confusion that the class stores one value for every future instance. D targets the sibling confusion that a class is one instance whose state every call must share.
- claims: C1,C2,C6,C11

### Q2

- prompt: After `first = Counter(3)`, `second = Counter(8)`, and `first.value = 4`, what are the values of `first.value` and `second.value`?
- choices:
  - A: Both are `4`, because both instances came from `Counter`
  - B: `first.value` is `4` and `second.value` is `8`
  - C: Both are `8`, because the second initializer replaces the first state
  - D: Neither has a value, because `self` is shared by the class
- answer: B
- rationale: Each call creates a separate instance, and `first.value = 4` targets only the instance named `first`; the corresponding attribute on `second` remains `8`. A targets shared instance state, C targets one initializer replacing another object’s state, and D targets the confusion that `self` is one class-wide object.
- claims: C2,C4,C6,C8

### Q3

- prompt: In `def add(self, amount):`, what does `self` identify when `first.add(2)` is called?
- choices:
  - A: The class object `Counter`
  - B: The number `2`
  - C: The particular instance `first`
  - D: One shared variable used by every counter
- answer: C
- rationale: The instance call supplies the particular instance as the method’s first parameter, conventionally named `self`; `amount` receives `2`. A targets the class-object/current-instance confusion, B targets the argument-mapping confusion between `self` and `amount`, and D targets the shared-`self` confusion.
- claims: C1,C2,C4,C6,C10

### Q4

- prompt: What is the effect of this method on a counter whose value is `5`? `def add(self, amount): value = self.value + amount`
- choices:
  - A: It stores the new total in the instance automatically because `value` and `self.value` mean the same thing
  - B: It changes every counter made from the class
  - C: It computes a local value, but it does not update the instance attribute
  - D: It changes the instance attribute because every method assignment is persistent
- answer: C
- rationale: The bare name `value` is local to the method call. The instance attribute would be updated only by assigning to `self.value`, such as `self.value = self.value + amount`. A targets the sibling confusion that a bare name and `self.value` are the same destination; B targets shared instance state; D targets the sibling confusion that every method assignment persists on the object.
- claims: C5,C6,C7,C9

### Q5

- prompt: Which explanation best fits `return self.value + 1` inside an instance method?
- choices:
  - A: It reads the calling instance’s value, computes one more, and returns that result without assigning it back
  - B: It changes the value on every instance of the class
  - C: It creates a local `self` object that is discarded after the call
  - D: It always changes the calling instance because reading an attribute mutates it
- answer: A
- rationale: `self` identifies the instance that made the call, so the expression reads that instance’s attribute and returns a computed result. There is no assignment to `self.value`, so the stored attribute is not changed by this line. B targets shared instance state, C targets the class-object/current-instance confusion, and D targets the sibling confusion that reading an attribute mutates it; the line only returns a result.
- claims: C1,C4,C5,C6,C9,C10

## Review

### R1

- prompt: If `word = "code"`, what happens when `upper_word = word.upper()` runs?
- choices:
  - A: `word` is changed in place and `upper_word` is `None`
  - B: `upper_word` receives the uppercase string and `word` remains unchanged
  - C: Both names refer to a list of uppercase characters
  - D: The call changes every string in the program
- answer: B
- rationale: `upper()` returns a string result, and the original string value is unchanged; assigning the result gives that returned string to `upper_word`.
- claims: C12

### R2

- prompt: After `items = ["red"]` and `result = items.append("blue")`, which statement is true?
- choices:
  - A: `items` is `['red', 'blue']` and `result` is `None`
  - B: `items` is unchanged and `result` is the expanded list
  - C: `items` is `None` and `result` is the expanded list
  - D: `items` and `result` are two equal expanded lists
- answer: A
- rationale: `append` changes the list in place and returns `None`, so the list contains both items while the saved return value is `None`.
- claims: C13

## Sources

- S1
- S2
- S3
- S4
- S5
- S6
- S7
- S8
