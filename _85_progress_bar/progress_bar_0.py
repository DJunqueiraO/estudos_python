from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks = 10
    x = 0
    while x < tasks:
        x += 1
        time.sleep(1)
        progressbar['value'] += 10
        percent.set("{:.0f}%".format((x/tasks)*100))
        text.set(f'{x}/{tasks} tasks completed' if x != tasks else 'tasks completed!!')
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

progressbar = Progressbar(window, orient=HORIZONTAL, length=300)
progressbar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(
    window, 
    text="download", 
    command=start
).pack()

window.mainloop()