"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
#       Recordar intarlar
#           sudo python -m pip install pymongo
#       Libre necesarias para conectar a MongoDB con Python
import pymongo

#from pymongo import MongoClient
import pprint
#import MySQLdb

#Ultima pureba con:mysql-connector-python
import mysql.connector
#from MySQLdb import _mysql
#from models import 
import json


#from yourproject.models import Poll, Choice
#                        importar clases hechas en archivo models,py
#                        Para usar esos modelos para CRUD MongoDB

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Aplicacion para transpasar datos del sensor FreeStyle Libre de MongoDB a MySql',
            'year':datetime.now().year,
        }
    )
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def ConexionMongoDB(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)

    # conexión con mongo
    #client = pymongo.MongoClient("mongodb+srv://Prueba:prueba@cluster0.xv7cj.mongodb.net/Prueba?retryWrites=true&w=majority")
    #   PARA PRUEBA LOCAL
    client = pymongo.MongoClient("mongodb://localhost:27017")
    

    #   https://www.w3schools.com/python/python_mongodb_query.asp
    # conexión con la base de datos
    db = client['Prueba']
    #db = client.Prueba
    #   PARA PRUEBA LOCAL
    #db = client.local

    # dentro de Prueba elegimos la colecciónn
    #collection = db.entries
    collection = db['entries']
    #   PARA PRUEBA LOCAL
    #collection = db.startup_log
    #dictsensor = {
    #    "date":1599,
    #    "dateString":"2020-09-01T22:56:30.000Z",
    #    "rssi":100,
    #    "device":"glimp://libre/0M0060Y7HP4",
    #    "direction":"NOT COMPUTABLE",
    #    "rawbg":136,
    #    "sgv":136,
    #    "type":"sgv",
    #    "utcOffset":-300,
    #    "sysTime":"2020-09-01T22:56:30.000Z",
    #    }
    #x = collection.insert_one(dictsensor)
    #Impresion de datos
    #print(x.inserted_id) //Arroja el ID con el que se almacena
    #print(db.list_collection_names())
    for x in collection.find():
        print(x)
        

    #for cursor in collection.find():
    #    pprint.pprint(cursor)
    

    #   https://jarroba.com/python-mongodb-driver-pymongo-con-ejemplos/
    #mongoClient = MongoClient('localhost',27017)
    return render(
        request,
        'app/ConexionMongoDB.html',
        {
            'title':'Conexion y lectura Django a MongoDB',
            'message':'Pagina de prueba para conexion con MongoDB desde Django.',
            'year':datetime.now().year,
        }
    )
def ConexionMysql(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    # conexión con MySql
    #   DOCUMENTACION DE:
    #   https://www.w3schools.com/python/python_mysql_select.asp
    
    #   PARA PRUEBA LOCAL
    #   ---------------------------------------------
    #db =_mysql.connect(host="localhost",user="root",
    #              passwd="admin",db="prueba")

    # Accessing an existing table
    #db.query("""select * from tabla_prueba""")
    
    #Impresion de datos
    #res=db.store_result()
    #print(res.fetch_row)
    #   ---------------------------------------------
    
    #   Conexion con la base de datos PC Universidad
    db = mysql.connector.connect(user='root',
                         db='pruebatesis',
                         passwd='admin',
                         host='localhost'  )
    #   Conexion con la base de datos PC Local
    #db = MySQLdb.connect(user='root', db='pruebatesis', passwd='Gsc98082457704', host='localhost')
    
    mycursor = db.cursor()
    #mycursor.execute("SHOW DATABASES")
    #for x in mycursor:
    #    print(x)
    #cursor.execute("SHOW TABLES")
    #   QUERY
    mycursor.execute('SELECT * FROM sensorFreeStyle')
        
    #myresult = mycursor.fetchall()
    for x in mycursor:
        print( x )
    db.close()

    #   https://jarroba.com/python-mongodb-driver-pymongo-con-ejemplos/
    #mongoClient = MongoClient('localhost',27017)
    return render(
        request,
        'app/ConexionMysql.html',
        {
            'title':'Conexion y lectura Django a Mysql',
            'message':'Pagina de prueba para conexion con MongoDB desde Mysql.',
            'year':datetime.now().year,
        }
    )

def TranspasoMongoDB_Mysql(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    
    # conexión con mongo
    #client = pymongo.MongoClient("mongodb+srv://Prueba:prueba@cluster0.xv7cj.mongodb.net/Prueba?retryWrites=true&w=majority")
    #   PARA PRUEBA LOCAL
    client = pymongo.MongoClient("mongodb://localhost:27017")
    # conexión con la base de datos
    dbMongo = client['Prueba']
         
    # dentro de Prueba elegimos la colecciónn
    collection = dbMongo['entries']
    
    #x = collection.insert_one(dictsensor)
    #Impresion de datos
    lista = []
    for valFreestyle in collection.find():
        valFreestyle.pop('_id')
        valFreestyle['date'] = int(valFreestyle['date'])
        listaAux = valFreestyle.values()
        #listaAux.pop('_id')
        listas = tuple(listaAux)
        lista.append(listas)

    for item in lista:
        print(item)


    #   Conexion con la base de datos MySql PC Universidad
    db = mysql.connector.connect(user='root',
                         db='pruebatesis',
                         passwd='admin',
                         host='localhost'  )
    
    mycursor = db.cursor()
    #str(Contenido a convertir)
    #   QUERY
    #querry = """INSERT INTO sensorFreeStyle (date,dateString,rssi,device,direction,rawbg,sgv,type,utcOffset,sysTime) VALUES (%d,%s,%d,%s,%s,%d,%d,%s,%d,%s)"""
    querry = "INSERT INTO sensorFreeStyle (date,dateString,rssi,device,direction,rawbg,sgv,type,utcOffset,sysTime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    querry2 = "INSERT INTO sensorFreeStyle (date,dateString,rssi,device,direction,rawbg,sgv,type,utcOffset,sysTime) VALUES (%d,'%s',%d,'%s','%s',%d,%d,'%s',%d,'%s')"
    print("-------")
    print(type(lista[0][0]))#'int'
    print(type(lista[0][1]))#'str'
    print(type(lista[0][2]))#'int'
    print(type(lista[0][3]))#'str'
    print(type(lista[0][4]))#'str'
    print(type(lista[0][5]))#'int'
    print(type(lista[0][6]))#'int'
    print(type(lista[0][7]))#'str'
    print(type(lista[0][8]))#'int'
    print(type(lista[0][9]))#'str'
    print("-------")
    #print(querry % (lista[0]))
    listaQuerry = []
    i= 0
    for item in lista:
        listaQuerry.append(querry2 % item)
        #print(listaQuerry[i])
        i+=1
    #for indice in listaQuerry:
        #print(indice)
        #respuesta = mycursor.execute(indice)

    #querry3 = "INSERT INTO customers (name, address) VALUES (%s,%s)"
    #mycursor.execute(querry3,('rr','rr'))
    #querry3 = "INSERT INTO customers (name, address) VALUES ('rr','rr')"
    #mycursor.execute(querry3)
    
    try:
        mycursor.executemany(querry,lista)
        db.commit()
    except:
        print("Eror: "+ error)
    
    print("Number record inserted, ID:", mycursor.lastrowid)
    db.close()    
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'lista':lista,
        }
    )
#https://dev.mysql.com/doc/connector-python/en/connector-python-tutorial-cursorbuffered.html
#https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html