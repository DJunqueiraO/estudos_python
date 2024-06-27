from tkinter import Menu, Misc
from text_editor_window import *
from text_editor import *

class FileMenu(Menu):
    def __init__(
        self, 
        master: TextEditorWindow, 
        text_editor: TextEditor, 
        initialdir: str
    ):
        super().__init__(master, tearoff=0)
        self.add_command(
            label="New", 
            command=lambda: master.new_file(
                then=text_editor.did_create
            )
        )
        self.add_command(
            label="Open", 
            command= lambda: master.open_file(
                initialdir=initialdir,
                then=lambda file: text_editor.did_open(file)
            )
        )
        self.add_command(
            label="Save", 
            command= lambda: master.save_file(
                initialdir=initialdir,
                then=text_editor.did_save
            )
        )
        self.add_separator()
        self.add_command(label="Exit", command=master.quit)