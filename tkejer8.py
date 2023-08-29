from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Calculadora2")
ventana.configure(bg="#F3C7AA")
ventana.configure(cursor="pencil")
ventana.geometry('460x150')
style = ttk.Style()
style.configure("Transparent.TLabel", background=ventana["bg"])

def count_up():
    current_value = int(num.get())
    new_value = current_value + 1
    num.config(state=NORMAL)
    num.delete(0, END)
    num.insert(0, new_value)
    num.config(state="readonly")

def count_down():
    current_value = int(num.get())
    new_value = current_value - 1
    num.config(state=NORMAL)
    num.delete(0, END)
    num.insert(0, new_value)
    num.config(state="readonly")

def reset_counter():
    num.config(state=NORMAL)
    num.delete(0, END)
    num.insert(0, 0)
    num.config(state="readonly")

cont = ttk.Label(ventana, text="Contador", width=10, style="Transparent.TLabel")
cont.grid(row=1, column=1, padx=10, pady=50)

num = ttk.Entry(ventana, width=15)
num.insert(END, "0")
num.grid(row=1, column=2)
num.config(state="readonly")

countup = Button(ventana, text="CountUp", width=10, command=count_up).grid(row=1, column=3, pady=(10, 0), padx=(10, 10), sticky=W+E)
countdown = Button(ventana, text="CountDown", width=10, command=count_down).grid(row=1, column=4, pady=(10, 0), padx=(0, 10), sticky=W+E)
rest = Button(ventana, text="Rest", width=10, command=reset_counter).grid(row=1, column=5, pady=(10, 0), padx=(0, 10), sticky=W+E)

ventana.mainloop()