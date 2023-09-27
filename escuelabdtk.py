import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(host="localhost", user="root", password="estudiantes2020", database="ESCUELA", port=3305)

# Función para cargar y mostrar información en el Treeview
def cargar_datos():
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("SELECT Alumnos.IDALUMNO, Alumnos.NOMBRE, Alumnos.APELLIDO, Alumnos.DNI, Carreras.NOMBRE, estadoalumno.NOMBRE FROM Alumnos JOIN Carreras ON Alumnos.IDCARRERA = Carreras.IDCARRERA JOIN estadoalumno ON Alumnos.IDESTADOALUMNO = estadoalumno.IDESTADOALUMNO WHERE Alumnos.IDEstadoAlumno=1 and Alumnos.estadoAI=1")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)


# Función para obtener las carreras desde la base de datos y cargarlas en el ComboBox
def cargar_carreras():
    cursor = conexion.cursor()
    cursor.execute("SELECT IDCARRERA, NOMBRE FROM Carreras ORDER BY NOMBRE")
    carreras = cursor.fetchall()#traer la sentencia de arriba, es la lista de tuplas
    carrera_combobox['values'] = [row[1] for row in carreras]#cada row es una tupla[(id,nombre)[]
    print(carreras)
    return carreras  # Devolver también la lista de carreras con sus ID

def cargar_estado():
    cursor = conexion.cursor()
    cursor.execute("SELECT IDESTADOALUMNO, NOMBRE FROM EstadoAlumno ORDER BY NOMBRE")
    estado = cursor.fetchall()#traer la sentencia de arriba, es la lista de tuplas
    estado_combobox['values'] = [row[1] for row in estado]#cada row es una tupla[(id,nombre)[]
    print(estado)
    return estado

def cargar_dni():
    cursor = conexion.cursor()
    cursor.execute("SELECT DNI FROM Alumnos")
    dni = [val [0] for val in cursor.fetchall()]
    print(dni)
    return dni

# Función para mostrar una ventana de alerta
def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)
#ventana modal o cuadro de dialogo, ventana avisa, para campos obligatorios

def validardni():
    dni= dni_entry.get()
    traerdni=cargar_dni()
    if dni not in traerdni:
        if "." in dni:
            dni=dni.replace(".","")
        if len(dni)!=8:
            messagebox.showerror("Error", "El DNI debe contener exactamente 8 números.")
        else:
            try:
                int(dni)
                return (dni)
            except:
                messagebox.showerror("Error", "El DNI no admite letras")
                return
    else:
        messagebox.showerror("Error", "El DNI ya existe")




# Función para guardar un nuevo registro de alumno
def guardar_alumno():
    nombre = nombre_entry.get().upper()#lo guarda en mayusculas
    apellido = apellido_entry.get().upper()
    dni = validardni()
    carrera_nombre = carrera_combobox.get() #desplegable, se cargan con otra función 
    estado_alumno = 1  # Valor predeterminado para IDESTADOALUMNO "REGULAR"


    if nombre and apellido and dni and carrera_nombre:
        # Obtener el ID de la carrera seleccionada
        carreras = cargar_carreras()
        carrera_id = None
        for carrera in carreras:
            if carrera[1] == carrera_nombre:
                carrera_id = carrera[0]
                break

        cursor = conexion.cursor()
        # Insertar un nuevo registro en la tabla Alumnos con el ID de carrera y el valor predeterminado para IDESTADOALUMNO
        cursor.execute("INSERT INTO Alumnos (NOMBRE, APELLIDO, DNI, IDCARRERA, IDESTADOALUMNO, estadoAI) VALUES (%s, %s, %s, %s, %s, 1)", (nombre, apellido, dni, carrera_id, estado_alumno))#%s seteo de configuracion, cada uno se va a reemplazar por lo que ingresó el usuario en el mismo orden que esta establecido
        conexion.commit()
        cargar_datos()  # Actualizar la vista
        # Limpiar los campos después de insertar
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        carrera_combobox.set("")  # Limpiar la selección del ComboBox
        estado_combobox.config(state="disable")
    else:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")


def guardar_cambios(idalumno):
    cursor = conexion.cursor()
    nombre=nombre_entry.get()
    apellido=apellido_entry.get()
    dni=dni_entry.get()
    carrera=carrera_combobox.get()
    if nombre and apellido and dni and carrera:
        caja=tree.item(tree.selection())
        caja=caja["values"]
        print (caja)
        carreras = cargar_carreras()
        carrera_id = None
        for car in carreras:
            if car[1] == carrera:
                carrera_id = car[0]
                break
        cursor.execute("update alumnos set nombre=%s, apellido=%s, dni=%s, idcarrera=%s WHERE idalumno = %s",  (nombre,apellido,dni,carrera_id, idalumno))
        conexion.commit()
        cargar_datos()
        messagebox.showinfo("Exito!","Cambios guardados con exito!")
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        carrera_combobox.set("") 
        estado_combobox.config(state="readonly")
        guardar_button.config(text="Guardar",command=guardar_alumno)



