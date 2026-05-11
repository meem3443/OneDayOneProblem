from tkinter import *

total = 0

def decrease():
    global total
    total -= 1
    label['text'] = str(total)

def increase():
    global total
    total += 1
    label['text'] = str(total)

window = Tk()
window.title("tk")
window.geometry('350x100')

btn_minus = Button(window, text="-", command=decrease)
btn_minus.pack(side=LEFT)

label = Label(window, text=str(total), width=10)
label.pack(side=LEFT)

btn_plus = Button(window, text="+", command=increase)
btn_plus.pack(side=LEFT)

window.mainloop()