"""
创建窗口，要求用户在文本框里输入姓名。点击按钮，显示”hello”消息和姓名，
并改变背景和消息框的字体颜色。添加到文本框中。
"""

from tkinter import *


def click():
    name = textbox1.get()
    message = str("Hello\n" + name)
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "red"
    textbox2["text"] = message


window = Tk()
window.geometry("500x200")

label1 = Label(text="Enter your name:\n")
label1.place(x=30, y=20)

textbox1 = Entry(text="")
textbox1.place(x=150, y=20, width=200, height=25)
textbox1['justify'] = 'center'
textbox1.focus()

button1 = Button(text='Press me', command=click)
button1.place(x=30, y=50, width=120, height=25)

textbox2 = Message(text="")
textbox2.place(x=150, y=50, width=200, height=50)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()
