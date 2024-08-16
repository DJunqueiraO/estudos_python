# coding=utf-8
# **Exercício 6: Lista de Tarefas** - Implemente uma aplicação para gerenciar uma lista de tarefas. Deve permitir 
# adicionar novas tarefas, marcar tarefas como concluídas e remover tarefas da lista. ### Nível Avançado 

from tkinter import *


class TaskListbox(Listbox):

  def __init__(self, master):
    super().__init__(master)

    self.tasks = []

  def insert(self, index: str | int, *elements: str | float) -> None:
    if {*elements}.issubset(self.tasks):
      return
    self.tasks.append(*elements)
    if elements[0] == '':
      return
    return super().insert(index, *elements)
  
  def delete(self, first: str | int, last: str | int | None = None) -> None:
    self.tasks.remove(self.get(first, last))
    return super().delete(first, last)
  
  def complete(self, first: str | int, last: str | int | None = None) -> None:
    active_task: str = self.get(first, last)
    self.delete(ACTIVE)
    return self.insert(END, active_task if ' |OK|' in active_task else f'{active_task} |OK|')