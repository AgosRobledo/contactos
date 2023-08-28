from tkinter import *


ventana= Tk()
ventana.title("Factorial")
ventana.configure(bg="#FFEFEB")
ventana.configure(cursor="pencil")
ventana.geometry('500x120')


def siguiente():
    numsiguiente= displayentry.get()
    numsiguiente= int(numsiguiente)
    numsiguiente+=1
    displayentry.config(state=NORMAL)
    displayentry.delete(0,END)
    displayentry.insert(0,numsiguiente)
    displayentry.config(state="readonly")


def factorial():
    numero1= displayentry.get()
    numero2= displayentry2.get()
    numero1= int(numero1)
    numero2=int(numero2)
    factor= numero1*numero2
    displayentry2.config(state=NORMAL)
    displayentry2.delete(0,END)
    displayentry2.insert(0,factor)
    displayentry2.config(state="readonly")



displayn=Label(ventana, text="n", justify="center")
displayn.grid(row=2, column=2, pady=30, padx=40)

displayFn=Label(ventana, text="Factorial (n)", justify="center")
displayFn.grid(row=2, column=4, pady=30, padx=20)

displayentry=Entry(ventana, justify="right",width=17)
displayentry.grid(row=2, column=3, pady=2, padx=2)
displayentry.insert(0,1)
displayentry.config(state="readonly")

displayentry2=Entry(ventana, justify="right",width=17)
displayentry2.grid(row=2, column=5, pady=2, padx=2)
displayentry2.insert(0,1)
displayentry2.config(state="readonly")

displayboton= Button(ventana, text="Siguiente", command= lambda: [siguiente(), factorial()])
displayboton.grid(column=6, row=2)

ventana.mainloop()