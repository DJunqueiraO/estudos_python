from typing import Callable

students = [
    ("Josicleison", "E", 60), 
    ("Jose", "A", 33), 
    ("Elves", "B", 66), 
    ("Patrick", "C", 20), 
    ("Spongebob", "D", 72)
]

grade: Callable[[str], str] = lambda ages: ages[2]

students.sort(key=grade, reverse=True)

for i in students:
    print(i)