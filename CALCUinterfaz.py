from tkinter import * 

root= Tk()
root.title("Calculadora")
root.configure(bg="black")
root.configure(cursor="pencil")
root.geometry('355x506')


display = Entry(root, justify="right", width=32, background="black", foreground="white", font=("arial",15))
display.grid(row=0,column=0,columnspan=4, ipady=50)

i=0
def obtener_numeros(n):
    global i
    display.insert(i, n)
    i+=1

def agregar_operador(operator):
    global i 
    operator_lenght =len(operator)
    display. insert(i, operator)
    i +=operator_lenght

def clean_display():
    display.delete(0, END)

def borrar_uno():
	global i 
	if i==-1:
		pass
	else:
		display.delete(i,last =None)
		i-=1
                
def operacion():
	global i
	ecuacion = display.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))
			display.delete(0,END)
			display.insert(0,result)
			longitud = len(result)
			i = longitud
		except:
			result = 'ERROR'
			display.delete(0,END)
			display.insert(0,result)
	else:
		pass

  


#enumerar botones
Button(root, text="AC",bg="lightgrey", width=8, height=4, font=("arial",10), command=lambda: clean_display()).grid(row=2, column=0, sticky=W+E)
Button(root, text="C", bg="lightgrey", width=8, height=4, font=("arial",10), command=lambda: borrar_uno()).grid(row=2, column=1, sticky=W+E)
Button(root, text="%", bg="lightgrey", width=8, height=4, font=("arial",10), command=lambda: agregar_operador("%")).grid(row=2, column=2, sticky=W+E)
Button(root, text="/", bg="darkorange",width=8, height=4, font=("arial",10), command=lambda: agregar_operador("/")).grid(row=2, column=3, sticky=W+E)

Button(root, text="7", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: obtener_numeros(7)).grid(row=3, column=0, sticky=W+E)
Button(root, text="8", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: obtener_numeros(8)).grid(row=3, column=1, sticky=W+E)
Button(root, text="9", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: obtener_numeros(9)).grid(row=3, column=2, sticky=W+E)
Button(root, text="*", bg="darkorange",width=8, height=4, font=("arial",10),command=lambda: agregar_operador("*")).grid(row=3, column=3, sticky=W+E)

Button(root, text="4", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: obtener_numeros(4)).grid(row=4, column=0, sticky=W+E)
Button(root, text="5", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: obtener_numeros(5)).grid(row=4, column=1, sticky=W+E)
Button(root, text="6", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: obtener_numeros(6)).grid(row=4, column=2, sticky=W+E)
Button(root, text="-", bg="darkorange",width=8, height=4, font=("arial",10),command=lambda: agregar_operador("-")).grid(row=4, column=3, sticky=W+E)

Button(root, text="1", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: obtener_numeros(1)).grid(row=5, column=0, sticky=W+E)
Button(root, text="2", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: obtener_numeros(2)).grid(row=5, column=1, sticky=W+E)
Button(root, text="3", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: obtener_numeros(3)).grid(row=5, column=2, sticky=W+E)
Button(root, text="+", bg="darkorange",width=8, height=4, font=("arial",10),command=lambda: agregar_operador("+")).grid(row=5, column=3, sticky=W+E)

Button(root, text="0", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: obtener_numeros(0)).grid(row=6, columnspan=2, sticky=W+E)#ver
Button(root, text=".", bg="grey",  width=8, height=4, font=("arial",10),command=lambda: agregar_operador(".")).grid(row=6, column=2, sticky=W+E)
Button(root, text="=", bg="darkorange",width=8, height=4, font=("arial",10), command=lambda: operacion()).grid(row=6, column=3, sticky=W+E)


root.mainloop()
