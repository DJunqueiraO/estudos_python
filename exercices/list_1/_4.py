# coding=Cp1252
# **Exercício 4: Verificador de Palíndromo** - Escreva um programa que verifica se uma palavra inserida pelo usuário é um palíndromo 
# (a palavra é a mesma quando lida de trás para frente). 

word = input("Informe uma palavra: ")
reversed_word = ''.join(list(word)[::-1])

print(f"Essa palavra {"é " if word == reversed_word else "não é "}um palíndromo.")
print(f"palavra: {word}, palavra invertida: {reversed_word}")