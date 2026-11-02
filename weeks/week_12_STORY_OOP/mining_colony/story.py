class Story:
    def __init__(self, title, setting, main_character):
        self.title = title
        self.setting = setting
        self.main_character = main_character

    def introduce(self):
        print(f"Welcome to {self.title}!")
        print(f"Far away, {self.setting} waits.")
        print(f"Our hero is {self.main_character}.")



