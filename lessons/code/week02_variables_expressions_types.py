"""week02_variables_expressions_types.py

Runnable companion to lessons/02-variables-expressions-types.md (CS1, Week 2).

Every example below is adapted from Deitel & Deitel, *Intro to Python for
Computer Science and Data Science* (2020), Chapter 2, "Introduction to
Python Programming," sections 2.2-2.8 (variables/assignment, arithmetic,
print/strings, input, if/comparison, objects/dynamic typing), plus the
official Python documentation:

  - Numeric types:            https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
  - Formatted string literals: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
  - Built-in functions int/float/str/bool:
      https://docs.python.org/3/library/functions.html#int
      https://docs.python.org/3/library/functions.html#float
      https://docs.python.org/3/library/functions.html#func-str
      https://docs.python.org/3/library/functions.html#bool
  - Operator precedence:      https://docs.python.org/3/reference/expressions.html#operator-precedence
  - Style Guide for Python Code (PEP 8): https://peps.python.org/pep-0008/

Run it with no input required:

    python3 week02_variables_expressions_types.py

Every section prints a label before its output so you can match what you
see back to the corresponding part of the lecture and lesson page.
"""


def variables_and_assignment() -> None:
    """Deitel 2.2 -- creating variables, running a calculation, and saving
    the result for later use."""
    print("--- 2.2 Variables and Assignment Statements ---")
    x = 7
    y = 3
    print(f"x = {x}, y = {y}")
    print(f"x + y = {x + y}")

    total = x + y  # the right side always evaluates first
    print(f"total = x + y -> total = {total}")


def arithmetic_and_precedence() -> None:
    """Deitel 2.3 -- the arithmetic operators, true vs. floor division, the
    remainder operator, and why parentheses change a result."""
    print("\n--- 2.3 Arithmetic ---")
    print(f"7 * 4   = {7 * 4}")          # multiplication
    print(f"2 ** 10 = {2 ** 10}")        # exponentiation
    print(f"9 ** (1 / 2) = {9 ** (1 / 2)}")  # square root via exponent 0.5

    print(f"7 / 4   = {7 / 4}   (true division -> float)")
    print(f"7 // 4  = {7 // 4}  (floor division -> truncated int)")
    print(f"-13 / 4  = {-13 / 4}")
    print(f"-13 // 4 = {-13 // 4}  (rounds toward negative infinity, not zero)")

    print(f"17 % 5  = {17 % 5}   (remainder operator)")

    # Parentheses are not decoration -- they change which operator group
    # evaluates first, exactly like algebra.
    print(f"10 * (5 + 3) = {10 * (5 + 3)}")
    print(f"10 * 5 + 3   = {10 * 5 + 3}")


def types_and_dynamic_typing() -> None:
    """Deitel 2.8 -- every value is an object with a type; a variable can be
    rebound to a value of a different type at any time (dynamic typing)."""
    print("\n--- 2.8 Objects and Dynamic Typing ---")
    x = 7
    print(f"x = {x!r}, type(x) = {type(x)}")
    x = 4.1
    print(f"x = {x!r}, type(x) = {type(x)}")
    x = "dog"
    print(f"x = {x!r}, type(x) = {type(x)}")

    # bool is a subtype of int (docs.python.org/3/library/stdtypes.html)
    flag = True
    print(f"flag = {flag}, type(flag) = {type(flag)}, flag + flag = {flag + flag}")


def formatted_output() -> None:
    """Deitel 2.4 -- print with multiple arguments -- plus f-strings, which
    the book introduces later but which are the modern, recommended way to
    build formatted output (docs.python.org's Formatted String Literals)."""
    print("\n--- 2.4 print and formatted output ---")
    print("Sum is", 7 + 3)  # Deitel-style comma-separated print

    price = 19.999
    print(f"Price: ${price:.2f}")  # f-string with a format spec: 2 decimals
    name = "Ada"
    count = 3
    print(f"{name} bought {count} item{'s' if count != 1 else ''}.")


def conversion_and_input_pattern() -> None:
    """Deitel 2.6 -- input() always returns a string; convert with int()/
    float() before doing arithmetic, or you get string concatenation
    instead of addition."""
    print("\n--- 2.6 Conversion (input always returns str) ---")
    value1 = "7"    # stand-in for input('Enter first number: ')
    value2 = "3"    # stand-in for input('Enter second number: ')
    print(f"value1 + value2 (as strings) = {value1 + value2!r}  <- concatenation, not addition")

    total = int(value1) + int(value2)
    print(f"int(value1) + int(value2) = {total}")

    print(f"float('6.2') * 3.3 = {float('6.2') * 3.3}")
    print(f"str(42) -> {str(42)!r}, type is {type(str(42))}")


def caffeine_half_life(initial_mg: float) -> None:
    """The historical CS1 lab this course has assigned since at least Fall
    2021 (see lessons/02-variables-expressions-types.md's 'Historical
    materials' note and computer_science_1/archive/fall-2021): caffeine's
    half-life in humans is about 6 hours, so the amount remaining after t
    hours is initial_mg * 0.5 ** (t / 6). This is Deitel 2.3's exponentiation
    operator (**) and Deitel 2.4's formatted output, applied to one real
    problem instead of two separate toy examples."""
    print("\n--- Historical lab: caffeine half-life, formatted output ---")
    half_life_hours = 6
    for hours in (6, 12, 24):
        remaining = initial_mg * 0.5 ** (hours / half_life_hours)
        print(f"After {hours:>2} hours: {remaining:6.2f} mg remain "
              f"(started at {initial_mg} mg)")


def try_it_yourself_with_real_input() -> None:
    """Uncomment and run this function's body interactively to see Deitel
    2.6's input()/int() pattern with your own numbers -- left commented out
    so this file runs unattended (e.g. in an autograder) with no prompts."""
    # value = input("Enter an integer: ")
    # value = int(value)
    # print(f"You entered {value}, type {type(value)}")
    pass


if __name__ == "__main__":
    variables_and_assignment()
    arithmetic_and_precedence()
    types_and_dynamic_typing()
    formatted_output()
    conversion_and_input_pattern()
    caffeine_half_life(initial_mg=100.0)
