from tkinter import *
root = Tk()

root.title("Calculator")
root.geometry("300x300")
root.minsize(300, 300)
root.maxsize(300, 300)
root.config(background="grey")

text = Label(root, text="Welcome to Calculator", background="grey")
text.pack()

s1 = Label(root, text="Enter here :", background="grey")
s1.pack()
n = Entry(root, border=5, background="yellow")
n.pack()

def calc():
    a = n.get()
    s = eval(a)
    ass.config(text="Answer: "+ str(s))

b = Button(root, text="Claculate", command=calc, background="red")
b.pack()

ass = Label(root, text="Answer: ", background="grey")
ass.pack()

root.mainloop()
