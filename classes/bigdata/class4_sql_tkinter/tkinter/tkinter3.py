"""
创建窗口，要求用户在文本框里输入姓名。
点击按钮，将姓名添加到文本框中。另一个按钮清除所有姓名列表。
"""

from tkinter import *


def add_name():
    name = name_box.get()
    name_list.insert(END, name)
    name_box.delete(0, END)
    name_box.focus()


def clear_list():
    name_list.delete(0, END)
    name_box.focus()


window = Tk()
window.title("Name list")
window.geometry("400x300")

label1 = Label(text="Enter your name")
label1.place(x=10, y=20, width=100, height=30)

name_box = Entry(text=0)
name_box.place(x=120, y=20, width=100, height=30)
name_box.focus()

button1 = Button(text="Add to list", command=add_name)
button1.place(x=250, y=20, width=100, height=25)

name_list = Listbox()
name_list.place(x=120, y=50, width=100, height=60)

button2 = Button(text="Clear list", command=clear_list)
button2.place(x=250, y=50, width=100, height=25)

window.mainloop()