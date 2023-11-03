import tkinter as tk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
import time

conexion = mysql.connector.connect(host="localhost", user="root", password="estudiantes2020", database="JUEGO", port=3305)

cursor = conexion.cursor()
pregunta_actual = 0

global puntuacion
puntuacion = 0


root = None
ventana = None

global inicio
global jugadores_data
jugadores_data = []


global label_pregunta
global botones_respuesta
global frame_respuestas
global nombre_entry
global apellido_entry  
global telefono_entry
global tree


def actualizar_tree():
    global tree

    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor.execute("select codjugador, nombre, apellido, telefono, puntaje, tiempo from jugador order by puntaje DESC")
    for row in cursor.fetchall():
        print(row)
        tree.insert("", "end", values=row)



def crear_ventana():
    global tree
    global nombre_entry
    global apellido_entry  
    global telefono_entry

    ventana = tk.Tk()
    ventana.title("Jugadores")
    ventana.attributes('-fullscreen', True)
    ventana.configure(bg="#630551")

    # Crear un frame con un borde visible para el formulario de inscripción
    formulario_frame = tk.Frame(ventana, bd=2, relief=tk.SOLID, bg="#B591B6")
    formulario_frame.grid(padx=10, pady=10)

    # Título del formulario
    titulo_label = tk.Label(formulario_frame, text="Jugador", bg="#B591B6", font=("Arial", 22, 'bold'))
    titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Campos de entrada para nombre, apellido y teléfono con el mismo ancho que el ComboBox
    nombre_label = tk.Label(formulario_frame, text="Nombre:", bg="#B591B6", font=("Arial", 17))
    nombre_label.grid(row=1, column=0)
    nombre_entry = tk.Entry(formulario_frame)
    nombre_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

    apellido_label = tk.Label(formulario_frame, text="Apellido:", bg="#B591B6", font=("Arial", 17))
    apellido_label.grid(row=2, column=0)
    apellido_entry = tk.Entry(formulario_frame)
    apellido_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

    telefono_label = tk.Label(formulario_frame, text="Teléfono:", bg="#B591B6", font=("Arial", 17))
    telefono_label.grid(row=3, column=0)
    telefono_entry = tk.Entry(formulario_frame)
    telefono_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

    jugar_button = tk.Button(formulario_frame, text="JUGAR", bg="#9E5B00", font=("Arial", 10, 'bold'), command=lambda:iniciar_juego(nombre_entry,apellido_entry,telefono_entry))
    jugar_button.grid(row=6, columnspan=2, pady=1, sticky="ew")

    jugar_button = tk.Button(formulario_frame, text="SALIR", bg="#9E5B00", font=("Arial", 10, 'bold'), command=lambda:salir_pantalla_princial(ventana))
    jugar_button.grid(row=7, columnspan=3, pady=5, sticky="ew")

    titulo2_label = tk.Label(ventana, text="Tabla de Jugadores", font=("Arial", 35, 'bold'), bg="#630551", fg="white")
    titulo2_label.grid(row=4, column=0, columnspan=5, padx=250, pady=15)

    # Crear Treeview para mostrar la información
    tree = ttk.Treeview(ventana, columns=("idjugador", "Nombre", "Apellido", "Telefono", "Puntaje", "Tiempo"))
    tree.heading("#2", text="Nombre")
    tree.heading("#3", text="Apellido")
    tree.heading("#4", text="Teléfono")
    tree.heading("#5", text="Puntaje")
    tree.heading("#6", text="Tiempo")
    tree.heading("#1", text="idjugador")
    tree.column("#1", width=0, stretch=tk.NO)
    tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
    tree.column("#2", width=230)  # Aumenta el ancho del Treeview
    tree.config(height=23)  # Aumentar la altura del Treeview
    tree.grid(row=5, column=0, padx=250, pady=0)

    actualizar_tree()


    ventana.mainloop()




#######################################
#######################################
#######################################


def iniciar_juego(nombre_entry,apellido_entry,telefono_entry):

    global jugadores_data

    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    telefono = telefono_entry.get()

    # Verificar si todos los campos están llenos
    if nombre and apellido and telefono:
        jugadores_data= [nombre, apellido, telefono]
        print(jugadores_data)
        global inicio
        inicio=time.time()
        abrir_juego()
        
    else:
        messagebox.showerror("Error", "Los campos son obligatorios. Debes completarlos.")




