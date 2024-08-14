# coding=Cp1252
# **Exercício 8: Ordenação de Lista sem Métodos Prontos** - Implemente um algoritmo de ordenação (como bubble sort ou insertion sort) para ordenar uma lista de números sem usar métodos de ordenação prontos do Python (como `list.sort()` ou `sorted()`). 

def sort(array):
  for i in range(len(array)):
    for j in range(i + 1, len(array)):
      if array[i] > array[j]:
        array[i], array[j] = array[j], array[i]
  return array

print(sort([9,8,7,6,5,4,3,2,1,0]))