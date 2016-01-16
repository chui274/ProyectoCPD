from multiprocessing.connection import Client
from array import array
import sqlite3

conndb= sqlite3.connect('proyectoCPD2.db')
c= conndb.cursor()

address = ('compute-0-0',6000)
conn = Client(address, authkey= 'sofia')
conn.send('close')
leido = conn.recv()

replicado= 1
c.execute("insert into yahoo values (:symbol, :last, :date, :change, :high, :low, :vol, 1)", leido)
c.execute("select * from yahoo")
print c.fetchall()
conndb.commit()
conndb.close()



conn.close()
print "Conexion exitosa"
