# coding=utf-8
# **Exerc�cio 1: Janela Simples** - Crie uma janela b�sica do Tkinter com um t�tulo e um tamanho fixo.

from tkinter import *

tk = Tk()
tk.title('titulo')
tk.geometry('300x300')
tk.mainloop()