from animals.animal import Animal

class Rabbit(Animal):
    def run(self) -> None:
        print(f"This {self} is running")