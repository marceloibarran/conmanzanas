import requests
import time
from bs4 import BeautifulSoup


paises = ['chile']
product = ['precios-supermercado']
lista_pais_peso = {'chile':'peso chileno'}

for pais in paises:

    url = 'https://preciosmundi.com/' + pais
    for i in product:
        ur = url + '/' + i
        r = requests.get(ur)

        soup = BeautifulSoup(r.content, "html.parser")
        tbody_total = soup.find_all('tbody')

        #se obtiene el tipo de moneda
        tipo_precio = soup.find_all('th')[1].get_text().strip()
        total_cadena= len(tipo_precio)
        direc = total_cadena-1
        while tipo_precio[direc] != ' ':
            direc = direc - 1
            tipo_valor_filtrado = tipo_precio[0:direc]
            pass


        for tbody in tbody_total:
            tr_tabla = tbody.find_all('tr')

            for tr_dato in tr_tabla:
                fecha_actualizacion = soup.find('p').get_text().strip()
                nombre = tr_dato.find('td', class_='product-name').get_text().strip()
                precio_peso = tr_dato.find_all('td', class_='price')[0].get_text().strip()
                cantidad = len(precio_peso)
                precio_peso = precio_peso[:cantidad - 1]
                print(nombre)
                print(tipo_valor_filtrado)
                print(precio_peso)
                print("-------------------")








