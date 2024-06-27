from tkinter import Text, StringVar, END
from tkinter import colorchooser
from typing import Callable
from io import TextIOWrapper

class TextEditor(Text):

    def did_create(self):
        self.delete(1.0, END)

    def did_open(self, file: TextIOWrapper):
        self.delete(1.0, END)
        self.insert(1.0, file.read())

    def did_save(self, file: TextIOWrapper): (
        file.write(self.get(1.0, END))
    )

    def __init__(self, master=None):
        super().__init__(master)
        self.font_name = StringVar(self.master)
        self.font_size = StringVar(self.master)
        self.setFont('Arial', '25')
        self.configure(font=(self.font_name.get(), self.font_size.get()))

    def setFont(self, name: str, size: str):
        self.font_name.set(name)
        self.font_size.set(size)

    def getFont(self) -> tuple[str, str]:
        return (self.font_name.get(), self.font_size.get())

    def cut(self):
        self.event_generate('<<Cut>>')

    def copy(self):
        self.event_generate('<<Copy>>')

    def paste(self):
        self.event_generate('<<Paste>>')

    def change_color(self):
        color = colorchooser.askcolor(title="pick a color")
        self.configure(foreground=color[1])

    def change_font(self):
        self.configure(font=self.getFont())