from tkinter import Tk, Label, Button
import random

def roll():
    # 1~6 사이의 랜덤 숫자를 생성하여 레이블에 업데이트
    number = random.randint(1, 6)
    label.config(text=str(number))

window = Tk()
window.title("tk")
window.geometry("200x150")

# 숫자가 표시될 레이블 (초기값 3)
label = Label(window, text="3", font=("Arial", 24))
label.pack(expand=True)

# 굴리기 버튼
button = Button(window, text="굴리기", command=roll)
button.pack(pady=10)

window.mainloop()