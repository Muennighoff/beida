from tkinter import *
import random

def quicksort(A):
    if len(A) <= 1:
        return A
    L, R = [], []
    pivot_idx = random.choice(range(len(A))) 
    pivot_val = A[pivot_idx]
    for i in range(len(A)):
        if i == pivot_idx:
            continue
        if A[i] < pivot_val:
            L.append(A[i])
        else:
            R.append(A[i])
    return quicksort(L) + [pivot_val] + quicksort(R)

def square_sort(data):
    """
    对数组每个数字求平方，然后排序
    """
    return quicksort(list(map(lambda x: x ** 2, data)))

class Window:
    def __init__(self, wname="Sorting & Squaring"):
        # Basic Configuration
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.configure(background="black")
        self.root.title(wname)

        # Input Array Box
        self.text = Entry(self.root,font=("Purisa",12))
        self.text["justify"] = "center"
        self.text.focus()
        self.text.pack()

        # Output Array Box
        self.out = Message(text="")
        self.out.place(x=50, y=150, width=400, height=100)
        self.out["justify"] = "center"
        self.out["bg"] = "white"
        self.out["fg"] = "black"
    
        # Execution Button
        self.button = Button(self.root, text ="Button", command=self.click)
        self.button.pack()
        self.root.mainloop()

    def click(self):
        array = self.text.get()
        # Test appropriate format
        try:
            array = [int(i.strip().strip(",")) for i in array.split(",")]
            message = f"{square_sort(array)}"
        except:
            message = "Please input an array of the form: 2,5,7"
        self.out["text"] = message

if __name__ == "__main__":
    w = Window("My window")