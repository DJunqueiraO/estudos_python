# coding=utf-8
# **Exercício 4: Calculadora Simples** - Desenvolva uma calculadora simples com botões 
# para números e operações básicas 
# (soma, subtração, multiplicação, divisão) e um campo de exibição para os resultados. 

from tkinter import *
  

class CalculatorButton(Button):
  def __init__(self, master):
    super().__init__(master)
    self.configure(
      font=('Arial', 15),
      foreground='white',
      background='black'
    )