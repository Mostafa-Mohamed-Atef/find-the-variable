import ttkbootstrap as ttk
from tkinter import messagebox
import sympy as sy


def Calculate():
    try:
        l, r = equ.get().strip().split('=')
        output.set('')
        eqx = sy.Eq(sy.sympify(l),sy.sympify(r))
        solved = sy.solve(eqx)
        output.set(solved)
    except:
        messagebox.showerror('Invalid input', 'Your need to enter an equation!')

def clear():
    equ_entry.delete(0, ttk.END)
    equ_entry.focus()


window = ttk.Window(themename='minty')
window.title("find your x")
window.geometry('600x400')

#variables
equ = ttk.StringVar()
output = ttk.IntVar()

#widgets
input_frame = ttk.Frame(master=window,padding=50)
button_frame = ttk.Frame(master=window)
label = ttk.Label(master=input_frame,text='Enter your Equation')
equ_entry = ttk.Entry(master=input_frame,justify='center',textvariable=equ)
clear_button = ttk.Button(master=window,text="\u232B",command=clear,padding=10)
cal_button = ttk.Button(master=window,text="Calculate",command=Calculate,padding=10)
x_label = ttk.Label(master=window,textvariable=output,padding=10)

#packing widgets
input_frame.pack()
label.pack()
equ_entry.pack(side='left')
equ_entry.focus()
clear_button.pack()
button_frame.pack()
cal_button.pack(pady=10)
x_label.pack()

window.mainloop()
