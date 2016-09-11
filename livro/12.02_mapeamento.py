#!/usr/python3.5
'''
MAPEAMENTO
consiste em aplicar uma funcao a todos os itens de uma sequencia,
gerando outra sequencia contendo os resultados e com o mesmo tamnho da
sequencia inicial. O mapeamento e implementado pelo iterador map(). Retornando
sempre um gerador.
'''
#
from math import log10
# a funcao map direciona cada elemento do range para a funcao de log10 e gera
# um obj map que e convertido para lista
print(list(map(log10, range(1, 11)))) 

# map direciona cada elemento do range para a variavel x da lambda, que por sua 
# vez, efetua a expressao definida nela, logo o objeto gerado pelo map e
# convertido para lista, e e impresso na tela
print(list(map(lambda x: x/3, range(1, 11)))) 


