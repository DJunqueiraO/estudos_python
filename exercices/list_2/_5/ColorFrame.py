# coding=utf-8
# **Exerc�cio 5: Alterador de Cores** - Crie uma interface com tr�s sliders 
# (red, green, blue) que alteram a cor de fundo de um painel (frame) de acordo com os valores dos sliders. 

from tkinter import Frame


class ColorFrame(Frame):
  def __init__(self, master):
    super().__init__(master)

  def configure_background(self, rgb):
    self.configure(background='#%02x%02x%02x' % tuple(rgb))