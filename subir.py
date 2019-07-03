import sqlite3
import json
import requests
def ac(name):
    name = name.replace('á','a')
    name = name.replace('é', 'e')
    name = name.replace('í', 'i')
    name = name.replace('ó', 'o')
    name = name.replace('ú', 'u')
    return (name)

con = sqlite3.connect('/home/jaimemor/Escritorio/Taller/git/conmanzanas/db.sqlite3')
cursor = con.cursor()
sql = "SELECT nombrep FROM basedatos_pais"
sq = cursor.execute(sql)
s= sq.fetchall()
for c in s:
    cons = str(c[0])

dir = '/home/jaimemor/Escritorio/Taller/git/conmanzanas/file.json'
paises = json.load(open(dir))
for pais in paises:
    p=ac(str(pais['Pais'].lower()))
    print(cons)






