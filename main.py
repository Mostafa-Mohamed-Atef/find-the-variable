import ttkbootstrap as ttk
from tkinter import messagebox


def Calculate():
    try:
        splitted_equ = equ.get().strip().split('=')
        output.set('')
        for i in range(-100,100):
            x = i
            l = eval(splitted_equ[0])
            r = eval(splitted_equ[1])
            if l == r:
                print(output.set(x))
                break
    except:
        messagebox.showerror('Invalid input', 'Your need to enter an equation!')


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
cal_button = ttk.Button(master=window,text="Calculate",command=Calculate,padding=10)
x_label = ttk.Label(master=window,textvariable=output,padding=10)

#packing widgets
input_frame.pack()
label.pack()
equ_entry.pack(side='left')
equ_entry.focus()
button_frame.pack()
cal_button.pack(pady=10)
x_label.pack()

window.mainloop()
