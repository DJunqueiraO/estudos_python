from animals.animal import Animal

class Predator(Animal):
    def hunt(self) -> None:
        print(f"This {self} is hunting")