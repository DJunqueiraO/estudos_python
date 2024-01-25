from animals.animal import Animal

class Dog(Animal):
    def bark(self) -> None:
        print(f"This {self} is barking!")
        