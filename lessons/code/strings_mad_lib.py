"""Live Mad Lib opener for Strings Are Objects.

Run from the repository root: python3 lessons/code/strings_mad_lib.py
"""

print("The Great Campus Goose Emergency")
print("Give Python six silly answers. Try extra spaces and MIXED capitals!")
print()

raw_name = input("A made-up hero's name: ")
# Save the returned string so we can use the cleaned-up name in the story.
name = raw_name.strip().title()
adjective = input("An adjective (like wobbly): ").strip().lower()
noun = input("A singular noun (like toaster): ").strip().lower()
place = input("A place (like the moon): ").strip().title()
verb = input("A verb (like dance, not dancing): ").strip().lower()
absurd_thing = input("Something absurd (like a committee of rubber ducks): ").strip().lower()

print()
print(f'Name as typed: "{raw_name}"')
print(f'Name after .strip().title(): "{name}"')
print()

story = f"""BREAKING NEWS FROM {place}!
{name} arrived at {place} carrying a very {adjective} {noun}.
A campus goose blocked the door and declared, "To pass, you must {verb}!"
{name} tried to {verb}, but accidentally summoned {absurd_thing}.
The goose appointed the {noun} dean. Classes now meet at the duck pond.
{name} would like a refund."""

print(story)
