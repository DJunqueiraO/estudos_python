
double = lambda a: a * 2
multiplb = lambda a, b: a * b
sum = lambda a, b, c: a + b + c
full_name = lambda first_name, last_name: f"{first_name} {last_name}"
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiplb(5, 6))
print(sum(2, 2, 2))
print(full_name("Josicleison", "Elves"))
print(age_check(12))