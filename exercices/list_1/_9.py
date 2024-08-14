# coding=Cp1252
# **Exerc�cio 9: Busca Bin�ria Recursiva** - Implemente uma fun��o recursiva que realiza uma busca bin�ria em uma lista ordenada de n�meros 
# e retorna o �ndice do elemento procurado (ou -1 se o elemento n�o estiver presente). 
# Lembre-se de testar seus programas para garantir que eles funcionem como esperado.

def find(array, element, by_index: int = 0):
  return (
    -1 if by_index == len(array) else
    array[by_index] if array[by_index] == element else
    find(array, element, by_index + 1)
  )

print(find([1,2,3,4,5,6,7,8,9,120], 2))