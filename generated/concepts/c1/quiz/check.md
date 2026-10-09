# Knowledge check

## Quiz

### Q1

Which description best fits a value such as a string or list in Python?

- A: An object with a type, state or value, and behaviors
- B: A variable name that permanently is the object's type
- C: A value whose methods must change it in place and return nothing
- D: A mutable container, because every object can change in place

<details>
<summary>Answer and rationale</summary>

- Answer: A
- Rationale: The first object model asks what kind of thing a value is, what it holds, and what it can do. B targets the related confusion that a name is the type. C and D target the misconception that methods must change objects in place or return nothing.

</details>

### Q2

What does this call do to the original string when its result is not saved: `s.upper()`?

- A: It changes the original string in place
- B: It returns a string result and leaves the original unchanged
- C: It returns `None` after changing the original string
- D: It returns `None` and leaves the original unchanged

<details>
<summary>Answer and rationale</summary>

- Answer: B
- Rationale: Strings are immutable. The call returns a string; the original is unchanged. A targets the misconception that a method changes the original. C targets expecting an in-place change and no useful return value. D targets expecting a method to return nothing instead of a value; assigning the string result is what makes a name refer to the returned text.

</details>

### Q3

After `items.append("blue")`, which statement is correct?

- A: The list is unchanged and append returns an expanded list
- B: The list changes in place and append returns None
- C: The list changes in place and append returns the changed list
- D: The list changes in place, but append returns a new list

<details>
<summary>Answer and rationale</summary>

- Answer: B
- Rationale: Lists are mutable sequences; append adds to the existing list and returns None. A targets expecting no mutation and an expanded return value. C targets expecting the in-place method to return the changed list. D targets expecting a new list value instead of the documented no-value return.

</details>

### Q4

What kind of value does a string split method return?

- A: The original string changes in place and becomes the pieces
- B: A list of pieces
- C: Nothing is returned; split only changes the original string
- D: The original string changes in place and split returns `None`

<details>
<summary>Answer and rationale</summary>

- Answer: B
- Rationale: Split is a string method whose result is a list; the original string is unchanged. A targets expecting a method to mutate the original. C targets expecting a method to return nothing. D combines both parts of the misconception: it expects an in-place change and a `None` result.

</details>

### Q5

Which investigation sequence is the best way to explore an unfamiliar object?

- A: Use `type`, inspect names with `dir`, read focused `help`, then run a small test
- B: Use `type`, call every name from `dir` because `dir` lists only methods you must call, and skip `help`
- C: Call every name from `dir` because `dir` lists only methods you must call; errors mean the object is broken
- D: Assume every method changes the original and returns nothing

<details>
<summary>Answer and rationale</summary>

- Answer: A
- Rationale: `type` identifies the object, `dir` helps discover names, `help` explains a type or method, and a small experiment checks a prediction. B and C target the related confusion that `dir` lists only methods you must call. D targets the misconception that every method changes the original and returns nothing.

</details>

## Spaced review

### R1

Given `word = "code"`, which expression produces `"o"` while `len(word)` produces `4`?

- A: `word[1]`
- B: `word[0]`
- C: `word[4]`
- D: `word[len(word)]`

<details>
<summary>Answer and rationale</summary>

- Answer: A
- Rationale: String indexing starts at zero, so index 1 selects the second character, `o`; the length is four.

</details>

### R2

If `place = "home"` and `count = 2`, what does `f"{place}: {count}"` produce?

- A: `"place: count"`
- B: `"home: 2"`
- C: `"home2"`
- D: `"{place}: {count}"`

<details>
<summary>Answer and rationale</summary>

- Answer: B
- Rationale: An f-string evaluates the expressions inside braces and inserts their values into the surrounding text.

</details>
