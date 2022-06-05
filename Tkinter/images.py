from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Aprendiendo a usar Tkinter")


#icono en la ventana (solo .ico)
root.iconbitmap("C:/Users/Usuario/Desktop/Python/Tkinter/estudiante.ico")

#guardamos la imagen en una etiqueta
mi_imagen = ImageTk.PhotoImage(Image.open("perrini.png"))
mi_etiqueta = Label(image=mi_imagen)
mi_etiqueta.pack()

#boton de salir
boton_salir = Button(root, text="Salir", command=root.quit)
boton_salir.pack()


root.mainloop()