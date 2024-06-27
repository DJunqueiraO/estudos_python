foods = list()
while True:
    if food := input('What food do you like?: ') == 'quit':
        break
    foods.append(food)