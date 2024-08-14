# coding=utf-8
# **Exerc�cio 3: Entrada de Texto** - Crie uma interface que contenha um campo de entrada (entry) 
# onde o usu�rio pode digitar seu nome e um bot�o que, ao ser clicado, exibe "Ol�, [nome]!" em um r�tulo. 
# ### N�vel M�dio 

from tkinter import *

tk = Tk()
tk.title('titulo')
tk.geometry('300x300')

frame = Frame(tk)
frame.pack(expand=True)

frame_2 = Frame(frame)
frame_2.pack()

message = Label(frame)

button = Button(frame_2)
button.pack(side=RIGHT)

entry = Entry(frame_2)
entry.pack(side=RIGHT)

button.configure(
  text='Cick-Me',
  command=lambda: (
    message.pack(), 
    message.configure(text=f'Hello {entry.get()}')
  )
)

label = Label(frame_2)
label.configure(text='Label:')
label.pack(side=RIGHT)

tk.mainloop()