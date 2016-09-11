#!/usr/python3.5
'''
TRANSPOSICAO
constroi uma serie de sequencias a partir de outra serie de sequencia, em que a
primeira nova sequencia contem o primeiro elemento de cada sequencia original, a
segunda nova sequencia contem o segundo elemento de sequencia original, ate que
alguma sequencia original acabe.
'''

from string import ascii_lowercase

# ascii_lowercase e uma string com o alfabeto minusculo, pode ser acessado exatamente igual a uma lista, possui 26 lestras
# range(1, 100) retorna uma lista que vai de 1 ate 99
# zip enao combina essas duas listas com os elementos nas respectivas posicoes, ate alguma dessas lista chegar no fim
# seu retorno e convertido para uma lista que contem as tuplas combinadas
print(list(zip(ascii_lowercase, range(1, 100))))

# os elementos a matriz sao transpostos
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(zip(*matriz)))

# os tres intervalos sao transposto
a = range(0, 100, 2)
b = range(0, 100, 3)
c = range(0, 100, 4)
print(list(zip(a, b, c)))

