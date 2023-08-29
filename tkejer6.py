from tkinter import *
from tkinter import ttk
import random

ventana= Tk()
ventana.title("Generador de números")
ventana.configure(bg="#F3C7AA")
ventana.configure(cursor="pencil")
ventana.geometry('330x200')
style =ttk.Style()
style.configure("Transparent.TLabel", background=ventana["bg"])

def numeroaleatorio():
    num1 = int(spinbox1.get())
    num2 = int(spinbox2.get())
    generado = random.randint(num1, num2)
    numgen.config(state=NORMAL)
    numgen.delete(0, END)
    numgen.insert(0, generado)


display=ttk.Label(ventana, text="Número 1", style="Transparent.TLabel", font=("Arial", 9, "bold"))
display.grid(row=2, column=1, padx=20, pady=15)

display2=ttk.Label(ventana, text="Número 2", style="Transparent.TLabel", font=("Arial", 9, "bold"))
display2.grid(row=3, column=1, padx=20, pady=10)

spinbox1 = Spinbox(ventana, from_=0, to=100)
spinbox1.grid(row=2, column=2, padx=10)

spinbox2 = Spinbox(ventana, from_=0, to=100)
spinbox2.grid(row=3, column=2, padx=10)

display3=ttk.Label(ventana, text="Numero Generado", style="Transparent.TLabel", font=("Arial", 9, "bold"))
display3.grid(row=4, column=1, padx=20, pady=10)
numgen=ttk.Entry(ventana, width=15)
numgen.grid(row=4, column=2, pady=(10, 10), padx=10, sticky=W+E)
numgen.insert(0,0)
numgen.config(state="readonly")
#🥹inteté que funcionara y no pude🥹

Button(ventana, text="Añadir", bg="#9E3700", fg="white", command=numeroaleatorio). grid(row=5, column=2, padx=20, pady=20)


ventana.mainloop()