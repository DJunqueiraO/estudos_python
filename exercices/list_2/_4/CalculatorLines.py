# coding=utf-8
# **Exercício 4: Calculadora Simples** - Desenvolva uma calculadora simples com botões 
# para números e operações básicas 
# (soma, subtração, multiplicação, divisão) e um campo de exibição para os resultados. 

from tkinter import *
from functools import reduce


class CalculatorLines(list):
  def __init__(self, entry: Entry):
    super().__init__(
      [
        ['+/-', 'e', 'C', 'CE'],
        ['(', ')', '%', '/'],
        ['7', '8', '9', '*'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['00', '0', '.', '=']
      ]
    )
    self.entry = entry

  def get_controls(self):
    def command(text):
      self.entry.insert(len(self.entry.get()), text)
    controls =  dict(map(
      lambda a: (a, lambda: command(a)), 
      reduce(lambda a, b: a + b, self)
    ))
    
    def c():
      self.entry.delete(0, len(self.entry.get()))
    controls['C'] = c

    def ce():
      entry_len = len(self.entry.get())
      self.entry.delete(entry_len - 1, entry_len)
    controls['CE'] = ce

    def equals():
      result = eval(self.entry.get())
      c()
      self.entry.insert(0, result)
    controls['='] = equals

    def equals():
      result = eval(self.entry.get())*(-1)
      c()
      self.entry.insert(0, result)
    controls['+/-'] = equals

    return controls