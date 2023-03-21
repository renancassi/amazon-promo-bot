import requests
from lxml import etree

paginaRequest = requests.get("https://www.amazon.com.br/s?i=stripbooks&bbn=7882388011&rh=n%3A7882388011%2Cp_n_deal_type%3A23565493011&dc&qid=1679327344&rnid=23565491011&ref=sr_pg_2")

while paginaRequest.status_code != 200:
    paginaRequest = requests.get("https://www.amazon.com.br/s?i=stripbooks&bbn=7882388011&rh=n%3A7882388011%2Cp_n_deal_type%3A23565493011&dc&qid=1679327344&rnid=23565491011&ref=sr_pg_2")    

parser = etree.HTMLParser()

htmlParsed = etree.fromstring(paginaRequest.content, parser)
    
xpathTitulo = htmlParsed.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]')
# xpathValor = htmlParsed.xpath('//span[@class="a-offscreen"]')

xpathValorSimbolo = htmlParsed.xpath('//span[@class="a-price-symbol"]/text()')
xpathValorValor = htmlParsed.xpath('//span[@class="a-price-whole"]/text()')
xpathValorDecimal = htmlParsed.xpath('//span[@class="a-price-decimal"]/text()')
xpathValorCentavos = htmlParsed.xpath('//span[@class="a-price-fraction"]/text()')
xpathValor = ''.join([xpathValorSimbolo[1], xpathValorValor[1], xpathValorDecimal[1], xpathValorCentavos[1]])



# print(type(xpathTitulo))
for titulo,valor in zip(xpathTitulo, [xpathValor]):
    print(titulo.text)
    print(valor)
    teste = ''




