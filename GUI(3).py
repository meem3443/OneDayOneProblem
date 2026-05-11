from tkinter import *

def move_up():
    Canvas.move(rect, 0, -10)

def move_down():
    Canvas.move(rect, 0, 10)

def move_left():
    Canvas.move(rect, -10, 0)

def move_right():
    Canvas.move(rect, 10, 0)

window = Tk()
window.title("Move Rectangle")
window.geometry('500x400')

Canvas = Canvas(window, width=400, height=300)
Canvas.pack()

rect = Canvas.create_rectangle(50, 50, 150, 150, fill="blue")

btn_up = Button(window, text="Up", command=move_up)
btn_up.pack(side=TOP)

btn_down = Button(window, text="Down", command=move_down)
btn_down.pack(side=TOP)

btn_left = Button(window, text="Left", command=move_left)
btn_left.pack(side=LEFT)

btn_right = Button(window, text="Right", command=move_right)
btn_right.pack(side=RIGHT)

window.mainloop()