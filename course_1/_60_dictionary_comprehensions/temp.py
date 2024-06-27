from enum import Enum

class Temp(Enum):
    COLD = 0
    WARM = 1
    HOT = 2

    @staticmethod
    def check(temp: int):
        if temp >= 70:
            return Temp.HOT
        elif temp >= 40:
            return Temp.WARM
        else:
            return Temp.COLD

    def __str__(self) -> str:
        return self.name