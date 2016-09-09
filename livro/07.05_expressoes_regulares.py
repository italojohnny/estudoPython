#!/usr/python3.5
'''
EXPRESSOES REGULARES
E uma maneira de identificar padroes em sequencias de caracteres. Em python, o
modulo re prove um analisador sintatico que permite o uso de tais expressoes. Os
padroes definidos por meio de caracteres que tem significado especial para o
analisador.

PRINCIPAIS CARACTERES:
    .   qualquer caractere, menos o de nova linha.
    ^   inicio da string
    $   fim da string
    \   caractere de escape, permite usar caracteres especiais como se fossem comuns
    []  qualquer caractere dos listados entre os colchetes
    *   zero ou mais ocorrencias da expressao anterior
    +   uma ou mais ocorrencias da expressao anterior
    ?   zero ou uma ocorrencia da expressao  anterior
    {n} n ocorrencias da expressao anterior
    |   ou logico
    ()  delimitam um grupo de expressoes
    \d  digito. Equivale a [0-9]
    \D  nao digito. Equivale [^0-9]
    \s  qualquer caractere de espacamento([ \t\n\r\f\v])
    \S  qualquer caractere que nao seja de espacamento ([^ \t\n\r\f\v])
    \w  qualquer caracter alfanumerico ou underline ([a-zA-Z0-9_]).
    \W  qualquer caracter que nao seja alfanumerico ou underline ([^a-zA-Z0-9_])
'''
import re

rex = re.compile(r'\w+')
bandas = 'Yes, Genesis & Camel'
print('bandas', '->', rex.findall(bandas))

bjork =  re.compile('[Bb]j[öo]rk')
for m in ('Björk', 'björk', 'Biork', 'Bjork', 'bjork'):
    print(m, '->', bool(bjork.match(m)))

texto = 'A próxima faixa é Stairway to Heaven'
print(texto, '->', re.sub('[Ss]tairway [Tt]o [Hh]eaven', 'The Rover', texto))

bandas = 'Tool, Porcupine Tree e NIN'
print(bandas, '->', re.split(',?\s+e?\s+', bandas))