def abrir_juego():

    global label_pregunta
    global botones_respuesta
    global frame_respuestas

    root = tk.Toplevel()
    root.attributes('-topmost', True)


    root.title("Juego de Preguntas y Respuestas")
    root.attributes("-fullscreen", True)
    root.configure(bg="#630551")

    label_pregunta = tk.Label(root, text="", font=("Helvetica", 20, 'bold'), bg="#630551", fg="white")
    label_pregunta.pack(pady=90)

    frame_respuestas = tk.Frame(root, bg="#630551")
    frame_respuestas.pack()
    botones_respuesta = []

    
          
    global preguntas_respuestas
    preguntas_respuestas = obtener_preguntas()
            
    for i in range(4):
        frame_grupo = tk.Frame(frame_respuestas, bg="#630551")
        frame_grupo.pack(pady=30)
        boton = tk.Button(frame_grupo, text="", font=("Helvetica", 17), command=lambda i=i: verificar_respuesta(botones_respuesta[i]['text'] , root))
        boton.pack(pady=10)

        botones_respuesta.append(boton)
    mostrar_pregunta(root,frame_respuestas)


    root.mainloop()

   #quiero una funcion que me permita apretar el boton salir de la ventana root y se vuelva a la ventana principal

    

#######################################
#######################################
#######################################
#######################################
#######################################
#######################################


def salir_pantalla_princial(ventana):
        ventana.destroy()


#######################################
#######################################
#######################################



 


#######################################
#######################################
#######################################
#######################################
#######################################
#######################################


def obtener_preguntas():
    global preguntas_respuestas
    cursor.execute("SELECT preguntas, respuestas, respuestaErronea_uno, respuestaErronea_dos, respuestaErronea_tres FROM Preguntas")
    preguntas_respuestas = cursor.fetchall()
    random.shuffle(preguntas_respuestas)  # Mezclar las preguntas para que aparezcan en orden aleatorio
    return preguntas_respuestas



#######################################
#######################################
#######################################



def mostrar_pregunta(root,frame_respuestas):
    global label_pregunta
    global botones_respuesta

    global preguntas_respuestas
    global pregunta_actual
    if pregunta_actual < len(preguntas_respuestas):
        pregunta, respuesta_correcta, respuesta_incorrecta_1, respuesta_incorrecta_2, respuesta_incorrecta_3 = preguntas_respuestas[pregunta_actual]
        label_pregunta.config(text=pregunta)
        opciones = [respuesta_correcta, respuesta_incorrecta_1, respuesta_incorrecta_2, respuesta_incorrecta_3]
        random.shuffle(opciones)  # Mezclar las opciones de respuesta
        for i, opcion in enumerate(opciones):
            botones_respuesta[i].config(text=opcion)
    else:
        label_pregunta.config(text="Fin del juego. Puntuación: " + str(puntuacion))

        for boton in botones_respuesta:
            boton.config(state=tk.DISABLED)
        fin_Juego(root, frame_respuestas)



#######################################
#######################################
#######################################




def verificar_respuesta(opcion,root):
    global preguntas_respuestas
    global pregunta_actual
    global puntuacion
    global jugadores_data

    global puntuacion_total
    global tiempo_total
    global tiempo_total_bd

    pregunta, respuesta_correcta, _, _, _ = preguntas_respuestas[pregunta_actual]
    if opcion == respuesta_correcta:
        puntuacion += 100


    pregunta_actual += 1
    mostrar_pregunta(root,frame_respuestas)
    if pregunta_actual < len(preguntas_respuestas):
    
       
        puntuacion_total = puntuacion
        print(jugadores_data)
        tiempo_transcurrido=(time.time()-inicio) * 1000
        print('Tiempo transcurrido:', tiempo_transcurrido)
        minutos, segundos= divmod(tiempo_transcurrido/1000,60)
        segundos, milisegundos = divmod(segundos,1)
        print(f"tiempo transcurrido: {int(minutos)}, {int(segundos)}, {int(milisegundos)}")
        tiempo_total=(f"tiempo transcurrido: {int(minutos)}:{int(segundos)}")
        tiempo_total_bd = (f"{int(minutos)}:{int(segundos)}")
    else:
        label_pregunta.configure(text="¡Has respondido todas las preguntas!", bg="#630551", font=("Arial", 26, 'bold'))




#######################################
#######################################
#######################################

def fin_Juego(root, frame_pregunta):
    global preguntas_respondidas
    global contador_correctas
    global contador_incorrectas
    global tiempo_total
    global lista_jugador
    global jugadores_treeview
    global nombre_entry
    global apellido_entry  
    global telefono_entry
    
    frame_pregunta.destroy()

    frame_Fin = tk.Frame(root, bg="#630551")
    frame_Fin.pack(pady=50)

    agradecimiento_Label = tk.Label(frame_Fin, text="¡Muchas gracias por participar!", bg="#630551", font=("Arial", 22, 'bold'), fg="white")
    agradecimiento_Label.pack()

    label_1 = tk.Label(frame_Fin, text=f"Tiempo logrado: {tiempo_total}", bg="#630551",font=("Arial", 22, 'bold'), fg="white")
    label_1.pack()

    label_2 = tk.Label(frame_Fin, text=f"Puntaje obtenido: {puntuacion}",bg="#630551", font=("Arial", 22, 'bold'), fg="white")
    label_2.pack()

    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    telefono_entry.delete(0, tk.END)
    
    boton_volver = tk.Button(frame_Fin, text= "Volver a la pantalla de inicio", font=("Arial", 20, 'bold'), bg="red", fg="white", command = lambda: [cerrar_juego(root)])
    boton_volver.pack(pady= 12)





