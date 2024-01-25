from typing import Callable
from functools import reduce
from person import *

double: Callable[[float], float] = lambda a: a * 2
multiplb: Callable[[float, float], float] = lambda a, b: a * b
sum: Callable[[tuple[int]], int] = lambda *a: reduce(lambda a, b: a + b, list(a))
full_name: Callable[[Person], str] = lambda person: f"{person.first_name} {person.last_name}"
age_check: Callable[[Person], bool] = lambda person: True if person.age >= 18 else False

person = Person("Josicleison", "Elves", 17)

print(double(5))
print(multiplb(5, 6))
print(sum(2,2,2))
print(full_name(person))
print(age_check(person))