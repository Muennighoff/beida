from tkinter import *


def plus():
    var = input_textbox.get()
    num = var.split(' ')
    result = int(num[0]) + int(num[1])
    input_textbox.delete(0, END)
    output_textbox.delete(1.0,'end')
    output_textbox.insert('end',str(result))


window = Tk()
window.title('a+b')
window.geometry('300x300')

input_textbox = Entry(window, bg='blue', fg='yellow', font=('Arial', 20))
input_textbox.place(x=150, y=10, width=200, height=50, anchor='center')

add_button = Button(window,
                    text='计算',  # 显示在按钮上的文字
                    bg='yellow', fg='red',  # 设置背景颜色和文本颜色
                    font=('Arial', 20),  # 设置字体
                    command=plus)  # 点击按钮式执行的命令
add_button.place(x=150, y=80, anchor='center')

output_textbox = Text(window, bg='pink',font=('Arial', 20))
output_textbox.place(x=150, y=200, width=200, height=50,anchor='center')

window.mainloop()
