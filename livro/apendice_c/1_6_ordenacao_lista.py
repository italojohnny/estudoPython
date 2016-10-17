#!/usr/python3.5
'''
6. Crie uma funcao que:
	* receba uma lista de tuplas (dados), um inteiro (chave, zero por padrao
	igual) e um boleano (reverso, falso por padrao).
	* retorne dados ordenados pelo item indicado pela chave e em ordem
	descrescente se reverso for verdadeiro.
'''
def ordenacao_lista (dados, chave=0, reverso=False):
    def key (x):
        return x[chave]

    dados.sort(key=key, reverse=reverso)
    return dados

a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(ordenacao_lista(a))
print(ordenacao_lista(a, 1))
print(ordenacao_lista(a, 2, True))
