# coding=Cp1252
# **Exerc�cio 5: Contador de Vogais** - Crie um programa que conta o n�mero de vogais em um texto fornecido pelo usu�rio. 

from functools import reduce

text = input("Insira um texto: ")

vowels = {'a', 'e', 'i', 'o', 'u'}

print(reduce(lambda a, b: a + 1 if b in vowels else a, text.lower(), 0))