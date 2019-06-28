import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
import time

def pulir_precio(precio_old):
    total_cadena = len(precio_old)
    p_sin = precio_old[2:total_cadena]
    precio_p = p_sin.replace('.','')
    return precio_p
    pass

def pulir_nombre(nombre):
    posicion = nombre.find(' ')
    total = len(nombre)
    if nombre[posicion-1] == '*':
        return nombre[posicion:total]
    return nombre
    pass

for cate in range(1,10):
    if cate != 8:
        link = 'https://www.ccdm.cl/aranceles-vigentes/?prevision=1&atencion=1&cate='+str(cate)
        rest = requests.get(link)
        soup = BeautifulSoup(rest.content, "html.parser")
        tr = soup.find_all('tr', class_='tr-categorias')

        for td in tr:
            nombre = pulir_nombre(td.find_all('td')[1].get_text().strip())
            precio = pulir_precio(td.find_all('td')[2].get_text().strip())
            fecha_obtencion_dato = date.today()
            fecha_actualizacion = date.today()
            fuente = link
            print(nombre)
            print(precio)
            print(fecha_obtencion_dato)
            print(fecha_actualizacion)
            print(fuente)





            pass
        time.sleep(5)