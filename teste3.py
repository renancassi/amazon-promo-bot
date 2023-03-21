import requests
from lxml import etree

paginaRequest = requests.get("https://www.amazon.com.br/s?i=stripbooks&bbn=7882388011&rh=n%3A7882388011%2Cp_n_deal_type%3A23565493011&dc&qid=1679327344&rnid=23565491011&ref=sr_pg_2")

while paginaRequest.status_code != 200:
    paginaRequest = requests.get("https://www.amazon.com.br/s?i=stripbooks&bbn=7882388011&rh=n%3A7882388011%2Cp_n_deal_type%3A23565493011&dc&qid=1679327344&rnid=23565491011&ref=sr_pg_2")    

parser = etree.HTMLParser()

htmlParsed = etree.fromstring(paginaRequest.content, parser)
    
xpathTitulo = htmlParsed.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]')
xpathDivValorPai = htmlParsed.xpath('//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1][contains(text(), "Capa Comum")]')
teste = ''
# print(type(xpathTitulo))

for titulo,valor in zip(xpathTitulo, xpathDivValorPai):
    print(titulo.text)
    print(valor.text)
    print('\n')
    teste = ''




