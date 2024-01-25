
STUDENTS = [100, 90, 80, 70, 60, 50, 40, 30, 0]

passed_students = list(filter(lambda a: a >= 60, STUDENTS))
print(passed_students)

print([student for student in STUDENTS if student >= 60])

print([student if student >= 60 else None for student in STUDENTS])