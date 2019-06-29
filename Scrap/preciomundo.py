import requests
from bs4 import BeautifulSoup
from datetime import datetime, date



#paises = ['afganistan','albania','alemania','andorra','angola','arabia-saudita','argelia','argentina','armenia','australia','austria','bahrein','bangladesh','belgica','bielorrusia','bolivia','bosnia-herzegovina','brasil','bulgaria','butan','cabo-verde','camboya','camerun','canada','catar','chile','china','chipre','colombia','corea-del-sur','costa-rica','croacia','dinamarca','ecuador','egipto','el-salvador','emiratos-arabes-unidos','eslovaquia','eslovenia','españa','estados-unidos','estonia','filipinas','finlandia','francia','georgia','ghana','grecia','guatemala','haiti','hong-kong','hungria','india','indonesia','irak','iran','irlanda','islandia','israel','italia','jamaica','japon','jordania','kazajstan','kenia','']
product = ['precios-supermercado']
paises= ['peru']
#diccionario de paises con tipo de moneda peso
lista_pais_peso = {'chile':'Peso Chileno', 'argentina': 'Peso Argentino', 'uruguay': 'Peso Uruguayo', 'mexico': 'Peso Mexicano'}
validador = 0

#funcion que obtiene el tipo de moneda
def tipo_moneda(tipo_precio):
    total_cadena = len(tipo_precio)
    direc = total_cadena - 1
    while tipo_precio[direc] != ' ':
        direc = direc - 1
        tipo_valor_filtrado = tipo_precio[0:direc]
        pass
    return tipo_valor_filtrado
    pass


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

    for pais_lista in lista_pais_peso:
        if pais == pais_lista:
            #cambia a 1 cuando es un tipo de pais con moneda tipo peso
            validador = 1
            tipo_valor_filtrado= lista_pais_peso[pais_lista]
            pass
        pass



    url = 'https://preciosmundi.com/' + pais
    for i in product:
        ur = url + '/' + i
        r = requests.get(ur)

        soup = BeautifulSoup(r.content, "html.parser")
        fecha_actualizacion_final = fecha_actializacion(soup.find('p').get_text().strip())


        tbody_total = soup.find_all('tbody')


        #valida si pais es con moneda peso
        if validador == 0:
            #se obtiene el tipo de moneda
            tipo_valor_filtrado = tipo_moneda(soup.find_all('th')[1].get_text().strip())

        for tbody in tbody_total:
            tr_tabla = tbody.find_all('tr')

            for tr_dato in tr_tabla:

                nombre = tr_dato.find('td', class_='product-name').get_text().strip()
                precio = pulir_precio(tr_dato.find_all('td', class_='price')[0].get_text().strip())
                fecha_obtencion_dato = date.today()
                fuente = ur

                print(nombre)
                print(precio)
                print(tipo_valor_filtrado)
                print(fecha_actualizacion_final+' fecha de actualizacion')
                print(fecha_obtencion_dato)
                print(fuente)
                print('-----------')








