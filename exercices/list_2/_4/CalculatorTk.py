# coding=utf-8
# **Exercício 4: Calculadora Simples** - Desenvolva uma calculadora simples com botões 
# para números e operações básicas 
# (soma, subtração, multiplicação, divisão) e um campo de exibição para os resultados. 

from tkinter import *

from CalculatorLines import CalculatorLines
from CalculatorButton import CalculatorButton


class CalculatorTk(Tk):
  def __init__(self):
    super().__init__()
    self.title('titulo')
    self.geometry('300x300')

    self.entry = Entry(self)
    self.lines = CalculatorLines(self.entry)

    self.entry.configure(font=('Arial', 15))
    entry_rowspan = 1
    entry_relheight = entry_rowspan/10
    self.entry.place(
      relheight=entry_relheight,
      relwidth=1
    ) 

    for line_index in range(len(self.lines)):
      line_frame = Frame(self)
      line_frame.configure(background='red')
      line_frame_relheight = ((10 - entry_rowspan)/len(self.lines))/10
      line_frame.place(
        rely=(line_index*line_frame_relheight + entry_relheight), 
        relwidth=1, 
        relheight=line_frame_relheight
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