def cerrar_juego(ventana):
    cursor.execute("INSERT INTO JUGADOR (NOMBRE, APELLIDO, TELEFONO, PUNTAJE, TIEMPO) values (%s,%s,%s,%s,%s)", (jugadores_data[0], jugadores_data[1], jugadores_data[2], puntuacion_total, tiempo_total_bd))
    conexion.commit()
    ventana.destroy()
    actualizar_tree()


crear_ventana()


#base de datos
"""create database JUEGO;
use JUEGO;
CREATE TABLE Preguntas (
codpreguntas int PRIMARY KEY auto_increment ,
preguntas VARCHAR(150) NOT NULL,
respuestas varchar (150),
respuestaErronea_uno varchar (250) not null,
respuestaErronea_dos varchar (250) not null,
respuestaErronea_tres varchar (250) not null);

CREATE TABLE Jugador (
codjugador int PRIMARY KEY auto_increment ,
nombre varchar (150) NOT NULL,
apellido varchar (150) not null,
telefono varchar (150) not null,
puntaje int not null,
tiempo varchar (150) not null);



insert into Preguntas(preguntas, respuestas, respuestaErronea_uno, respuestaErronea_dos, respuestaErronea_tres)
values('¿En qué año se fundó el ISAUI?', '1983', '1970', '1990', '1995'),

('¿Cuál fué el nombre del establecimiento educativo cuando se fundó?', 'COMPLEJO FACULTATIVO DE ENSEÑANZA SUPERIOR San Francisco de Asís (COFES Sn.FCO.DE ASIS)', 'INSTITUTO SANTA CLARA DE ASIS', 'COLEGIO SAN FRANCISCO JAVIER', 'INSTITUTO ARGENTINO	DE ENSEÑANZA SUPERIOR(IADES)'  ),

('¿En qué año se convierte a colegio Nacional?', '22/07/85', '25/10/85', '06/08/85', '15/11/85' ),

('¿Cuántos directores tuvo el Instituto hasta la fecha?', '4', '7', '5', '9' ),	

('¿Cuántas carreras se dictan actualmente en el ISAUI ?', '6', '3', '5', '7'),

('¿Cuál fué el primer número de teléfono del Instituto?', '41164', '42546', '44561', '48586'),

('¿Qué es el workshop? ', 'Es una técnica de venta de las carreras del Inst.ISAUI', 'Es un evento para recudar fondos', 'Es una presentación de proyectos sin un fin en especial', 'Es un concierto'),

('¿Qué carrera fué la pionera con los viajes en las materias de prácticas?', 'TÉCNICO Y GUIA SUPERIOR EN TURISMO', 'TÉCNICO SUPERIOR EN DESSARROLLO DE SOFTWARE', 'ENFERMERIA', 'DISEÑO DE ESPACIOS'),

('¿Cómo era el edificio  educativo en sus comienzos?', 'UNA CASA CON 3 AMBIENTES QUE SE CONVIRTIERON EN AULAS', 'UNA CASONA ABANDONADA', 'UN CENTRO VECINAL', 'UNA BIBLIOTECA'),

('¿ISAUI es un Instituto público ?', 'SI', 'NO','SEMI-PÚBLICA', 'SEMI-PRIVADA'),

('¿A partir de que año la cooperadora comenzó a construir las aulas?', '1986', '1987', '1988', '1990'),

('¿De dónde provenía el dinero para la construcción de aulas?', 'DEL BONO CONTRIBUCIÓN QUE ABONABAN LOS PADRES', 'DEL GOBIERNO NACIONAL', 'DE LA MUNICIPALIDAD DE VILLA CARLOS PAZ', 'DE DONACIONES'),

('¿Quién fué el presidente de la cooperadora en los comienzos de la Institución?', 'SR.GATICA', 'SR.FARIAS', 'SR.BERTOLDI', 'SR.BERTOLDO'),

('¿Quién es la presidenta de la cooperadora actualmente?','MASCHIO DANIELA', 'GERBAUDO ANDREA', 'BERTOLDO CARLA', 'PAEZ MARIELA'),

('¿En qué época se logró la nacionalización?', 'LA PRESIDENCIA DE R.ALFONSÍN', 'LA PRESIDENCIA DE C.S.MENEM', 'LA PRESIDENCIA DE R.BIGNONE', 'LA PRESIDENCIA DE E.DUHALDE');
"""



