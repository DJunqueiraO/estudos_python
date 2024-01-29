from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 50
    download = 0
    speed = 2
    while download < GB:
        download += 1
        time.sleep(0.05)
        progressbar['value'] += (speed/GB)*100
        percent.set("{:.0f}%".format((download/GB)*100))
        text.set(f"{download}/{GB} GB's completed" if download != GB else 'tasks completed!!')
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

progressbar = Progressbar(window, orient=HORIZONTAL, length=300)
# progressbar = Progressbar(window, orient=VERTICAL, length=300)
progressbar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(
    window, 
    text="download", 
    command=start
).pack()

window.mainloop()