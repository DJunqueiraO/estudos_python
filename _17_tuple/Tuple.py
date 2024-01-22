STUDENT = ('Joao', 25, 'M', 7.5)

print(STUDENT.count("Joao"))
print(STUDENT.index("M"))

for INFORMATION in STUDENT:
    print(INFORMATION)

if "Joao" in STUDENT:
    print('Joao is here')