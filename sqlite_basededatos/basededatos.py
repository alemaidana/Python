import sqlite3

#--------Consultar la base de datos --------

#mostrar todos los registros
def mostrar_todo():
    conn = sqlite3.connect("customer.db")	
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")	
    elementos = c.fetchall()	  	
    for elemento in elementos:
	    print(elemento)

    conn.commit()

    conn.close()

#agrega un registro a la vez
def agregar(nombre, apellido, correo):
    conn = sqlite3.connect("customer.db")	
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)",(nombre, apellido, correo))
    conn.commit()
    conn.close()


#agrega varios registros a la vez
def agregar_varios(lista):
    conn = sqlite3.connect("customer.db")	
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", lista)
    conn.commit()
    conn.close()


#Borra un registro por id
def borrar_registro(id):
    conn = sqlite3.connect("customer.db")	
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()











