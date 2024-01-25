from rectangle import *

class Cube(Rectangle):
    def __init__(self, length: float, width: float, height: float):
        super().__init__(length, width)
        self.height = height

    def volume(self) -> float:
        return self.length * self.width * self.height