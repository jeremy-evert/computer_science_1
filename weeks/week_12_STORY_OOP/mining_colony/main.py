class Story:
    def __init__(self, title, setting):
        self.title = title
        self.setting = setting

    def introduce(self):
        print(f"Welcome to {self.title}!")
        print(f"Far away, {self.setting} waits.")
        print("A ship arrives with a brave crew ready to dig deep.")
        print("What they uncover could change the stars forever!")


def main():
    science_fiction_object = Story(
        "Deep Core Colony",
        "a mining colony on the edge of the asteroid belt",
    )
    sfo = science_fiction_object
    sfo.introduce()
    print(sfo is science_fiction_object)


if __name__ == "__main__":
    main()
