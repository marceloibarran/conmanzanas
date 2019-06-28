import sqlite3
import json
def Subir_Paises():
    paises = json.load(open('file.json'))
    for pais in paises:
        paist= pais['Pais']
        con = sqlite3.connect('/home/jaimemor/Escritorio/Taller/Proyecto/conmanzanas/db.sqlite3')
        cursor = con.cursor()
        sql = "INSERT INTO basedatos_pais(idpais, nombrep) VALUES(Null,'"+paist+"')"
        cursor.execute(sql)
        pais_id = cursor.lastrowid
        regiont = pais['Continente']
        reg_id = cursor.lastrowid
        cursor.execute("""INSERT INTO basedatos_region VALUES(?,?,?)""", (None, pais_id, regiont));
        con.commit()
        con.close()




Subir_Paises()