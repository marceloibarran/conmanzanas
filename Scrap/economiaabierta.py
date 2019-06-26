import requests
import json

resp = requests.get('https://api.datos.sernac.cl/api/v2/dashboards/PRECI-MEDIC.json/?auth_key=edbb95d24d7caeeb9dc6a0da35bc5a3c1fed957d')

list_precio_medicamento = json.loads(resp.content)

page = 0
for x in list_precio_medicamento['resources']:
    guid = x['guid']



    link = "https://api.datos.sernac.cl/api/v2/datastreams/"+guid+"/data.pjson/?auth_key=edbb95d24d7caeeb9dc6a0da35bc5a3c1fed957d&limit=50&page="


