from multiprocessing.connection import Client
from array import array
import sqlite3
#Conexion
conndb= sqlite3.connect('proyectoCPD2.db')
#creamos un cursor, por el cual podremos ejecutar comandos SQL vía el método execute.
c= conndb.cursor()

address = ('compute-0-0',6000)
conn = Client(address, authkey= 'sofia')
conn.send('close')
leido = conn.recv()

replicado= 1
c.execute("insert into yahoo values (:symbol, :last, :date, :change, :high, :low, :vol, 1)", leido)
c.execute("select * from yahoo")
print c.fetchall()
conndb.commit()#Guardar cambios
conndb.close()



conn.close()
print "Conexion exitosa"
