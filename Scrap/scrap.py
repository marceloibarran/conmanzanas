import requests
import time
from bs4 import BeautifulSoup
import json
import os.path

data = {}
data['Productos'] = []
paises = {}
paises['pais'] = []


pais = ['afganistan', 'albania', 'alemania', 'andorra','angola','arabia-saudita','argelia','argentina','armenia','australia','austria','bahrein','bangladesh','belgica','bielorrusia','bolivia','bosnia-y-herzegovina','brasil','bulgaria','butan','cabo-verde','camboya','camerun','canada','catar','chile','china','chipre','colombia','corea-del-sur','croacia','dinamarca','ecuador','egipto','el-salvador','emiratos-arabes-unidos','eslovaquia','eslovenia']
#pais = ['afganistan','albania']
#product =['precios-supermercado','precio-restaurantes','precio-ropa-calzado','precio-transporte-servicios','precio-vivienda-salarios','precio-ocio-deportes']
product = ['precios-supermercado']

for index in pais:
        
    url = 'https://preciosmundi.com/'+index
    for i in product:
        ur = url+'/'+i
        print(ur)
        r = requests.get(ur)
        soup = BeautifulSoup(r.content)
        
        for b in range(0,15):
            descripcionsuper = soup.find_all('td',class_='product-name')[b]
            preciosuper = soup.find_all('td',class_='price')[b]
            
                
            
            data['Productos'].append({
             
             'pagina': soup.title.text,
             'nombre': descripcionsuper.text,
             'precio Peso Chileno':preciosuper.text,
             'url': url,
             'fechaScrapy': time.strftime("%m-%d-%Y-%H-%M-%S"),
            
            }) 
dir = os.path.dirname(os.path.abspath(__file__)) + '/data'

file_name ='archivo__'+time.strftime("%m-%d-%Y-%H-%M-%S")+'.json'

with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

        