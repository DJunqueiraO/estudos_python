DRINKS = ["coffee", "soda", "tea"]
DINNER = ["pizza", "hamburger", "hotdog"]
DESSERT = ["cake", "ice cream"]

FOODS = [DRINKS, DINNER, DESSERT]

print(FOODS[1][2])

for SPECIFIC_FOODS in FOODS:
    for FOOD in SPECIFIC_FOODS:
        print(FOOD)
    