from tkinter import *
import math

root = Tk()
root.title("Calculator")
root.geometry("235x150")
root.minsize(235,150)
root.maxsize(300,150)
root.config(background="grey")

a = ""
b = ""

def a1():
    global a
    a += "1"
    l1.config(text=a)
def a2():
    global a
    a += "2"
    l1.config(text=a)
def a3():
    global a
    a += "3"
    l1.config(text=a)
def a4():
    global a
    a += "4"
    l1.config(text=a)
def a5():
    global a
    a += "5"
    l1.config(text=a)
def a6():
    global a
    a += "6"
    l1.config(text=a)
def a7():
    global a
    a += "7"
    l1.config(text=a)
def a8():
    global a
    a += "8"
    l1.config(text=a)
def a9():
    global a
    a += "9"
    l1.config(text=a)
def a0():
    global a
    a += "0"
    l1.config(text=a)
def add():
    global a
    a += "+"
    l1.config(text=a)
def sub():
    global a
    a += "-"
    l1.config(text=a)
def mul():
    global a
    a += "*"
    l1.config(text=a)
def div():
    global a
    a += "/"
    l1.config(text=a)
def dot():
    global a
    a += "."
    l1.config(text=a)
def equal():
    global a
    s = eval(a)
    a = str(s)
    l1.config(text=str(s))
def dlt():
    global a
    a = a[:-1]
    l1.config(text=a)
def ac():
    global a
    a = ""
    l1.config(text=a)

l1 = Label(root, textvariable=a)
l1.grid(row=0, column=0, columnspan=10)

b1 = Button(root,text="1", width=7,command=a1).grid(row=3,column=0)
b2 = Button(root,text="2", width=7,command=a2).grid(row=3,column=1)
b3 = Button(root,text="3", width=7,command=a3).grid(row=3,column=2)
b4 = Button(root,text="4", width=7,command=a4).grid(row=2,column=0)
b5 = Button(root,text="5", width=7,command=a5).grid(row=2,column=1)
b6 = Button(root,text="6", width=7,command=a6).grid(row=2,column=2)
b7 = Button(root,text="7", width=7,command=a7).grid(row=1,column=0)
b8 = Button(root,text="8", width=7,command=a8).grid(row=1,column=1)
b9 = Button(root,text="9", width=7,command=a9).grid(row=1,column=2)
b0 = Button(root,text="0", width=7,command=a0).grid(row=4,column=0)
ad = Button(root,text="+", width=7,command=add).grid(row=1,column=3)
su = Button(root,text="-", width=7,command=sub).grid(row=2,column=3)
mu = Button(root,text="*", width=7,command=mul).grid(row=3,column=3)
di = Button(root,text="/", width=7,command=div).grid(row=4,column=3)
dt = Button(root,text=".", width=7,command=dot).grid(row=4,column=1)
eq = Button(root,text="=", width=7,command=equal).grid(row=4,column=2)
dt = Button(root,text="Del", width=7,command=dlt).grid(row=5,column=0)
AC = Button(root,text="AC", width=7,command=ac).grid(row=5,column=1)


root.mainloop()
