#!/usr/python3.5
"""
MATRIZES
a classe matrix implementa operacoes de matrizes.
"""
import numpy

print('criando uma matriz a partir de uma lista:')
l = [[3, 4, 5], [6, 7, 8], [9, 0, 1]]
z = numpy.matrix(l)

print(z)

print('transposta da matriz:')
print(z.T)

print('inversa da matriz:')
print(z.I)

# criando outra matriz
r = numpy.matrix([[3, 2, 1]])

print('multiplicando matrizes:')
print(r * z)

print('resolvendo um sistem linear:')
print(numpy.linalg.solve(z, numpy.array([0, 1, 2])))

# o modulo numpy.linalg tambem implementa funcoes de decomposicao de matrizes:
from numpy import *
# matriz 3x3
a = array([(9, 4, 2), (5, 3, 1), (2, 0, 7)])
print('matriz a:')
print(a)

# decomponso usando QR
q, r = linalg.qr(a)
# resultados
print('matriz q:')
print(q)
print('matriz r:')
print(r)
# produto
print('q . r:')
print(int0(dot(q, r)))

# o numpy serve de base para diversos outros projetos de codigo aberto, como o
# matploib e o scipy, que complementam o numpy de varias formas
