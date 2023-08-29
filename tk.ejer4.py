from tkinter import *
from tkinter import ttk


ventana=Tk()
ventana.title("Calculadora")
ventana.configure(bg="#FFCC95")
ventana.geometry("300x280")
style = ttk.Style()# se utiliza para sacarle el fondo a las etiquetas
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




display=ttk.Label(ventana, text="Primer Número", style="Transparent.TLabel", font=("Arial", 10, "bold"))
display.grid(row=1, column=2, pady=(30, 10), padx=(10,10))

numero1=ttk.Entry(ventana, width=15)
numero1.insert(END, "")
numero1.grid(row=1, column=3, pady=(30, 10), padx=(22,10), sticky=W+E)

display2=ttk.Label(ventana, text="Segundo Número", style="Transparent.TLabel", font=("Arial", 10, "bold"))
display2.grid(row=3, column=2, padx=(22,10), pady=(15,15))
numero2=ttk.Entry(ventana, width=15)
numero2.insert(END, "")
numero2.grid(row=3, column=3, pady=(10, 10), padx=(22,10), sticky=W+E)


displayresult=ttk.Label(ventana, text="Resultado", style="Transparent.TLabel",font=("Arial", 10, "bold"))
displayresult.grid(row=4, column=2, pady=(15, 10), padx=(1,30))
resulatdo=ttk.Entry(ventana, width=15)
resulatdo.grid(row=4, column=3, pady=(10, 10), padx=(22,10), sticky=W+E)
resulatdo.config(state="readonly")



Button(ventana, text="+", bg="#9E5B00", width=15, command=calcularsuma).grid(row=5, column=2, pady=(10,0), padx=(20,10), sticky=W+E)
Button(ventana, text="-", bg="#9E5B00", width=15, command=calcularesta).grid(row=5, column=3, pady=(10,0), padx=(20,10), sticky=W+E)

Button(ventana, text="*", bg="#9E5B00", width=15, command=calcularmult).grid(row=6, column=2, pady=(10,0), padx=(20,10), sticky=W+E)
Button(ventana, text="/", bg="#9E5B00", width=15, command=calculardiv).grid(row=6, column=3, pady=(10,0), padx=(20,10), sticky=W+E)

Button(ventana, text="%",     bg="#9E5B00", width=15, command=calcularporc).grid(row=7, column=2, pady=(10,0), padx=(20,10), sticky=W+E)
Button(ventana, text="CLEAR", bg="#9E5B00", width=15, command=clean_display).grid(row=7, column=3, pady=(10,0), padx=(20,10), sticky=W+E)


ventana.mainloop()