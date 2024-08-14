# coding=utf-8
# **Exercício 2: Botão de Saudação** - Adicione um botão à janela que, quando clicado, 
# exibe uma mensagem de saudação em um rótulo (label). 

from tkinter import *

tk = Tk()
tk.title('titulo')
tk.geometry('300x300')

frame = Frame(tk)
frame.pack(expand=True)

label = Label(frame)
label.configure(text='Clicked')

button = Button(frame)
button.configure(
  text='Click-Me', 
  command=lambda: (label.pack(), button.destroy())
)
button.pack()

tk.mainloop()