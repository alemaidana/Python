import sqlite3

#crear conexion
conn = sqlite3.connect("customer.db")

#crear un cursor
c = conn.cursor()

#--------crear tablas--------
#c.execute("""CREATE TABLE customers (
#first_name text,
#last_name text,
#email text
#)""")

#Tipos de datos
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#--------insertar datos--------
#c.execute("""INSERT INTO customers VALUES (
#'Brian',
#'Alcaraz',
#'AnimeBrian@gmail.com'
#)""")

#--------insertar muchos datos--------

#lista_clientes = [
					#('Carolina', 'Avigliano', 'cvigliano@gmail.com'),
					#('Nora', 'Wexler', 'nora_3@gmail.com'),
					#('Walter', 'Pintos', 'wally_box@gmail.com'),

#]

#ejecutar muchos
#c.executemany("INSERT INTO customers VALUES (?,?,?)", lista_clientes)


#--------Consultar la base de datos--------

#c.execute("SELECT rowid,* FROM customers")

#c.fetchone()
#c.fetchmany(3)
#c.fetchall()

#se guarda en lista para despues mostrar iterado
#elementos = c.fetchall()

#impreso sin rowid pero con formato
#for elemento in elementos:
	#print(elemento[0] + " " + elemento[1] + " \t" + elemento[2])

#impreso con rowid
#for elemento in elementos:
#	print(elemento)

#--------Consultar la base de datos WHERE--------

c.execute("SELECT * FROM customers WHERE last_name = 'Maidana'")

elementos = c.fetchall()

for elemento in elementos:
	print(elemento)


#commit nuestro comando
conn.commit()

#cerramos la conexion
conn.close()