print("THE MONDAY COFFEE INCIDENT")
print("Give me some words. Sensible answers are permitted, but discouraged.\n")

name = input("A person's name: ").strip().title()
animal = input("An animal: ").strip().lower()
adjective = input("An adjective: ").strip().lower()
object_name = input("An object: ").strip().lower()
place = input("A place: ").strip().title()
sound = input("A sound: ").strip().upper()

story = (
    f"\nOn Monday morning, {name} arrived at {place} carrying a {adjective} "
    f"{object_name}.\n"
    f"Unfortunately, a {animal} had already claimed the coffee machine.\n"
    f'"{sound}!" shouted the {animal}.\n'
    f'{name} replied, "I have not had coffee. You are now the professor."\n'
)

print("\n--- YOUR MAD LIB ---")
print(story)

print("--- STRING LAB: WHAT JUST HAPPENED? ---")
print(f"Name after .strip().title(): {name!r}")
print(f"Animal after .strip().lower(): {animal!r}")
print(f"Sound after .strip().upper(): {sound!r}")

print(f"\nThe name has {len(name)} characters.")
print(f"The first character of the name is {name[0]!r}." if name else
      "The name is empty, so it has no first character.")
print(f"The first three characters of the place are {place[:3]!r}.")

print(f"\nDoes the story contain 'coffee'? {'coffee' in story.lower()}")
print(f"How many times does 'coffee' appear? {story.lower().count('coffee')}")

louder_story = story.replace("coffee", "COFFEE")
print("\nAfter .replace('coffee', 'COFFEE'):")
print(louder_story)

words = story.split()
print(f"The story contains {len(words)} whitespace-separated words.")
print("The first five words, joined with |: " + " | ".join(words[:5]))

print("\nOriginal story still begins:")
print(story.splitlines()[1])