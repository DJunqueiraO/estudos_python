from tkinter import *

window = Tk()

window.bind("<Return>", lambda event: print(event))

label = Label(window, text="Press any key", font=('helvetica', 50))
label.pack()

window.bind("<Key>", lambda event: label.configure(text=event.keysym))
window.mainloop()