from tkinter import *
root = Tk()

root.title("Table Calculator")
root.geometry("300x300")
root.minsize(300, 300)
root.maxsize(300, 300)
root.config(background="grey")

text = Label(root, text="Welcome to Table Calculator", background="grey")
text.pack()

s1 = Label(root, text="Enter here :", background="grey")
s1.pack()
n = Entry(root, border=5, background="yellow")
n.pack()

def table():
    c = n.get()
    x = int(c)
    r = ""
    for i in range(1,11):
        a = f"{x} X {i} = {x*i}"
        r += a + "\n"
    ass.config(text=r)

b = Button(root, text="Show Table", command = table, background="red")
b.pack()

ass = Label(root, text="", background="grey")
ass.pack()

root.mainloop()
