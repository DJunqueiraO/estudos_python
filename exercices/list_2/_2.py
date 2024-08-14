# coding=utf-8
# **Exerc�cio 2: Bot�o de Sauda��o** - Adicione um bot�o � janela que, quando clicado, 
# exibe uma mensagem de sauda��o em um r�tulo (label). 

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