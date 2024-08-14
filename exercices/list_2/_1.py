# coding=utf-8
# **Exercício 1: Janela Simples** - Crie uma janela básica do Tkinter com um título e um tamanho fixo.

from tkinter import *

tk = Tk()
tk.title('titulo')
tk.geometry('300x300')
tk.mainloop()