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

conndb= sqlite3.connect('proyectoCPD.db')
c= conndb.cursor()



address = ('compute-0-0',6000)
listener =Listener(address, authkey='sofia')
conn = listener.accept()
print'connection accepted from', listener.last_accepted 
while True:
    msg = conn.recv()
    leido= getYahooStockQuote('GOOG')
    conn.send(leido)
    replicado= 1
    c.execute("insert into yahoo values (:symbol, :last, :date, :change, :high, :low, :vol, 1)", leido)
    c.execute("select * from yahoo")
    print c.fetchall()
    conndb.commit()
    conndb.close()
    
    
    if msg =='close':
            conn.close()
            break
        
        
        
        
        

listener.close()
