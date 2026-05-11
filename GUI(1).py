from tkinter import Tk, Label, LEFT, Button

def click():
    label.config(text="Clicked")

window = Tk()
window.title("Welcome")
window.geometry('350x150')

label = Label(window, text = "Hi!")
label.pack(side = LEFT)

button = Button(window, text="Click Me", command=click)
button.pack(side = LEFT)

window.mainloop()