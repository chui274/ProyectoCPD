from multiprocessing.connection import Listener
from array import array
import urllib2
import sqlite3
import cPickle 

conndb= sqlite3.connect('servidor.db')

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
    D['fecha'] = L[2]
    D['change'] = L[3]
    D['high'] = L[4]
    D['low'] = L[5]
    D['vol'] = L[6]
    return D



c= conndb.cursor()


address = ('localhost',6000)
listener =Listener(address)
conn = listener.accept()
print (('connection accepted from', listener.last_accepted))
while True:
    msg = conn.recv()
    leido= getYahooStockQuote('GOOG')
    conn.send(leido)
    replicado= 1
    # c.execute('''CREATE TABLE yahoo(symbol text, last text, fecha text, change text, high text, low text, vol text,send int)''')
    c.execute("INSERT INTO yahoo values(:symbol, :last, :fecha, :change, :high, :low, :vol)", leido)
    c.execute("SELECT * from yahoo")
    resultado=c.fetchall()
    print (resultado)
    conndb.commit()#Guardar cambios
    conndb.close()


    if msg =='close':
            packed = cPickle.dumps(leido)

            conn.close()
            break
    
    

listener.close()
