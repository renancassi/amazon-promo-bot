import requests
from lxml import etree


pRequest = requests.get('https://store.steampowered.com/search/?supportedlang=brazilian&specials=1&ndl=1')

while pRequest.status_code != 200:
    pRequest = requests.get('https://store.steampowered.com/search/?supportedlang=brazilian&specials=1&ndl=1')

parser = etree.HTMLParser()

htmlParsed = etree.fromstring(pRequest.content, parser)

xpathTitulo = htmlParsed.xpath('//span[@class="title"]')
teste = ''

for index,titulo in enumerate(xpathTitulo, start=1):
    xpathValorPromo = htmlParsed.xpath(f'//*[@id="search_resultsRows"]/a[{index}]/div[2]/div[4]/div[2]/text()[2]')
    xpathValor = htmlParsed.xpath(f'//*[@id="search_resultsRows"]/a[{index}]/div[2]/div[4]/div[2]/span/strike')
    print('Nome: ' + titulo.text)
    print('Valor: ' + xpathValor[0].text if xpathValor else 'Valor: Não disponível')
    print('Valor Promoção: ' + xpathValorPromo[0] if xpathValorPromo else 'Valor Promoção: Não disponível')
    print('\n')
