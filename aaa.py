import nltk   
import requests
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"    
html = requests.get(url).content    
raw = nltk.clean_html(html)  
print(raw)