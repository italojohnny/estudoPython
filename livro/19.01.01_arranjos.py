#!/usr/python3.5
"""
PROCESSAMENTO NUMERICO
alem de recursos matematicos que fazem parte da biblioteca-padrao, o
processamento numerico pode ser feito por meio do NumPy e de outros pacotes que
foram construidos a partir dele.

NUMPY
e um pacote que inclui:
    * classe array
    * classe matrix
    * varias funcoes auxiliares

ARRANJOS
a classes array implementa um arranjo homogeneo mutavel com numero arbitrario de
elementos, semelhante a lista comum do python, porem mais poderosa.
"""
# python -m pip install numpy
import numpy

# criando arranjo
print('Arranjo criado a partir de uma lista:')
a = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(a)

print('Arranjo criado a partir de um intervalo:')
z = numpy.arange(0., 4.5, .5)
print(z)

print('Arranjo de 1s 2x3:')
y = numpy.ones((2, 3))
print(y)

print('Arranjos podem gerar novos arranjos:')
cos = numpy.round(numpy.cos(z), 1) # e uma funcao semelhante ao builtin round(), porem aceita arranjos como parametro
print(cos)

print('multiplicando cada elemento por um escalar:')
print(5 * z)

print('somando arranjos elemento por elemento:')
print(z + cos)

print('redimensionando o arranjos:')
z.shape = 3, 3
print(z)

print('arranjo tranposto:')
print(z.transpose())

print('achata o arranjo')
print(z.flatten())

print('o acesso aos elementos funciona como as listas:')
print(z[1])

print('caso especial, diferente da lista')
print(z[1, 1])

#dados sobre o arranjo
print('formato do arranjo')
print(z.shape)

print('quantidade de eixos:')
print(z.ndim)

print('tipo dos dados:')
print(z.dtype)

# ao contrario da lista, os arranjos sempre sao homogeneos, ou seja, todos os
# elementos sao do mesmo tipo
