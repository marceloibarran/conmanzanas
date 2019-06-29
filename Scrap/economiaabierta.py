import requests
import json
from datetime import date

def modifica_fecha_publicacion(fecha_old):
    dia = fecha_old[0:2]
    mes = fecha_old[3:5]
    ano = fecha_old[6:10]
    fecha_new = ano+'-'+mes+'-'+dia
    return fecha_new

resp = requests.get('https://api.datos.sernac.cl/api/v2/dashboards/PRECI-MEDIC.json/?auth_key=edbb95d24d7caeeb9dc6a0da35bc5a3c1fed957d')

list_precio_medicamento = json.loads(resp.content)

page = 0
validador = 0

ultimo = list_precio_medicamento['resources'][0]
guid = ultimo['guid'].strip()



while validador == 0:
    link = "https://api.datos.sernac.cl/api/v2/datastreams/" + guid + "/data.pjson/?auth_key=edbb95d24d7caeeb9dc6a0da35bc5a3c1fed957d&limit=50&page=" + str(
        page)

    lista_producto = requests.get(link)
    lista_producto_json = json.loads(lista_producto.content)
    if len(lista_producto_json['result']) == 1:
        validador = 1
        pass
    page = page + 1
    for c in range(0, 49):
        lista_medicamento = lista_producto_json['result'][c]
        nombre = lista_medicamento['Glosa_Producto-Principio-Activo']
        precio = 3

        fecha_publicacion = modifica_fecha_publicacion(lista_medicamento['Fecha'])

        fecha_hoy = date.today()
        fuente = 'https://datos.sernac.cl/dashboards/20611/precios-medicamentos/'

        print(nombre)
        print(precio)
        print(fecha_publicacion)
        print(fecha_hoy)
        print(fuente)

        pass


