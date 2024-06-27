from functools import reduce

numbers = [5, 4, 3, 2, 1]

result = reduce(lambda a, b, : a * b, numbers)

print(result)