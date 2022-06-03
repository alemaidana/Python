#Creamos una contraseña en una variable
clave = "python"

#Creamos una respuesta para ver si acertamos a la contraseña
#(la creamos vacia para poder despues preguntar al usuario)
respuesta = " "

#Creamos una cantidad de intentos
intentos = 3

#Creamos una variable para que el ciclo se repita
fin_de_ciclo = False

#creamos un ciclo while que se va a repetir indefinidamente
#hasta que el el usuario acierte la contraseña o pierda
#el total de los intentos
while not fin_de_ciclo:

	#mostramos al usuario la cantidad de intentos que tiene
	print("Cantidad de intentos disponibles:", intentos)

	respuesta = input("Ingresa la contraseña: ")


#entonces una de nuestas condiciones de salida sera que el usuario
#acierte la contraseña
	if respuesta == clave:

		#damos por verdadero el fin del ciclo y salimos del programa
		fin_de_ciclo = True
	else:
	
		#si no hemos acertado se nos restara un intento
		intentos -= 1 #esto es igual a intentos = intentos - 1


	
	#ahora debemos evaluar la segunda condicion de salida que
	#es que el usuario se quede sin intentos
	if intentos == 0:
		
		#mensaje al usuario
		print("Te has quedado sin intentos")
		#damos por verdadero el fin del ciclo y salimos del programa
		fin_de_ciclo = True		

#aqui afuera del ciclo while un mensaje para mostrar que el programa
#sigue normalmente
print("Continuacion del programa normalmente")	
