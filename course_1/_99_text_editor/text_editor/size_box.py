from tkinter import Spinbox, Misc
from text_editor import *

class SizeBox(Spinbox):

    def __init__(
        self, 
        master: Misc,
        text_editor: TextEditor,
        cnf: dict[str, any] | None = {}
    ):
        super().__init__(
            master, 
            cnf=cnf,
            from_=1, to=100, 
            textvariable=text_editor.font_size, 
            command=text_editor.change_font
        )