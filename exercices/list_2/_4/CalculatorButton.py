# coding=utf-8
# **Exerc�cio 4: Calculadora Simples** - Desenvolva uma calculadora simples com bot�es 
# para n�meros e opera��es b�sicas 
# (soma, subtra��o, multiplica��o, divis�o) e um campo de exibi��o para os resultados. 

from tkinter import *
  

class CalculatorButton(Button):
  def __init__(self, master):
    super().__init__(master)
    self.configure(
      font=('Arial', 15),
      foreground='white',
      background='black'
    )