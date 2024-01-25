from car import *
from motorcycle import *

def change_color(vehicle: Vehicle, color: str):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()
bike_2 = Motorcycle()
bike_3 = Motorcycle()

change_color(car_1, 'red')
change_color(car_2, 'green')
change_color(car_3, 'blue')

change_color(bike_1, 'turquoise')
change_color(bike_2, 'amber')
change_color(bike_3, 'hotpink')

print(car_1.color)
print(car_2.color)
print(car_3.color)

print(bike_1.color)