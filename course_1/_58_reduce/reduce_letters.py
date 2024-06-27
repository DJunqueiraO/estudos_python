from functools import reduce

letters = ['H', 'E', 'L', 'L', 'O']

word = reduce(lambda a, b: a + b, letters)

print(word)