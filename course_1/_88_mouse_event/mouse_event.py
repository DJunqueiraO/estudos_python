from tkinter import *

def doSomething(event: Event):
    keysym = event.keysym
    if keysym == '??':
        keysym = None
    print(f'{'' if keysym == None else f'key: {keysym}, '}', end='')
    print(f'mouse cordinates: ({event.x}, {event.y}).')

window = Tk()

# window.bind('<Button-1>', doSomething) # left click
# window.bind('<Button-2>', doSomething) # middle click
# window.bind('<Button-3>', doSomething) # right click
# # window.bind('<ButtonRelease>', doSomething)
window.bind('<Return>', doSomething) # enter
# window.bind('<Leave>', doSomething) # leave

window.bind('<Motion>', doSomething) # mouse move

window.mainloop()