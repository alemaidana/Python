import sqlite3

#crear conexion
conn = sqlite3.connect("customer.db")

#crear un cursor
c = conn.cursor()

#--------Actualizar la base de datos --------

c.execute("""UPDATE customers SET first_name = 'Alfredo'
	WHERE rowid = 1
	""")




c.execute("SELECT rowid, * FROM customers")

elementos = c.fetchall()

for elemento in elementos:
	print(elemento)


#commit nuestro comando
conn.commit()

#cerramos la conexion
conn.close()