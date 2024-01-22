UTENSILS = {'fork', 'spoon', 'knife'}
DISHES = {'plate', 'cup', 'knife'}

DINNER_TABLE = UTENSILS.union(DISHES)
DISHES.update(UTENSILS)
UTENSILS.add("napkin")
UTENSILS.remove('fork')
UTENSILS.clear()

print("Utensils: ", end='')
for UTENSIL in UTENSILS:
    print(UTENSIL, end=' ')
print()

print("Dishes: ", end='')
for DISH in DISHES:
    print(DISH, end=' ')
print()

print("Dinner Table: ", end='')
for ELEMENT in DINNER_TABLE:
    print(ELEMENT, end=' ')
print()