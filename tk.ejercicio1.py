from tkinter import * 
i=0
def increment(num):
    num+=1
    if num == 1:
        pass
    display.delete(0, END)
    display.insert(END, num)

ventana=Tk()
ventana.title("ContCreciente")
ventana.configure(bg="pink")
ventana.geometry("390x190")

mylabel=Label(ventana, text="Contador")#Label, te deja introducir una imagen o un texto estático
mylabel.grid(row=0,column=5, pady=50, padx=20)#ipady, margen interno

display= Entry(ventana, justify='center')
display.grid(row=0,column=6, pady=60, padx=20)

Button(ventana, text="+", command=lambda:increment(int(display.get()))).grid(row=0, column=7, pady=70, padx=20)

ventana.mainloop()