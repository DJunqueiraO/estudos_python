from animals.animal import Animal

class Prey(Animal):
    def flee(self) -> None:
        print(f"This {self} is flying")