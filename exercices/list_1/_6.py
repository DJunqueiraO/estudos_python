# coding=Cp1252
# **Exercício 6: Lista de Quadrados** - Dada uma lista de números, escreva um programa que imprima uma nova lista com os quadrados de cada número. ### Nível Avançado 

def quadrados(numeros: list[float]):
  return list(map(lambda x: x*2, numeros))

print(quadrados([1, 2, 3, 4, 5])) # [2, 4, 6, 8, 10]
print(quadrados([2, 3, 4, 5, 6])) # [4, 9, 16, 25, 36]

