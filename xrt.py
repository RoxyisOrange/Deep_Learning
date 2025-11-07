class Cat:
    def __init__(self, name: str):
        self.name = name


class Shawn(Cat):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
