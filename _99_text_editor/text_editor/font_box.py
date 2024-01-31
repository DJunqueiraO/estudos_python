from tkinter import OptionMenu, Misc, font
from text_editor import *

class FontBox(OptionMenu):

    def __init__(
        self, 
        master: Misc,
        text_editor: TextEditor
    ):
        super().__init__(
            master,
            text_editor.font_name, 
            *font.families(), 
            command=lambda _: text_editor.change_font()
        )