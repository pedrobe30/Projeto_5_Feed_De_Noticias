from bs4 import BeautifulSoup
import requests

url = "https://google.com"
resposta= requests.get(url)

conteudo_html = resposta.content
soup= BeautifulSoup(conteudo_html, "html.parser")
links= soup.find_all("a")

for link in links:
    print("texto: {%s}, URL: {%s}" % (link.text, link.get("href")))


import requests, bs4, os 
url= "https://www.playstation.com/pt-br/"
os.makedirs("playstation", exist_ok=True)
while not url.endswith("#"):
    print("Downloading page %s..." % url)
    res=requests.get(url)
    res.raise_for_status()
    soup= bs4.BeautifulSoup(res.text)
    print(soup)