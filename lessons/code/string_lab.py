"""String Laboratory: what is this thing, and what can it do?

Run from the repository root: python3 lessons/code/string_lab.py
"""

print("STRING LABORATORY")
print("Predict each result, then run the program and compare.")
print("Dot notation: object.method() asks an object to use a behavior.")
print("In text.upper(), text is the object and upper() is the method call.")

text = "  The Bulldogs Have ESCAPED Again!  "
print()
print("1. String behaviors")
# Quotes make the spaces at the beginning and end visible.
print(f'Original text: "{text}"')
print(f'text.strip(): "{text.strip()}"')
print(f'text.lower(): "{text.lower()}"')
print(f'text.upper(): "{text.upper()}"')
print(f'text.title(): "{text.title()}"')
print(f'text.replace("Bulldogs", "Geese"): "{text.replace("Bulldogs", "Geese")}"')
print("text.split():", text.split())
print("split() returns a list of words; it splits on whitespace by default.")
print('text.count("a"):', text.count("a"))
print('text.find("Bulldogs"):', text.find("Bulldogs"))
print("find() returns the first matching position, counting from zero.")
print('text.find("Geese"):', text.find("Geese"))
print("A result of -1 means the text was not found.")
print('text.startswith("The"):', text.startswith("The"))
print('text.endswith("!"):', text.endswith("!"))
print("Those checks are False because the original has spaces at both ends.")

clean_text = text.strip()
print('clean_text.startswith("The"):', clean_text.startswith("The"))
print('clean_text.endswith("!"):', clean_text.endswith("!"))
print("count() and find() return integers; startswith() and endswith() return booleans.")
print(f'Original text after all those calls: "{text}"')

print()
print("2. Strings are immutable: their contents cannot be changed in place")
name = "jeremy"
print("Before calling upper():", name)
name.upper()
print("After name.upper() without saving its result:", name)
print("upper() returned an uppercase string, but we did not save it.")
name = name.upper()
print("After name = name.upper():", name)
print("Assignment makes name refer to the returned string.")
print("It does not change the contents of the original string.")

print()
print("3. Object detective: discover rather than memorize")
print("type(text):", type(text))
print("str is Python's string type. Our object has a text value and string behaviors.")
print("dir(text):", dir(text))
print("dir() lists available names, including methods such as replace.")
print("Names with double underscores are special; start with the familiar method names.")
print("help(str.replace): read what replace accepts and returns")
help(str.replace)
print("Try changing the words in text.replace() and predicting the returned string.")
