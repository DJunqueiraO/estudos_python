# coding=Cp1252
# **Exercício 5: Contador de Vogais** - Crie um programa que conta o número de vogais em um texto fornecido pelo usuário. 

from functools import reduce

text = input("Insira um texto: ")

vowels = {'a', 'e', 'i', 'o', 'u'}

print(reduce(lambda a, b: a + 1 if b in vowels else a, text.lower(), 0))