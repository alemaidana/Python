#Creamos una contraseña en una variable
clave = "python"

#Creamos una respuesta para ver si acertamos a la contraseña
#(la creamos vacia para poder despues preguntar al usuario)
respuesta = " "

#creamos un ciclo while que se va a repetir indefinidamente
#hasta que el el usuario acierte la contraseña
while respuesta != clave:


#entonces nuesta condicion de salida sera unicamente que el usuario
#acierte la contraseña
	respuesta = input("Ingresa la contraseña: ")


#aqui afuera del ciclo while un mensaje para mostrar que el programa
#sigue normalmente
print("Continuacion del programa normalmente")	
