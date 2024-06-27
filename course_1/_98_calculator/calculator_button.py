from tkinter import *

class CalculatorButton(Button):

    def __init__(self, master: Misc, cnf: dict[str, any]):
        self.configure(
            text='1',
            height=4, 
            width=9, 
            font=35
        )
        super().__init__(master, cnf)