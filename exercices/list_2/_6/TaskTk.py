# coding=utf-8
# **Exercício 6: Lista de Tarefas** - Implemente uma aplicação para gerenciar uma lista de tarefas. Deve permitir 
# adicionar novas tarefas, marcar tarefas como concluídas e remover tarefas da lista. ### Nível Avançado 

from tkinter import *
from TaskListbox import TaskListbox


class TaskTk(Tk):

  def __init__(self):
    super().__init__()
    self.geometry('300x300')

    self.frame = Frame(self)
    self.frame.configure(bg='blue')
    self.frame.place(relwidth=1, relheight=1)

    self.list_box = TaskListbox(self.frame)
    self.list_box.configure(bg='white')
    self.list_box.place(relwidth=1, relheight=0.8)

    self.entry = Entry(self.frame)
    self.entry.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)

    self.button_add = Button(self.frame)
    self.button_add.configure(text='+', command=self.add)
    self.button_add_rely = 0.9
    self.button_add.place(rely=0.9, relwidth=1/3, relheight=0.1)

    self.button_remove = Button(self.frame)
    self.button_remove.configure(text='-', command=self.remove)
    self.button_remove.place(relx=1/3, rely=0.9, relwidth=1/3, relheight=0.1)

    self.button_complete = Button(self.frame)
    self.button_complete.configure(text='Ok', command=self.complete)
    self.button_complete.place(relx=2/3, rely=0.9, relwidth=1/3, relheight=0.1)

  def add(self):
    self.list_box.insert(END, self.entry.get())

  def remove(self):
    self.list_box.delete(ACTIVE)

  def complete(self):
    self.list_box.complete(ACTIVE)