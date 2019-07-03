import sqlite3
import json
def ac(name):
    name = name.replace('á','a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    return (name)
def Subir_Paises():
    paises = json.load(open('/home/jaimemor/Escritorio/Taller/git/conmanzanas/file.json'))
    for pais in paises:
        con = sqlite3.connect('/home/jaimemor/Escritorio/Taller/git/conmanzanas/db.sqlite3')
        cursor = con.cursor()

        sql="SELECT nombrep FROM basedatos_pais"
        s=cursor.execute(sql)
        regiont = ac(pais['Continente'].lower())
        pa= ac(pais['Pais'].lower())
        for a in s:
            b= a[0]

            if b == pa:
                print("pase")
                v=cursor.execute("SELECT idpais FROM basedatos_pais")
                for vv in v:
                    g=vv[0]
                    ins = """"INSERT INTO basedatos_region VALUES(?,?,?)""", (None, g, regiont)
                    cursor.execute(ins)



Subir_Paises()
