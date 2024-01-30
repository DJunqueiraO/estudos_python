from tkinter import Tk
from typing import Callable
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os
from io import TextIOWrapper

class TextEditorWindow(Tk):
    def quit(self):
        self.destroy()

    def new_file(self, then: Callable):
        self.title('Untitled')
        then()

    def open_file(self, initialdir: str, then: Callable[[TextIOWrapper], any]):
        file = askopenfilename(
            initialdir=initialdir,
            defaultextension=".txt", 
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
        )
        try:
            self.title(os.path.basename(file))
            file = open(file, 'r')
            then(file)
        except FileExistsError:
            print("Couldn't read file")
        finally:
            if type(file) != 'str':
                file.close()

    def save_file(self, initialdir: str, then: Callable[[TextIOWrapper], any]):
        file = filedialog.asksaveasfilename(
            initialdir=initialdir,
            initialfile="untitled.txt",
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
        )
        try:
            self.title(os.path.basename(file))
            file = open(file, 'w')
            then(file)
        except FileExistsError:
            print("Couldn't write file")
        finally:
            if type(file) != 'str':
                file.close()