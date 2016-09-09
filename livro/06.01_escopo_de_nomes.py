#!/usr/python3.5

# O escopo de nomes em python e mantido por meio de namespaces, que sao
# dicionarios que relacionam os nomes dos objetos (referencias) e os objetos em
# si.
# Normalmente, os nomes estao definidos em dois dicionarios, que pode ser
# consultados atraves das funcoes locals() e globals(). Estes dicionarios sao
# atualizados dinamicamente em tempo de execucao.
# variaveis globais podem ser ofuscadas por variaveis locais (pois o escopo
# local e consultado antes do escopo global). Para evitar isso e preciso
# declarar a variavel como global no escopo globla.

def somalista (lista):
    """Soma listas de listas, recursivamente
    Coloca o resultado como global"""
    global soma
    for item in lista:
        if type(item) is list: # se o tipo do item for lista
            somalista(item)
        else:
            soma += item

# para acessar variaveis em escopo externo, mas nao global, ha a declaracao
# nonlocal

def calc ():
    def ad1 (temp):
        temp += 1
        return temp

    def ad2 ():
        nonlocal temp
        temp += 2
        return temp

    temp = 0

    # soma 1 a temp
    temp  = ad1(temp)

    # soma 2 a temp
    ad2()

    return temp

soma = 0
somalista([[1, 2], [3, 4, 5], 6])
print(soma)

temp = 5 #variavel global
print(calc())
print(temp)

# usar variaveis globais nao e considerado uma boa pratica de desenvolvimento,
# pois  tornam mais dificil entender o sistema, portanto e melhor evitar seu
# uso. E ofuscar variaveis tambem.
