class Car:
    def __init__(
        self, make: str, 
        model: str, 
        year: int, 
        color: str
    ) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.model} car is driving!")

    def stop(self):
        print("This car is stopping!")
        