from multiprocessing.connection import Client
from array import array
import sqlite3
#Conexion
conexiondb= sqlite3.connect('proyectoCPD2.db')
#creamos un cursor, por el cual podremos ejecutar comandos SQL vía el método execute.
c= conexiondb.cursor()

address = ('compute-0-1',5901)
conexion = Client(address, authkey= 'sofia')
conexion.send('close')
leido = conn.recv()

replicado= 1
c.execute("insert into yahoo values (:symbol, :last, :date, :change, :high, :low, :vol, 1)", leido)
c.execute("select * from yahoo")
print c.fetchall()
conexiondb.commit()#Guardar cambios
conexiondb.close()



conexion.close()
print "Conexion exitosa"
