# coding=Cp1252
# **Exerc�cio 4: Verificador de Pal�ndromo** - Escreva um programa que verifica se uma palavra inserida pelo usu�rio � um pal�ndromo 
# (a palavra � a mesma quando lida de tr�s para frente). 

word = input("Informe uma palavra: ")
reversed_word = ''.join(list(word)[::-1])

print(f"Essa palavra {"� " if word == reversed_word else "n�o � "}um pal�ndromo.")
print(f"palavra: {word}, palavra invertida: {reversed_word}")