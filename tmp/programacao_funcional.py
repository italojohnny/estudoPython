#!/usr/python3.5
'''
LAMBDA
funcao anonima composta apenas de expressoes
'''
lamb_quadrado = lambda x : x**2
print(lamb_quadrado(8))

#-------------------------------------------------------------------------------
'''
MAP
aplica uma funcao a todos os elementos de uma lista, gerando uma nova lista com
os resultados.
'''
def func_quadrado (x):
    return x**2
lista = range(10)
listb = list(map(func_quadrado, lista))
print(listb)

#-------------------------------------------------------------------------------
'''
FILTER
aplica uma funcoa que retorna true ou false a todos os elementos de uma lista,
gerando uma nova lista para os valores que retornaram true na funcao.
'''
def impar (x):
    return x%2
lista = range(10)
listb = list(filter(impar, lista))
print(listb)

#-------------------------------------------------------------------------------
'''
REDUCE
aplica uma lista a uma funcao que recebe dois valores como parametros, esses
valores sao iterados nessa lista, de modo que o primeiro valor e o resultado da
iteracao anterior e o segundo valor e o proximo valor na lista, resultando em um
unico valor ao finalizar a lista.
'''
from functools import reduce
def soma (x, y):
    #print("%d + %d = %d" %(x, y, x+y)) # se ficou confuso, isso explica melhor
    return x+y
lista = range(10)
listb = reduce(soma, lista)
print(listb)

#-------------------------------------------------------------------------------
'''
ZIP (transposicao)
esta função retorna uma lista de tuplas, onde a i-ésima tupla contém o i-ésimo
elemento de cada um dos argumentos.
'''
lista = [0, 2, 4, 6, 8]
listb = [1, 3, 5, 7, 9]
listc = list(zip(lista, listb))
print(listc)

#-------------------------------------------------------------------------------
'''
LIST COMPREHENSION
uma forma equivalente as expressoes matematicas para de descrever sequencias.
s = {x² para todo x em N, x >= 20}
sintaxe:
    lista = [ <expressao> for <iterador> in <sequencia> if <condicao>]
'''
lista = [x**2 for x in range(10) if x%2]
print(lista)

#-------------------------------------------------------------------------------
'''
DICTIONARY COMPREHENSION
parecido com a list comprehension
'''
dicio = {chr(x+65):x for x in range(26)}
print(sorted(dicio.keys()), dicio.values())

#-------------------------------------------------------------------------------
