from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

Car.__wheels__ = 2

print(car_2.__wheels__)
print(car_1.__wheels__)