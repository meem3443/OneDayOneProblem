from tkinter import Tk, Canvas

def move_left(event):
    canvas.move(rect, -10, 0)

def move_right(event):
    canvas.move(rect, 10, 0)

def move_up(event):
    canvas.move(rect, 0, -10)

def move_down(event):
    canvas.move(rect, 0, 10)

window = Tk()
window.title("tk")

canvas = Canvas(window, width=500, height=400, bg="white")
canvas.pack()

rect = canvas.create_rectangle(225, 175, 275, 225, fill="red")


window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)

window.mainloop()