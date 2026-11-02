# Python OOP and Modules: Stories with Main Characters

## Learning goal

Use one `Story` class from a shared module to build two separate story objects. Each object stores its own title, setting, and main character.

## Step 1: Define the shared class

Save this as `story.py`:

```python
class Story:
    def __init__(self, title, setting, main_character):
        self.title = title
        self.setting = setting
        self.main_character = main_character

    def introduce(self):
        print(f"Welcome to {self.title}!")
        print(f"Far away, {self.setting} waits.")
        print(f"Our hero is {self.main_character}.")
```

`Story` is a class: a template for creating story objects. `__init__` runs when an object is created and saves the supplied values on that object. The `introduce()` method uses the saved values to print the story opening.

## Step 2: Create a science fiction story

Save this as `science_fiction_story.py`:

```python
from story import Story


def main():
    science_fiction_story = Story(
        title="Deep Core Colony",
        setting="a mining colony on the edge of the asteroid belt",
        main_character="Captain Garnie",
    )
    science_fiction_story.introduce()


if __name__ == "__main__":
    main()
```

Run it with:

```text
python science_fiction_story.py
```

Output:

```text
Welcome to Deep Core Colony!
Far away, a mining colony on the edge of the asteroid belt waits.
Our hero is Captain Garnie.
```

## Step 3: Create an adventure story

Save this as `adventure.py`:

```python
from story import Story


def start_adventure():
    adventure_story = Story(
        title="The Enchanted Forest",
        setting="you wake up in the magic forest covered in magic dust, with a bunch of weird glowing mushrooms with eyes dancing around",
        main_character="Gerb",
    )
    adventure_story.introduce()


if __name__ == "__main__":
    start_adventure()
```

Run it with:

```text
python adventure.py
```

Output:

```text
Welcome to The Enchanted Forest!
Far away, you wake up in the magic forest covered in magic dust, with a bunch of weird glowing mushrooms with eyes dancing around waits.
Our hero is Gerb.
```

## What to notice

- Both story files import `Story` from `story.py`. One change to that shared class affects both stories.
- Adding a required parameter to `__init__` means every place that creates a `Story` must supply it. If one call leaves out `main_character`, Python raises a `TypeError` because a required argument is missing.
- `self` refers to the particular object currently being initialized or used. `self.main_character` belongs to that one story object, so Captain Garnie and Gerb remain separate.
- `science_fiction_story` and `adventure_story` are two different objects created from the same class. Each object has its own title, setting, and character.
- Keyword arguments such as `main_character="Gerb"` name the value being supplied, making the constructor call easier to scan.
- The `if __name__ == "__main__":` guard runs the function when a file is executed directly, while allowing the file to be imported without automatically starting the story.

## Small extension prompt

Add a third story in a new module. Import `Story`, choose a title, setting, and main character, then call `introduce()`. The shared class should not need another change.
