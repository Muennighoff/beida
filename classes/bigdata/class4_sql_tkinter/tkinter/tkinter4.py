"""
Tkinter GUI添加图片
"""

from tkinter import *


def click():
    name = textbox1.get()
    message = str("Your topic is " + name)
    textbox2["text"] = message


window = Tk()
window.title("Topics")
window.geometry("450x350")
window.wm_iconbitmap("python.ico")
window.configure(background="black")

logo = PhotoImage(file="logo.gif")

logoimage = Label(image=logo, bg='black')
logoimage.place(x=100, y=20, width=250, height=140)

label1 = Label(text="Enter your preferred topic:")
label1.place(x=5, y=200)
label1["bg"] = "black"
label1["fg"] = "white"

textbox1 = Entry(text="")
textbox1.place(x=170, y=200, width=180, height=25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text="Press me", command=click)
button1.place(x=30, y=250, width=120, height=25)
button1["bg"] = "yellow"

textbox2 = Message(text="")
textbox2.place(x=150, y=250, width=200, height=75)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()
