#!/usr/python3.5
'''
LAMBDA
e uma funcao anonima composta apenas de expressoes. As funcoes lambda
podem ter apenas uma linha e podem ser atribuidas a uma variavel. Sao muito
usadas em programacao funcional.

lambda <lista de variaveis>: <expressoes>

funcoes lambda consomem menos recursos computacionais que as funcoes
convencionais, porem sao mais limitadas, pois apenas permitem expressoes.
'''
# amplitude de um vetor 3d
# a funcao lambda espera 3 parametros quando e evocada;
# esses tres parametros sao usados na expressao
# e retorna o resultado da expressao
# neste caso, a funcao lambda em si e armazenada em uma variavel
# para posteriormente ser usada
amp = lambda x, y, z: (x ** 2 + y ** 2 + z ** 2) ** .5

print(amp(1, 1, 1))
print(amp(3, 4, 5))

print(list(lambda x: x+1, [1,2,3,4,5,6,7,8,9]))


