from tkinter import *

root = Tk()

root.title("Calculadora simple")

root.configure(bg = "#282a36")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#funciones
def boton_click(numero):
	actual = e.get()
	e.delete(0, END)
	e.insert(0, str(actual) + str(numero))


def boton_borrar():
	e.delete(0, END)


def boton_suma():
	primer_numero = e.get()
	global p_num 
	global math
	math = "suma"
	p_num = int(primer_numero)
	e.delete(0, END)


def boton_resta():
	primer_numero = e.get()
	global p_num 
	global math
	math = "resta"
	p_num = int(primer_numero)
	e.delete(0, END)


def boton_multiplicacion():
	primer_numero = e.get()
	global p_num 
	global math
	math = "multiplicacion"
	p_num = int(primer_numero)
	e.delete(0, END)


def boton_division():
	primer_numero = e.get()
	global p_num
	global math
	math = "division" 
	p_num = int(primer_numero)
	e.delete(0, END)



def boton_igual():
	segundo_numero = e.get()
	e.delete(0, END)

	if math == "suma":
		resultado = p_num + int(segundo_numero)
		e.insert(0, resultado)
	
	if math == "resta":
		resultado = p_num - int(segundo_numero)
		e.insert(0, resultado)
	
	if math == "multiplicacion":
		resultado = p_num * int(segundo_numero)
		e.insert(0, resultado)
	
	if math == "division":
		resultado = p_num / int(segundo_numero)
		e.insert(0, float(resultado))
	
#Definir botones

Button1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: boton_click(1), bg = "#44475a" , fg = "#f8f8f2")
Button2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: boton_click(2), bg = "#44475a" , fg = "#f8f8f2")
Button3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: boton_click(3), bg = "#44475a" , fg = "#f8f8f2")
Button4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: boton_click(4), bg = "#44475a" , fg = "#f8f8f2")
Button5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: boton_click(5), bg = "#44475a" , fg = "#f8f8f2")
Button6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: boton_click(6), bg = "#44475a" , fg = "#f8f8f2")
Button7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: boton_click(7), bg = "#44475a" , fg = "#f8f8f2")
Button8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: boton_click(8), bg = "#44475a" , fg = "#f8f8f2")
Button9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: boton_click(9), bg = "#44475a" , fg = "#f8f8f2")
Button0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: boton_click(0), bg = "#44475a" , fg = "#f8f8f2")

Button_suma = Button(root, text = "+", padx = 40, pady = 20, command = boton_suma, bg = "#44475a" , fg = "#f8f8f2")
Button_resta = Button(root, text = "-", padx = 41, pady = 20, command = boton_resta, bg = "#44475a" , fg = "#f8f8f2")
Button_multiplicacion = Button(root, text = "*", padx = 40, pady = 20, command = boton_multiplicacion, bg = "#44475a" , fg = "#f8f8f2")
Button_division = Button(root, text = "/", padx = 41, pady = 20, command = boton_division, bg = "#44475a" , fg = "#f8f8f2")

Button_igual = Button(root, text = "=", padx = 91, pady = 20, command = boton_igual, bg = "#44475a" , fg = "#f8f8f2")
Button_borrar = Button(root, text = "DEL", padx = 79, pady = 20, command = boton_borrar, bg = "#44475a" , fg = "#f8f8f2")


#poner botones en pantalla
Button1.grid(row =3 , column =0)
Button2.grid(row =3 , column =1)
Button3.grid(row =3 , column =2)

Button4.grid(row = 2, column =0)
Button5.grid(row = 2, column =1)
Button6.grid(row = 2, column =2)

Button7.grid(row = 1, column =0)
Button8.grid(row = 1, column =1)
Button9.grid(row = 1, column =2)

Button0.grid(row = 4, column =0)


Button_borrar.grid(row = 4, column =1, columnspan = 2)
Button_suma.grid(row = 5, column =0)
Button_igual.grid(row = 5, column =1, columnspan = 2)

Button_resta.grid(row = 6, column =0)
Button_multiplicacion.grid(row = 6, column =1)
Button_division.grid(row = 6, column =2)


root.mainloop()