"""week02_practice_problems.py

Optional, ungraded, self-checking companion to the "Optional extra
practice" section of lessons/02-variables-expressions-types.md (CS1,
Week 2).

**This is not the Coding Odyssey Gate and not a substitute for it.** The
real graded weekly deliverable is `assignments/odyssey_gates/week-02.md`
(see `assignments/A1-weekly-coding-practice.md`: "no separate chapter
problem set is due"). Nothing here is submitted, collected, or scored.
These eight problems are deliberately decontextualized -- no settlement,
case file, starship, or business -- plain Deitel/Python-docs-style
exercises on the raw mechanic (variable assignment, arithmetic and
precedence, formatted output, conversion, and type errors), for a student
who wants extra reps on the mechanic itself before attempting the gate
(which already has its own optional genre-flavored scaffolding -- a
different, narrative-embedded thing from this file).

Every problem below is followed immediately by an `assert` that checks the
stated answer is actually correct, so running this file *is* the answer
key: if it finishes with no `AssertionError`, every answer printed was
verified against real Python, not just asserted in prose.

Run it with no input required:

    python3 week02_practice_problems.py

Source concepts: Deitel & Deitel, *Intro to Python for Computer Science
and Data Science* (2020), Ch. 2, sections 2.2-2.4, 2.6, 2.8 -- the same
sections `week02_variables_expressions_types.py` and the lesson page
cite; no new source material introduced here.
"""


def problem_1_precedence() -> None:
    """Predict the output. c = a + b * 2, with a = 5, b = 2."""
    print("--- Problem 1: predict the output ---")
    print("a = 5")
    print("b = 2")
    print("c = a + b * 2")
    print("print(c)")
    a = 5
    b = 2
    c = a + b * 2  # b * 2 evaluates first (precedence), then a + 4
    print(f"Answer: {c}")
    assert c == 9, "multiplication binds tighter than addition (Deitel 2.3)"


def problem_2_division_operators() -> None:
    """Predict the output of /, //, and % on 17 and 5."""
    print("\n--- Problem 2: predict the output (three lines) ---")
    print("print(17 / 5)")
    print("print(17 // 5)")
    print("print(17 % 5)")
    true_div = 17 / 5
    floor_div = 17 // 5
    remainder = 17 % 5
    print(f"Answer: {true_div}, {floor_div}, {remainder}")
    assert true_div == 3.4
    assert floor_div == 3
    assert remainder == 2


def problem_3_fix_the_type_error() -> None:
    """Fix the type error in a buggy snippet: age + 1 where age came from
    input() and is therefore a str."""
    print("\n--- Problem 3: fix the type error ---")
    print("age = input('Enter your age: ')  # age is a str")
    print("next_year = age + 1              # buggy: TypeError")
    age = "17"  # stand-in for input(), same convention as the lecture script
    next_year = int(age) + 1  # the fix: convert before arithmetic
    print(f"Fixed: next_year = int(age) + 1 -> {next_year}")
    assert next_year == 18


def problem_4_write_formatted_price() -> None:
    """Write one line: print price formatted to 2 decimal places with a
    leading dollar sign."""
    print("\n--- Problem 4: write one line ---")
    print("Given price = 42.5, print it as a 2-decimal dollar amount.")
    price = 42.5
    formatted = f"${price:.2f}"
    print(f"Answer: print(f'${{price:.2f}}') -> {formatted}")
    assert formatted == "$42.50"


def problem_5_dynamic_typing() -> None:
    """Predict the output of type(x) after x is rebound to a new type."""
    print("\n--- Problem 5: predict the output ---")
    print("x = 10")
    print("x = 'ten'")
    print("print(type(x))")
    x = 10
    x = "ten"
    result_type = type(x)
    print(f"Answer: {result_type}")
    assert result_type is str, "Python is dynamically typed (Deitel 2.8)"


def problem_6_string_concatenation_trap() -> None:
    """What does value1 + value2 print when both are strings that look
    like numbers?"""
    print("\n--- Problem 6: what does this print? ---")
    print("value1 = '4'")
    print("value2 = '5'")
    print("print(value1 + value2)")
    value1 = "4"
    value2 = "5"
    result = value1 + value2
    print(f"Answer: {result!r} (concatenation, not addition -- both are str)")
    assert result == "45"


def problem_7_name_the_exceptions() -> None:
    """Identify which exception each of three snippets raises, then
    confirm each one for real."""
    print("\n--- Problem 7: name the exception each line raises ---")
    print("print(5 / 0)          -> ?")
    print("print(int('hello'))   -> ?")
    print("print(z + 1)          -> ? (z never assigned)")

    exceptions_seen = []
    try:
        5 / 0
    except ZeroDivisionError as exc:
        exceptions_seen.append(type(exc).__name__)

    try:
        int("hello")
    except ValueError as exc:
        exceptions_seen.append(type(exc).__name__)

    try:
        z + 1  # noqa: F821 -- deliberately undefined, that's the point
    except NameError as exc:
        exceptions_seen.append(type(exc).__name__)

    print(f"Answer, in order: {', '.join(exceptions_seen)}")
    assert exceptions_seen == ["ZeroDivisionError", "ValueError", "NameError"]


def problem_8_write_exponent() -> None:
    """Write one line: store 3 ** 4 in a variable named total, then print
    it."""
    print("\n--- Problem 8: write one line ---")
    print("Store 3 ** 4 in a variable named total, then print it.")
    total = 3**4
    print(f"Answer: total = 3 ** 4 -> {total}")
    assert total == 81


if __name__ == "__main__":
    problem_1_precedence()
    problem_2_division_operators()
    problem_3_fix_the_type_error()
    problem_4_write_formatted_price()
    problem_5_dynamic_typing()
    problem_6_string_concatenation_trap()
    problem_7_name_the_exceptions()
    problem_8_write_exponent()
    print("\nAll answers verified -- every assert above passed.")
