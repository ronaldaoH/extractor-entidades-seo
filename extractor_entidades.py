import selenium
import requests
import json
import re
from unicodedata import normalize
import time
from bs4 import BeautifulSoup
import re

api = 'c703af3cf06e496aacf8143642ab2de5'
def sort_confidence(val): 
    return val[3]

def cleanMe(html):
    for script in soup(["script", "style", "form", 'nav', 'meta', 'source']): # remove all javascript and stylesheet code
        script.extract()
    return soup

url = 'https://miposicionamientoweb.es/como-crear-un-blog/'
texto = requests.get(url)
texto = texto.content
soup = BeautifulSoup(texto, 'html.parser')

#p = soup.find_all('p')
#for pp in p:
#	print(pp.getText())
time.sleep(10)
article = soup.find("articlee")
if article:
	print("tiene article")
	texto = article.find_all('p')
else:
	print("no tiene article")
	texto = soup.find("body")
	soup = cleanMe(texto)
	print("##################### SACAMOS FOOTER ##############################")
	footer = soup.find('footer')
	footer_html = footer
	print("##################### SACAMOS HEADER ##############################")
	header = soup.find('header')
	header_html = header
	a1 =  str(texto)
	a2 = str(footer_html)
	a3 = str(header_html)
	texto = a1.replace(a2, "\n").replace(a3, "\n")


texto = texto
print(texto)
time.sleep(50)
lista_parrafos =  texto.split("\n")
lista_parrafos_sin_vacio = [string for string in lista_parrafos if string != ""]

string = ''
for oracion in lista_parrafos_sin_vacio:
	string = string + oracion

print(string)

print("##################### EXTRAYENDO ENTIDADES BROW ##############################")

string = string.replace(" ", "%20")
response = requests.get("https://api.dandelion.eu/datatxt/nex/v1/?lang=es&text=" + string + "&token=" + api)
string = response.content
string = string.decode('utf-8')


json_object = json.loads(string)
#json_formatted = json.dumps(json_object, indent=2, ensure_ascii=False)
#print(json_formatted)

print("##################### EXTRAER JSON ##############################")
entidades_lista = []

for obj in json_object['annotations']:
	#print(obj['label'], obj['title'], obj['spot'], obj['confidence'] )
	entidades_lista.append([obj['label'], obj['title'], obj['spot'], obj['confidence']])

entidades_lista.sort(key = sort_confidence,reverse = True)  
print(entidades_lista) 

for el in entidades_lista:
	print(el)