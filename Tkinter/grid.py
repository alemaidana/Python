from tkinter import *

root = Tk()

#Creando una etiqueta para la ventana
myLabel = Label(root, text = "Hola mundo!").grid(row = 0, column = 0)
myLabel2 = Label(root, text = "Mi nombre es Alfredo").grid(row = 1, column = 1)

#final del ciclo del programa
root.mainloop()

