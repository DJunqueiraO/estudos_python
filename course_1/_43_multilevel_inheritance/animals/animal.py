from animals.organism import Organism

class Animal(Organism):
    def eat(self) -> None:
        print(f"This {self} is eating!")
    
    def __str__(self) -> str:
        return self.__class__.__name__.lower()