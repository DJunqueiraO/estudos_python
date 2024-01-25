from animals.animal import Animal

class Hawk(Animal):
    def fly(self) -> None:
        print(f"This {self} is flying")