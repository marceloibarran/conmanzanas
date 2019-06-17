import requests
import time
from bs4 import BeautifulSoup
import json
import os.path

data = {}
data['Productos'] = []
paises = {}
paises['pais'] = []




pais = ['chile']
product =['precios-supermercado','precio-restaurantes','precio-ropa-calzado','precio-transporte-servicios','precio-vivienda-salarios','precio-ocio-deportes']

for index in pais:
        
    url = 'https://preciosmundi.com/'+index
    for i in product:
        ur = url+'/'+i
        r = requests.get(ur)

        soup = BeautifulSoup(r.content, "html.parser")
        tbody_total = soup.find_all('tbody')

        for tbody in tbody_total:
            tr_tabla = tbody.find_all('tr')

            for tr_dato in tr_tabla:
                nombre = tr_dato.find('td', class_='product-name').get_text().strip()
                precio_peso = tr_dato.find_all('td', class_='price')[0].get_text().strip()
                cantidad = len(precio_peso)
                precio_peso = precio_peso[:cantidad-1]
                precio_dolar = tr_dato.find_all('td', class_='price')[1].get_text().strip()
                cantidad = len(precio_dolar)
                precio_dolar= precio_dolar[:cantidad-1]
                precio_euro = tr_dato.find_all('td', class_='price')[2].get_text().strip()
                cantidad = len(precio_euro)
                precio_euro = precio_euro[:cantidad-1]





