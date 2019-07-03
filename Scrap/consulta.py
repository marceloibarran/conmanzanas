import sqlite3


def buscar_dato_pais(pais):
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT idpais from basedatos_pais WHERE nombrep ="+str(pais))
    rows = c.fetchall()
    for row in rows:
        print(row[0])

    conn.commit()
    conn.close()

def lista_pais():
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT nombrep from basedatos_pais")
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return rows



