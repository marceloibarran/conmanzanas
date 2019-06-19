import json
import sqlite3

traffic = json.load(open('data/da.json'))
db = sqlite3.connect("bdtarea.sqlite")
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS bds
            ('nombre, precio_peso, precio_dolar, precio_euro')''')

query = "insert into bds values (?,?,?,?)"
columns = ['nombre', 'precio_peso', 'precio_dolar', 'precio_euro']
for timestamp, data in traffic.iteritems():
    keys = (timestamp,) + tuple(data[c] for c in columns)
    c = db.cursor()
    c.execute(query, keys)
    c.close()
traffic.close()
db.commit()
db.close()