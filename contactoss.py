import os
dicpersona = {}
salir = False
nombre_completo = 0
numero = 0
personas = 0
nombre = 0
telefono = 0
buscar = 0

while salir == False:
    print("Bienvenido a contactos.\n 1. agregar contactos. \n 2. buscar contactos.\n 3.eliminar contactos.\n 4.mostrar contactos.\n 5.salir ")
    op=int(input("ingrese la opcion: "))
    os.system("cls")
    if (op == 5):
        salir = True
    if (op == 1):
        nombre_completo = input("ingrese un nombre completo: ")
        numero = int(input("ingrese el numero de telefono: "))
        dicpersona[nombre_completo] = numero
    if (op == 2):
        buscar = input("ingrese el nombre que desea buscar ")
        for key , num in dicpersona.items():
            if (key == buscar):
                print("el contacto que busca es: " + key + " " + str(num))
    if (op == 3):
        eliminar = input("ingrese el nombre que desea eliminar ")
        for key , num in dicpersona.items():
            if (key == eliminar):
                eliminar = key
        dicpersona.pop(eliminar)
        print(dicpersona)
    if (op == 4):
        print("Estos son los contactos: ")
        for i, k in (dicpersona.items()):
            print(f"{i} : {k} ")