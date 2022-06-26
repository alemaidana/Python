import sqlite3

#crear conexion
conn = sqlite3.connect("customer.db")

#crear un cursor
c = conn.cursor()

#--------Ordenar la base de datos --------

c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

elementos = c.fetchall()

for elemento in elementos:
	print(elemento)


#commit nuestro comando
conn.commit()

#cerramos la conexion
conn.close()