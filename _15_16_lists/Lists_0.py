PIZZA = "pizza"

FOODS = ["burguer", "hotdog", "fries", "cola"]

FOODS.append(PIZZA)
FOODS.remove(PIZZA)
FOODS.pop()
FOODS.insert(0, PIZZA)
FOODS.sort()
FOODS.clear()

print(type(FOODS))
# print(FOODS[2])
for FOOD in FOODS:
    print(FOOD)