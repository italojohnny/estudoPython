#!/usr/python3.5
'''
4. implementar uma funcao que receba um dicionario e retorne a soma, a media e a
variacao dos valores.
EXPLICADO MAL PRA CARALHO, SEU FILHO DA PUTA
'''

def soma_media_variacao (d):
    s = sum(d.values())
    m = s / len(d.values())
    v = max(d.values()) - min(d.values())
    return s, m, v

# teste
d = {chr(v): v for v in range(55, 70)}
print(soma_media_variacao(d))
