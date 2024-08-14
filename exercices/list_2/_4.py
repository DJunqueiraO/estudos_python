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
  

class CalculatorButton(Button):
  def __init__(self, master):
    super().__init__(master)
    self.configure(
      font=('Arial', 15),
      foreground='white',
      background='black'
    )


class CalculatorTk(Tk):
  def __init__(self):
    super().__init__()
    self.title('titulo')
    self.geometry('300x300')

    self.entry = Entry(self)
    self.lines = CalculatorLines(self.entry)

    self.entry.configure(font=('Arial', 15))
    self.entry.place(
      relheight=1/10,
      relwidth=1
    )

    for line_index in range(len(self.lines)):
      line_frame = Frame(self)
      line_frame.configure(background='red')
      line_frame.place(
        rely=(line_index*((9/len(self.lines))/10) + 1/10), 
        relwidth=1, 
        relheight=((9/len(self.lines))/10)
      )
      for column_index in range(len(self.lines[line_index])):
        button = CalculatorButton(line_frame)

        controls = self.lines.get_controls()

        button.configure(
          text=self.lines[line_index][column_index],
          command=lambda text=self.lines[line_index][column_index]: controls[text]()
        )
        relwidth = 1/len(self.lines[line_index])
        button.place(relheight=1, relwidth=relwidth, relx=column_index*relwidth)

tk = CalculatorTk()
tk.mainloop()