# coding=Cp1252
# **Exerc�cio 8: Ordena��o de Lista sem M�todos Prontos** - Implemente um algoritmo de ordena��o (como bubble sort ou insertion sort) para ordenar uma lista de n�meros sem usar m�todos de ordena��o prontos do Python (como `list.sort()` ou `sorted()`). 

def sort(array):
  for i in range(len(array)):
    for j in range(i + 1, len(array)):
      if array[i] > array[j]:
        array[i], array[j] = array[j], array[i]
  return array

print(sort([9,8,7,6,5,4,3,2,1,0]))