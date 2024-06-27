class Animal:
    
    alive: bool = True

    def eat(self) -> None:
        print(f"{self} eating")
    
    def sleep(self) -> None:
        print(f"{self} sleeping")

    def __str__(self) -> str:
        return self.__class__.__name__.lower()

