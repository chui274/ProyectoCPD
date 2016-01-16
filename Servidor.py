from multiprocessing.connection import Listener
from array import array
import urllib2
import sqlite3


def getYahooStockQuote(symbol):
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1c1hgv" % symbol
    f = urllib2.urlopen(url)
    s = f.read()
    f.close()
    s = s.strip()
    L = s.split(',')
    D = {}
    D['symbol'] = L[0].replace('"','')
    D['last'] = L[1]
    D['date'] = L[2]
    D['change'] = L[3]
    D['high'] = L[4]
    D['low'] = L[5]
    D['vol'] = L[6]
    return D
#Conexion
conexiondb= sqlite3.connect('proyectoCPD.db')
#Creación cursor
c= conexiondb.cursor()



address = ('compute-0-0',6000)
listener =Listener(address, authkey='sofia')
conexion = listener.accept()
print'connection accepted from', listener.last_accepted
while True:
    mensaje = conexion.recv()
    leido= getYahooStockQuote('GOOG')
    conexion.send(leido)
    replicado= 1
    c.execute("insert into yahoo values (:symbol, :last, :date, :change, :high, :low, :vol, 1)", leido)
    c.execute("select * from yahoo")
    print c.fetchall()
    conexiondb.commit()#Guardar cambios
    conexiondb.close()


    if msg =='close':
            conexion.close()
            break






listener.close()
