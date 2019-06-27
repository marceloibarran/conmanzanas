import sqlite3
import json
def Subir_Paises():
    paises = json.load(open('file.json'))
    for pais in paises:
        paist= pais['Pais']
        print(paist)
        con = sqlite3.connect('/home/jaimemor/Escritorio/Taller/Proyecto/conmanzanas/Scrap/db.sqlite3')
        cursor = con.cursor()
        sql = "INSERT INTO basedatos_pais(idpais, nombrep) VALUES(Null,'"+paist+"')"
        cursor.execute(sql)
        con.commit()
        con.close()
def Subir_Region():
    regiones = json.load(open('file.json'))
    for region in regiones:
        regiont= region['Continente']
        con = sqlite3.connect('/home/jaimemor/Escritorio/Taller/Proyecto/conmanzanas/Scrap/db.sqlite3')
        cursor = con.cursor()
        #sql= "INSERT INTO basedatos_region(idreg, nombreg, idpais_id) VALUES(Null,'""')"
        cursor.execute(sql)
        con.commit()
        con.close()
