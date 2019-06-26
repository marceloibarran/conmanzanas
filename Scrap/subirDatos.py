import sqlite3
import json
paises = json.load(open('Paises.json'))
for pais in paises:
    paist= pais['Pais']
    con = sqlite3.connect('/home/jaimemor/Escritorio/Taller/Proyecto/conmanzanas/Scrap/db.sqlite3')
    cursor = con.cursor()
    sql = "INSERT INTO basedatos_pais(idpais, nombrep) VALUES(Null,'"+paist+"')"
    cursor.execute(sql)
    con.commit()
    con.close()

