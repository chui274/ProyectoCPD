from multiprocessing.connection import Client
from array import array
import sqlite3
import cPickle 

	# Conexion
conndb= sqlite3.connect('cliente.db')
	# creamos un cursor por el 
	# cual podremos ejecutar comandos 
	# SQL via el metodo execute
c= conndb.cursor()
# c.execute('''CREATE TABLE yahoo(symbol text, last text, fecha text, change text, high text, low text, vol text, send int)''')
address = ('localhost',6000)
conn = Client(address)
conn.send('close')
msg = conn.recv()

replicado= 1

c.execute('INSERT INTO yahoo values(:symbol, :last, :fecha, :change, :high, :low, :vol)', msg)
c.execute('SELECT * FROM yahoo')
resultado = c.fetchall()
print (resultado)
conndb.commit()# Guardar cambios
conndb.close()



conn.close()
print ("Conexion exitosa")
