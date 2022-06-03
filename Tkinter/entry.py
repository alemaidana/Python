from tkinter import *

root = Tk()

#campo de texto de entrada
e = Entry(root, width = 50)
e.pack()
e.insert(0, "Ingresa tu nombre")

def elClick():
	hola = "Hola " + e.get() 
	mensaje = Label(root, text = hola)
	mensaje.pack()


#Creando una etiqueta para la ventana
myButton = Button(root, text = "Ingresa tu nombre", command = elClick)


myButton.pack()

#final del ciclo del programa
root.mainloop()

