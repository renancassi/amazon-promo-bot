import requests
from lxml import etree


paginaRequest = requests.get('https://www.submarino.com.br/landingpage/trd-romance?chave=trd-hi-at-generos-livros-blackfriday-romance')


while paginaRequest.status_code != 200:
    paginaRequest = requests.get('https://www.submarino.com.br/landingpage/trd-romance?chave=trd-hi-at-generos-livros-blackfriday-romance')
    
parser = etree.HTMLParser()

htmlParsed = etree.fromstring(paginaRequest.content, parser)

xpathTitulo = htmlParsed.xpath('//span[@class="product-name__Name-sc-13u5qjg-0 euRmnG"]')
teste = ''

for index,titulo in enumerate(xpathTitulo, start=1):
    xpathValor = htmlParsed.xpath(f'//*[@id="rsyswpsdk"]/div/section/div/div[2]/div[2]/div[2]/div[{index}]/div/div/a/div[3]/span[1]')
    print('Nome: ' + titulo.text)
    print('Valor: ' + xpathValor[0].text if xpathValor else 'Valor: Não disponível')
    print('\n')
    teste = ''