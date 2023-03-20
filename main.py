import requests
from lxml import etree

paginaRequest = requests.get("https://www.amazon.com.br/s?i=stripbooks&bbn=7882388011&rh=n%3A7882388011%2Cp_n_deal_type%3A23565493011&dc&page=1&qid=1679327344&rnid=23565491011&ref=sr_pg_2")

parser = etree.HTMLParser()

htmlParsed = etree.fromstring(paginaRequest.content, parser)

xpathDivPai = htmlParsed.xpath('//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]')


listaResultados = [f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{index}]\n' for index in range(2,18)]

for item in listaResultados:
    print(item)