def modificar():
    caja=tree.item(tree.selection())
    caja=caja["values"]
    print(caja)
    idAlum= caja[0]
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    carrera_combobox.set("") 
    estado_combobox.set(caja[5])
    nombre_entry.insert(0,caja[1])
    apellido_entry.insert(0,caja[2])
    dni_entry.insert(0,caja[3])
    carrera_combobox.set(caja[4])
    guardar_button.config(text="GUARDAR CAMBIOS",command=lambda:guardar_cambios(idAlum))


def eliminar():        
    caja=tree.item(tree.selection())
    caja=caja["values"]
    print (caja)
    idAlum = caja[0]
    cursor = conexion.cursor()
    cursor.execute("update alumnos set estadoAI=0 where IDALUMNO =%s",(idAlum,))
    conexion.commit()
    cargar_datos()

# Crear ventana
root = tk.Tk()
root.title("Consulta de Alumnos")
root.configure(bg="#F3C7AA")
#root.geometry("900x900") no hace falta pero es para establecer los limites, manrgen de la ventana 
root.resizable(0,0)
# Crear un frame con un borde visible para el formulario de inscripción
formulario_frame = tk.Frame(root, bd=2, relief=tk.SOLID, bg="#F3C7AA")
formulario_frame.grid(padx=10, pady=10)

# Título del formulario
titulo_label = tk.Label(formulario_frame, text="Formulario Inscripción", bg="#F3C7AA", font=("Helvetica", 14))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Campos de entrada para nombre, apellido y DNI con el mismo ancho que el ComboBox
nombre_label = tk.Label(formulario_frame, text="Nombre:", bg="#F3C7AA")
nombre_label.grid(row=1, column=0)
nombre_entry = tk.Entry(formulario_frame)
nombre_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

apellido_label = tk.Label(formulario_frame, text="Apellido:", bg="#F3C7AA")
apellido_label.grid(row=2, column=0)
apellido_entry = tk.Entry(formulario_frame)
apellido_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

dni_label = tk.Label(formulario_frame, text="DNI:", bg="#F3C7AA")
dni_label.grid(row=3, column=0)
dni_entry = tk.Entry(formulario_frame)
dni_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Combo box para la carrera
carrera_label = tk.Label(formulario_frame, text="Carrera:", bg="#F3C7AA")
carrera_label.grid(row=4, column=0)
carrera_combobox = ttk.Combobox(formulario_frame,  state="readonly")# Configurar el ComboBox como de solo lectura
carrera_combobox.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")
#agregar validar dni, copiar previo a validar datos

estado_label = tk.Label(formulario_frame, text="Estado:", bg="#F3C7AA")
estado_label.grid(row=5, column=0)
estado_combobox = ttk.Combobox(formulario_frame,  state="readonly")# Configurar el ComboBox como de solo lectura
estado_combobox.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")
estado_combobox.config(state="disable")


# Cargar las carreras al inicio de la aplicación y obtener la lista de carreras con sus IDs
carreras = cargar_carreras()
estado=cargar_estado()

# Botón para guardar un nuevo registro de alumno
guardar_button = tk.Button(formulario_frame, text="Guardar", bg="#9E5B00", command=guardar_alumno)
guardar_button.grid(row=6, columnspan=2, pady=10, sticky="ew")

# Crear Treeview para mostrar la información
tree = ttk.Treeview(root, columns=("IDAlumno", "Nombre", "Apellido", "Carrera", "DNI", "Estado Alumno"))
tree.heading("#2", text="Nombre")
tree.heading("#3", text="Apellido")
tree.heading("#4", text="DNI")
tree.heading("#5", text="Carrera")
tree.heading("#6", text="Estado Alumno")
tree.heading("#1", text="IDAlumno")
tree.column("#1", width=0, stretch=tk.NO)
tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
tree.grid(padx=10, pady=10)

# Botón para cargar datos
cargar_button = tk.Button(root, text="CARGAR DATOS", bg="#9E5B00", command=cargar_datos)
cargar_button.grid(column= 0,pady=5)
botónmodificar=tk.Button(root, text="MODIFICAR", bg="#9E5B00", command= lambda: [estado_combobox.config(state="readonly") ,modificar() ]).grid(column= 0)#command=cargar_registro_seleccionado"""#agregar ubicación
botónguardarcambios=tk.Button(root, text="ELIMINAR", bg="#9E5B00", command=eliminar).grid(column= 0 , pady=(5,20))


# Ejecutar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()

