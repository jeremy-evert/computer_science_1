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
