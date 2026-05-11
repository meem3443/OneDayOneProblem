from tkinter import Tk, Label, Entry, Button

def convert():
    
    inch_val = float(entry.get())
    cm_val = inch_val * 2.54
    label_result.config(text=f"{cm_val} 센티미터")

window = Tk()
window.title("tk")
window.geometry("350x150")


Label(window, text="인치를 입력하시오:").grid(row=0, column=0, padx=10, pady=10)
entry = Entry(window)
entry.grid(row=0, column=1)

Label(window, text="변환결과:").grid(row=1, column=0)
label_result = Label(window, text="")
label_result.grid(row=1, column=1)


btn_convert = Button(window, text="변환!", command=convert)
btn_convert.grid(row=2, column=1, pady=10)

window.mainloop()