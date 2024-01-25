from typing import Callable

students = (
    ("Josicleison", "E", 60), 
    ("Jose", "A", 33), 
    ("Elves", "B", 66), 
    ("Patrick", "C", 20), 
    ("Spongebob", "D", 72)
)

age: Callable[[str], str] = lambda ages: ages[2]

sorted_students = sorted(students, key=age, reverse=True)

for i in sorted_students:
    print(i)