from tkinter import *

window = Tk()

__this_file_name__ = __file__.split('\\')[-1]
fire = PhotoImage(file=__file__.replace(__this_file_name__, 'fire.png'))
ice = PhotoImage(file=__file__.replace(__this_file_name__, 'ice.png'))

fire_label = Label(window)
fire_label.configure(image=fire)
fire_label.pack()

scale = Scale(window)
scale.configure(font=('Consolas', 20))
# scale.configure(showvalue=0) 
scale.configure(tickinterval=10)
scale.configure(from_=1000, to=150) # from and to
scale.configure(length=500) 
scale.configure(troughcolor='#00FF00', fg='#FF0000', bg='#0000FF') 
scale.configure(orient=VERTICAL) # orientation of scale
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(window)
button.configure(font=('Consolas', 20))
button.configure(text="Click Me!")
button.configure(command=lambda: print(f"temperatura is {scale.get()} degrees celsius."))
button.pack()

ice_label = Label(window)
ice_label.configure(image=ice)
ice_label.pack()

window.mainloop()