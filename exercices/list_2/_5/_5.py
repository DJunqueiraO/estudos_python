# coding=utf-8
# **Exercício 5: Alterador de Cores** - Crie uma interface com três sliders 
# (red, green, blue) que alteram a cor de fundo de um painel (frame) de acordo com os valores dos sliders. 

from tkinter import Tk, Frame, Scale
from ColorFrame import ColorFrame


tk = Tk()
tk.geometry('300x150')

frame = Frame(tk)
frame_relwidth = 0.6
frame.place(relwidth=frame_relwidth, relheight=1)

colors = (
  [0, 0, 0]
)

color_frame = ColorFrame(tk)
color_frame.configure_background(colors)
color_frame.place(relx=frame_relwidth, relwidth=1-frame_relwidth, relheight=1)

def on_map(index):
  scale = Scale(frame, from_=0, to=255, orient="horizontal")
  def command(value):
    colors[index] = int(value)
    color_frame.configure_background(colors)
  scale.configure(command=command)
  scale.place(rely=(1/len(colors))*index, relwidth=1)

list(map(lambda a: on_map(a[0]), enumerate(colors)))

tk.mainloop()