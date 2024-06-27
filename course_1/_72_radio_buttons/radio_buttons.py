from tkinter import *

foods = ["pizza",
         "hamburger",
         "hotdog"]

window = Tk()
window.geometry("500x500")

__this_file_name__ = __file__.split('\\')[-1]
pizza = PhotoImage(file=__file__.replace(__this_file_name__, 'pizza.png'))
hotdog = PhotoImage(file=__file__.replace(__this_file_name__, 'hotdog.png'))
hamburguer = PhotoImage(file=__file__.replace(__this_file_name__, 'hamburguer.png'))

food_images = list(
    map(
        lambda image: image.subsample(10, 10),
        [
            pizza,
            hotdog,
            hamburguer
        ]
    )
)

x = IntVar()

for index in range(len(foods)):
    radiobutton = Radiobutton(window)
    radiobutton.configure(text=foods[index], #adds text to radiobutton
                          variable=x, #groups radiobuttons together if they share the same variable
                          value=index, #assigns a value to each radiobutton
                          padx=20, #adds padding to the left and right
                          font=("Impact", 20), #sets the font
                          image=food_images[index], #sets the image
                          compound=LEFT, #sets the image to the left
                          indicatoron=0, #removes the radio button
                          width=300, #sets the width
                          command=lambda: print(f"you ordered {foods[x.get()]}"))
    radiobutton.pack(anchor=W)


window.mainloop()