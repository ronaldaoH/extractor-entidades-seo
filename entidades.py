import requests
import json
import re
from unicodedata import normalize
import time
from bs4 import BeautifulSoup
import re
from selenium import webdriver #connect python with webbrowser-chrome
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException     

api = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def sort_confidence(val): 
    return val[2]

def cleanMe(soup):
    for script in soup(["script", "style", "form", 'nav', 'meta', 'source']): 
        script.extract()
    return soup

options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path=r'browsers/geckodriver',  options=options)	

#GET URLS
with open("URLS.txt", 'r')  as file:
	urls = file.readlines()

#inicializando el txt final
file = open("Entidades_Output", "w")

for url in urls:
	print('[+] Extrayendo Informacion de : ' ,url.replace('\n', ''))
	driver.get(url)
	if check_exists_by_xpath(driver, "//meta[@name='description']"):
		metadesc = driver.find_element_by_xpath("//meta[@name='description']").text
		print(metadesc)
	else:
		metadesc = ""

	title = driver.find_element_by_tag_name('title').get_attribute("innerHTML")	
	texto = driver.find_element_by_tag_name('body')
	soup = BeautifulSoup(texto.get_attribute("innerHTML"), 'html.parser')
	soup = cleanMe(soup)

	lista_parrafos =  []

	lista_headings = []
	headings = soup.find_all(re.compile('^h[1-2]$'))
	for heading in headings:
		lista_headings.append(heading.getText())

	parrafos = soup.find_all('p')
	primeros_parrafos = []
	for p in parrafos:
		parrafo = p.getText().split(" ")
		if len(parrafo) > 9:
			primeros_parrafos.append(p.getText())

	primeros_parrafos_ok = primeros_parrafos[0:1]

	unificar_texto = ''
	unificar_texto = title + '. ' + metadesc + '. ' 
	for h in lista_headings:
		unificar_texto  = unificar_texto  + h
	for p in primeros_parrafos_ok:
		unificar_texto  = unificar_texto + '. ' + p
	string =  unificar_texto
	string = string.replace(" ", "%20")
	response = requests.get("https://api.dandelion.eu/datatxt/nex/v1/?lang=es&text=" + string + "&token=" + api)
	string = response.content
	string = string.decode('utf-8')
	json_object = json.loads(string)
	entidades_lista = []
	for obj in json_object['annotations']:
		entidades_lista.append([obj['label'], obj['title'], obj['confidence']])
	
	#ORDENAMOS LA LISTA
	entidades_lista.sort(key = sort_confidence,reverse = True)
	
	file.write("##### : " + url.replace('\n','') + " : #####"+ '\n')  

	for el in entidades_lista:
		print(el)
		file.write("'LABEL' - 'TITULO' - 'CONFIDENCIA'"+ '\n')
		file.write(str(el).replace("[","").replace("]","") + '\n')

file.close()
driver.close()