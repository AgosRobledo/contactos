from tkinter import *
from tkinter import ttk

ventana= Tk()
ventana.title("Calculadora2")
ventana.configure(bg="#F3C7AA")
ventana.configure(cursor="pencil")
ventana.geometry('420x200')
style =ttk.Style()
style.configure("Transparent.TLabel", background=ventana["bg"])

def calcularsuma():
    try:
        num1 = float(numero1.get())
        num2 = float(numero2.get())
        resultado = num1 + num2
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, resultado)
        resulatdo.config(state="readonly")
    except ValueError:
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, "Error")
        resulatdo.config(state="readonly")

def calcularesta():
    try:
        num1 = float(numero1.get())
        num2 = float(numero2.get())
        resultado = num1 - num2
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, resultado)
        resulatdo.config(state="readonly")
    except ValueError:
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, "Error")
        resulatdo.config(state="readonly")

def calcularmult():
    try:
        num1 = float(numero1.get())
        num2 = float(numero2.get())
        resultado = num1 * num2
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, resultado)
        resulatdo.config(state="readonly")
    except ValueError:
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, "Error")
        resulatdo.config(state="readonly")

def calculardiv():
    try:
        num1 = float(numero1.get())
        num2 = float(numero2.get())
        resultado = num1 / num2
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, resultado)
        resulatdo.config(state="readonly")
    except ValueError:
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, "Error")
        resulatdo.config(state="readonly")
    except ZeroDivisionError:
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, "División por 0")
        resulatdo.config(state="readonly")

def calcularporc():
    try:
        num1 = float(numero1.get())
        num2 = float(numero2.get())
        resultado = (num1 * num2) / 100
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, resultado)
        resulatdo.config(state="readonly")
    except ValueError:
        resulatdo.config(state=NORMAL)
        resulatdo.delete(0, END)
        resulatdo.insert(0, "Error")
        resulatdo.config(state="readonly")

def clean_display():
    numero1.delete(0, END)
    numero2.delete(0, END)
    resulatdo.config(state=NORMAL)
    resulatdo.delete(0, END)
    resulatdo.config(state="readonly")

valor1=ttk.Label(ventana, text="Valor 1", style="Transparent.TLabel")
valor1.grid(row=1, column=2, pady=(30, 10), padx=(10,10))
numero1=ttk.Entry(ventana, width=15)
numero1.insert(END, "")
numero1.grid(row=1, column=3, pady=(30, 0), padx=(22,10), sticky=W+E)


valor2=ttk.Label(ventana, text="Valor 2", style="Transparent.TLabel")
valor2.grid(row=3, column=2, padx=(22,10), pady=(1,1))
numero2=ttk.Entry(ventana, width=15)
numero2.insert(END, "")
numero2.grid(row=3, column=3, pady=(0, 10), padx=(22,10), sticky=W+E)


displayresult=ttk.Label(ventana, text="Resultado", style="Transparent.TLabel")
displayresult.grid(row=4, column=2, pady=(15, 10), padx=(30,30))
resulatdo=ttk.Entry(ventana, width=15)
resulatdo.grid(row=4, column=3, pady=(0, 0), padx=(22,10), sticky=W+E)#pady=(abajo, arriba)
resulatdo.config(state="readonly")


operaciones=ttk.Label(ventana, text="Operaciones", style="Transparent.TLabel")
operaciones.grid(row=1, column=4, padx=(55,0), pady=(5,0))


BotonSumar=ttk.Radiobutton(ventana, text=" SUMAR ", value=1, command=calcularsuma).grid(row=2, column=4, sticky=W+E, padx=10)
BotonRestar=ttk.Radiobutton(ventana, text=" RESTAR ", value=2, command=calcularesta).grid(row=3, column=4, sticky=W+E, padx=10)
BotonMultiplicar= ttk.Radiobutton(ventana, text=" MULTIPLICAR ", value=3, command=calcularmult).grid(row=4, column=4, sticky=W+E, padx=10, pady=(0,10))
BotonDividir= ttk.Radiobutton(ventana, text=" Dividir ", value=4, command=calculardiv).grid(row=5, column=4, padx=10, sticky=W+E, pady=0)

ventana.mainloop()