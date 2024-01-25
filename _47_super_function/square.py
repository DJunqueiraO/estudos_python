from rectangle import *

class Square(Rectangle):
    def __init__(self, length: float, width: float):
        super().__init__(length, width)

    def area(self) -> float:
        return self.length * self.width