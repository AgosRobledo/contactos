import tkinter as tk
from tkinter import ttk
import mysql.connector

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(host="localhost",user="root",password=" ",database="Almacen")

# Función para cargar y mostrar información en el Treeview
def cargar_datos():
    tree.delete(*tree.get_children()) # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("SELECT producto.nombre, producto.precio, marca.nombre, categoria.nombre FROM producto JOIN marca ON producto.codmarca = marca.codmarca JOIN categoria ON producto.codcategoria=categoria.codcategoria")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

# Crear ventana
root = tk.Tk()
root.title("Almacen")

# Crear Treeview para mostrar la información
tree = ttk.Treeview(root, columns=("nombre", "marca", "precio", "categoria", "stock"))
tree.heading("#1", text="nombre")
tree.heading("#2", text="marca")
tree.heading("#3", text="precio")
tree.heading("#3", text="categoria")
tree.heading("#3", text="stock")
tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
tree.pack(padx=10, pady=10)

# Botón para cargar datos
cargar_button = tk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()