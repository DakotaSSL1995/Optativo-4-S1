# -*- coding: utf-8 -*-
"""Mercado libre.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lcMTlQ1P2Zv_PMHblwbD4wAKGZDIMffP
"""

#Instalacion de requisitos
!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!pip install bs4
!pip install beautifulsoup4
!pip install pandas

#Importando librerias
import sys
from selenium import webdriver
import math
from bs4 import BeautifulSoup
import pandas as pd

#Configuraciones iniciales
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',options=options)

#Pagina principal
wd.get("https://listado.mercadolibre.cl/inmuebles/casas/")
 #Se obtiene el Html
html_code = wd.page_source
#Se crea un objeto apartir del html
soup = BeautifulSoup(html_code, 'lxml')
#Contador de resultados 
cantidad_c = float(soup.find(class_= "ui-search-search-result__quantity-results").text.split(" ")[0].replace(".",""))
#Contador de paginas
NumeroP = math.ceil(cantidad_c/48)

#Parceo de la direccion
def get_address(ubicacion):
  part = ubicacion.split(",")
  partAmount = len(part)
  if(partAmount == 3):
    return {'direccion' : part[0], 'ciudad' : part[1], 'region' : part[2]}
  elif(partAmount > 3): 
    return {'direccion' : " ".join(part[:len(part)-3]), 'cuidad' : part[partAmount-2], 'region' : part[partAmount-1]}
  elif(partAmount < 3): 
    for i in range(0,100):
      print("Error:")
      print(ubicacion)
    return {'direccion' : 'Fallo', 'ciudad' : 'Fallo', 'region' : ubicacion}

#Obtiene los detalles individuales
def casa_li_html_to_obj(casa_li_html): 
  #Obtiene la url de la Imagen 
  img = casa_li_html.find("img")
  try: 
    img_url = img['data-src']
  except:
    img_url = img['src']

  #Obtiene el precio
  precio = casa_li_html.find(class_="price-tag-fraction").text.replace(".","")
  #Obtiene el titulo de la publicacion
  titulo = casa_li_html.find(class_="ui-search-item__title").text
  #Obtiene la Ubicacion
  ubicacion = casa_li_html.find(class_="ui-search-item__location").text
  ubicacion = get_address(ubicacion)
  #Obtiene tama??o y/o cantidad de habitaciones
  atributos = casa_li_html.find_all(class_="ui-search-card-attributes__attribute")
  tamanio = ""
  cuartos =  ""
  if(len(atributos) > 0): 
    if ("??tiles" in atributos[0].text):
      tamanio = atributos[0].text
    else:
      cuartos = atributos[0].text
  if(len(atributos) > 1):
    cuartos = atributos[1].text
  #Obtiene el Url de la publicacion
  url = casa_li_html.find("a")["href"]
  #Devuelve el objeto
  return {"img_url" : img_url, "precio" : precio, "titulo" : titulo, "direccion" : ubicacion['direccion'], "ciudad" : ubicacion['ciudad'], "region" : ubicacion['region'], "tama??io" : tamanio, "cuartos" : cuartos, "url" : url}

#Funcion que obtiene la pagina
def get_page_url(PN):
  #Mercado libre tiene sistema de paginacion basado en la cantidad de productos en pagina
  #Estos se limitan a 48 productos, el valor PN que se entrega es dado por el for que 
  #Pasea en las paginas
  inicial_rango = 1 + 48 * (PN - 1)
  #Url Base
  base_pa_url = "https://listado.mercadolibre.cl/inmuebles/casas/"
  #El valor difencial de la url es sustituido por el paramento inical_rango
  base_pa_url = base_pa_url + "_Desde_{}_NoIndex_True".format(inicial_rango)
  return base_pa_url

def parse_y_guardar(url_pag):
  #Me da el url que quiero
  wd.get(url_pag)
  #Se obtiene el Html
  html_code = wd.page_source
  #Se crea un objeto apartir del html
  soup = BeautifulSoup(html_code, 'lxml')
  #Obtiene todos los resultados de la pagina actual
  casas_li = soup.find_all("li", class_="ui-search-layout__item")
  #Los convierte en objetos y las guarda
  for casa_li_html in casas_li:
    casa_obj = casa_li_html_to_obj(casa_li_html)
    df = pd.DataFrame({"casa_obj" :  casa_obj})
    df.to_csv('casas.csv')

#Parseador de paginas
for actual_pag in range(1, NumeroP+1):
  url_pag = get_page_url(actual_pag)
  parse_y_guardar(url_pag)

