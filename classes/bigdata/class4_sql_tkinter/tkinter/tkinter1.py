"""
几何形状与位置（Geometry, Place）
"""
from tkinter import *


# 点击按钮后，在窗口中添加Label，并将背景色改为蓝色，字体色改为白色
def call():
    msg = Label(window, text="You pressed the button")  # 标签
    msg.place(x=30, y=50)  # 位置
    button['bg'] = 'blue'  # 按钮的背景色
    button['fg'] = 'white'  # 按钮的前景色（按钮文本的颜色）


# 窗口的建立
window = Tk()
window.geometry("500x410")

button = Button(text="press me", command=call)
button.place(x=30, y=20, width=100, height=30)

window.mainloop()