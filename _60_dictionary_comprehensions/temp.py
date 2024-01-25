from enum import Enum

class Temp(Enum):
    COLD = 0
    WARM = 1

    def __str__(self) -> str:
        return self.name