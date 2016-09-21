#!/usr/python3.5
"""
CLIENTE WEB
o python tambem pode funcionar do lado do cliente, por meio do modulo urllib.
"""
from urllib.request import Request, urlopen

# abre a url e fornece um objeto semelhante
# a um arquivo convencional
headers = {'User-Agent': 'Mozilla/5.0 (Android 4.4; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox'}
endereco = input('digite o endereco: ')
#req = Request('http://' +endereco, headers={'User-Agent': 'Mozilla/5.0'})
req = Request('http://' +endereco, headers=headers)
url = urlopen(req)
#url = urlopen('http://ark4n.wordpress.com')

# le a pagina
#html = str(url.read(), encoding='utf8').decode('utf-8')
html = url.read().decode('utf8')
# encontra os links
found = html.find('href=', 0)

# find retorna -1 se nao encontra
while found >= 0:
    # o fim do link(quando as aspas acabam)
    end = html.find(html[found +5], found +6) +1

    # mostra o link
    print(html[found:end])

    # passa para o proximo link
    found = html.find('href=', found +1)

"""
outra soulucao cliente e o twisted web, que e parte do projeto twisted, um
framework orientado a eventos voltado para protocolos de rede, incluindo http,
ssh, irc, imap e outros.
"""
