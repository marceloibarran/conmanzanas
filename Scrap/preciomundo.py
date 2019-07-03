import requests
from bs4 import BeautifulSoup
from datetime import date
import consulta

product = ['precios-supermercado']
paises= consulta.lista_pais()
def busca_mes(mes):
    diccionario = {'enero': '01', 'febrero':'02','marzo':'03','abril':'04','mayo':'05','junio':'06','julio':'07','agosto':'08','septiembre':'09','obtubre':'10','noviembre':'11','diciembre':'12'}
    for mes_list in diccionario:
        if mes == mes_list:
            return diccionario[mes_list]
        pass
    return '01'
    pass

#funcion que genera fecha de actualizacion
def fecha_actializacion(fecha):
    total_cadena = len(fecha)
    direc = 0
    fecha= fecha[16:total_cadena-1]

    while fecha[direc] != ' ':
        direc = direc + 1
        mes = fecha[0:direc]
        ano = fecha[direc+4:]
    fecha_final = ano+'-'+busca_mes(mes)+'-01'
    return fecha_final
    pass

def pulir_precio(precio):
    precio_new = precio.replace(',','')
    r = 'False'
    v = 0
    while str(r) == 'False':
        v = v + 1
        r = precio_new.isdigit()
        precio_new = precio_new[0:len(precio_new)-1]

    return precio_new


for pais in paises:
    pais_new = pais[0].replace(' ', '-')
    url = 'https://preciosmundi.com/' + pais_new
    print(pais_new)
    for i in product:
        ur = url + '/' + i
        r = requests.get(ur)

        soup = BeautifulSoup(r.content, "html.parser")
        fecha_actualizacion_final = fecha_actializacion(soup.find('p').get_text().strip())
        tbody_total = soup.find_all('tbody')




        for tbody in tbody_total:
            tr_tabla = tbody.find_all('tr')

            for tr_dato in tr_tabla:

                nombre = tr_dato.find('td', class_='product-name').get_text().strip()
                precio = pulir_precio(tr_dato.find_all('td', class_='price')[0].get_text().strip())
                fecha_obtencion_dato = date.today()
                fuente = ur

                print(nombre)
                print(precio)
                print(fecha_actualizacion_final+' fecha de actualizacion')
                print(fecha_obtencion_dato)
                print(fuente)
                print('-----------')








