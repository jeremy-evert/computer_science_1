class Rover:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def status(self):
        return f"{self.name} has {self.battery}% battery."


scout = Rover("Scout", 80)
print(scout.name)
print(scout.battery)
print(scout.status())
