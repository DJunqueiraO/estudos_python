phone_number = "123-456-7890"

for digit in phone_number:
    if digit == "-":
        continue
    print(digit, end="")

