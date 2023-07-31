from tkinter import *
import numpy as np

root = Tk()
root.geometry('440x250')
root.minsize(440,250)
root.maxsize(440,250)
root.title('Determinant Calculator')

def calculate_det():
    matrix_values = [a1.get(), a2.get(), a3.get(), a4.get(), a5.get(), a6.get(), a7.get(), a8.get(), a9.get()]
    matrix = np.array(matrix_values, dtype=int).reshape((3, 3))
    determinant = np.linalg.det(matrix)
    result.config(text='{}'.format(determinant))

def clear_text():
    for entry in [a1, a2, a3, a4, a5, a6, a7, a8, a9]:
        entry.delete(0, END)
    result.config(text='Determinant Value of Matrix is: ')

heading = Label(root, text='Determinant Calculator')
heading.grid(row=0, column=2)

slot1 = Label(root, text="Enter the Matrix Here")
slot1.grid(row=1, column=2)

a1 = Entry(root, border=5)
a1.grid(row=2, column=1)

a2 = Entry(root, border=5)
a2.grid(row=2, column=2)

a3 = Entry(root, border=5)
a3.grid(row=2, column=3)

a4 = Entry(root, border=5)
a4.grid(row=3, column=1)

a5 = Entry(root, border=5)
a5.grid(row=3, column=2)

a6 = Entry(root, border=5)
a6.grid(row=3, column=3)

a7 = Entry(root, border=5)
a7.grid(row=4, column=1)

a8 = Entry(root, border=5)
a8.grid(row=4, column=2)

a9 = Entry(root, border=5)
a9.grid(row=4, column=3)

bt = Button(root, text="Calculate", height=1, width=7, command=calculate_det)
bt.grid(row=5, column=2)

res = Label(root, text='Determinant Value of Matrix is: ')
res.grid(row=6, column=2)

result = Label(root, text='')
result.grid(row=7, column=2)

btt = Button(root, text="Reset", height=1, width=7, command=clear_text)
btt.grid(row=8, column=2)

root.mainloop()
