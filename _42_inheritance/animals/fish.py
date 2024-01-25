from animals.animal import Animal

class Fish(Animal):
    def swim(self) -> None:
        print(f"This {self} is swimming")