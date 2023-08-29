from tkinter import *
from tkinter import ttk

ventana= Tk()
ventana.title("Películas")
ventana.configure(bg="#F3C7AA")
ventana.configure(cursor="pencil")
ventana.geometry('420x220')
style =ttk.Style()
style.configure("Transparent.TLabel", background=ventana["bg"])

def añadir_pelicula():
    pelicula = nombre.get()
    if pelicula:
        listpelis.insert(END, pelicula)
        nombre.delete(0, END)

def borrar_todo():
    listpelis.delete(0, END)

titulo=ttk.Label(ventana, text="Ingresa el nombre de una película", style="Transparent.TLabel", font=("Arial", 9, "bold"))
titulo.grid(row=2, column=1, padx=20, pady=20)
nombre=ttk.Entry(ventana, width=25)
nombre.grid(row=3, column=1)

añadir=Button(ventana, text="Añadir", bg="#9E3700", fg="white", command=añadir_pelicula). grid(row=4, column=1, padx=20, pady=20)
añadir=Button(ventana, text="Borrar todo",  bg="#9E3700",  fg="white", command=borrar_todo). grid(row=5, column=1, padx=20, pady=8)

peliculas=ttk.Label(ventana, text="Películas", style="Transparent.TLabel", font=("Arial", 9, "bold"))
peliculas.grid(row=2, column=2, padx=20, pady=20)
listpelis = Listbox(ventana, width=25, height=9)
listpelis.grid(row=3, column=2, rowspan=3, padx=10)


ventana.mainloop()