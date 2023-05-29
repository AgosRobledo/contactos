    
""""Calculadora de Estadísticas de Números
Escribe un programa que permita al usuario ingresar una lista de números y realice los
siguientes cálculos estadísticos:
1. Calcular la suma de los números.
2. Calcular el promedio de los números.
3. Encontrar el número mínimo y el número máximo de la lista.
4. Calcular la desviación estándar de los números.
El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y
luego imprimir los resultados de los cálculos estadísticos."""

listanum=[]
listavar=[]
suma = 0
salir=True
prom=0
cont=0
suma2=0
variacion1=0
variacion2=0
desviacion=0

while True:
    num=input("Ingrese numeros con espacios: ")
    listanum=num.split()
    
    for k in range(0,len(listanum)):
        listanum[k]= int(listanum[k])
        
        
    for i in listanum:
        
        suma = suma + i
        
        if (cont==0):
            mayor= i
            menor= i
        if (i > mayor):
            mayor= i
        if (i < menor):
            menor= i
            
        cont = cont + 1
            
    prom = suma / cont
        
    for i in range (0,len(listanum)):
        variacion1=(listanum[i]-prom)**2
        suma2=suma2+variacion1 
    variacion2=suma2/cont
    desviacion=variacion2**(1/2)
    break

print(listanum)
print("La suma de los numeros es: " + str(suma))
print("el numero menor es: " + str(menor))
print("el numero mayor es: " + str(mayor))
print("el promedio es. "+ str(prom))
print("la estadistica es: " + str(desviacion))
      
            
        
        
      

      