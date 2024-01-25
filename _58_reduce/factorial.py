from functools import reduce

factorial = lambda number: reduce(lambda a, b: a * b, range(1, number + 1))
print(factorial(5))