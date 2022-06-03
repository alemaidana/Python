from tkinter import *

root = Tk()

def elClick():
	mensaje = Label(root, text = "Miren hice click en el boton")
	mensaje.pack()


#Creando una etiqueta para la ventana
myButton = Button(root, text = "Clickeame", command = elClick, fg = "blue", bg = "yellow")
#boton desactivado
#myButton2 = Button(root, text = "Hazme click", state = DISABLED)
#boton con otro tamaño
#myButton3 = Button(root, text = "click", padx = 50, pady = 50)


myButton.pack()
#myButton2.pack()
#myButton3.pack()

#final del ciclo del programa
root.mainloop()

