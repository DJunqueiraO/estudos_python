# coding=Cp1252
# **Exercício 7: Gerador de Senhas** - Escreva um programa que gera uma senha aleatória contendo letras maiúsculas, minúsculas, números e símbolos. 

from random import randint

def password_generator(password_length: int = 10) -> str:

  return ''.join(
    list(map(
      lambda _: chr(randint(0, 256)), 
      list(range(0, password_length))
    ))
  )

print(password_generator(20))