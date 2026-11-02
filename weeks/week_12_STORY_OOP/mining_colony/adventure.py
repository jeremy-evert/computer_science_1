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
