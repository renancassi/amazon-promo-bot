import requests
from lxml import etree
from datetime import datetime, timedelta
import time
import json

while True:
    pRequest = requests.get('https://store.steampowered.com/search/?supportedlang=brazilian&specials=1&ndl=1')

    while pRequest.status_code != 200:
        pRequest = requests.get('https://store.steampowered.com/search/?supportedlang=brazilian&specials=1&ndl=1')

    parser = etree.HTMLParser()

    htmlParsed = etree.fromstring(pRequest.content, parser)

    jogos = []

    for index, titulo in enumerate(htmlParsed.xpath('//span[@class="title"]'), start=1):
        jogo = {}
        jogo['nome'] = titulo.text
        xpathValorPromo = htmlParsed.xpath(f'//*[@id="search_resultsRows"]/a[{index}]/div[2]/div[4]/div[2]/text()[2]')
        xpathValor = htmlParsed.xpath(f'//*[@id="search_resultsRows"]/a[{index}]/div[2]/div[4]/div[2]/span/strike')
        xpathUrl = htmlParsed.xpath(f'//*[@id="search_resultsRows"]/a[{index}]/@href')
        xpathPromocao = htmlParsed.xpath(f'//*[@id="search_resultsRows"]/a[{index}]/div[2]/div[4]/div[1]/span')
        jogo['valor'] = xpathValor[0].text if xpathValor else 'Não disponível'
        jogo['valor_promocao'] = f'({xpathPromocao[0].text}) ' +xpathValorPromo[0] if xpathValorPromo else 'Não disponível'
        jogo['url'] = xpathUrl[0]
        jogos.append(jogo)

        print('Nome: ' + jogo['nome'])
        print('Valor: ' + jogo['valor'])
        print('Valor Promoção: ' + jogo['valor_promocao'])
        print('\n')

    with open('jogos.json', 'w') as f:
        json.dump(jogos, f, ensure_ascii=False, indent=4)

    print('\n')
    print('--------------------------------------------------')
    next_update = datetime.now() + timedelta(hours=1)
    next_update_str = next_update.strftime('%H:%M')
    print('Horário da próxima atualização: {}'.format(next_update_str))
    print('--------------------------------------------------')
    print('\n')
    time.sleep(3600) # Espera 1 hora antes de fazer a próxima requisição
