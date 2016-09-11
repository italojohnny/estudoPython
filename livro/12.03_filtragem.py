#!/usr/python3.5
'''
FILTRAGEM
uma funcao e palicada em todos os itens de uma sequencia. Se a funcao retornar
um valor que seja avaliado como verdadeiro, o item original fara parte da
sequencia resultante. Implementado pelo iterador filter()
'''
# uma funcao lambda que espera um parametro x
# esse parametro e divido pelo modulo de 2, ou seja, se a divisao por 2 por 
# igual a 0, logo o numero e par.
# a funcao lambda entao retornara o modulo da divisao por 2, que sera 0 para os 
# pares e >0 para os impares.
# deve se lembrar que 0 e considerado False e numeros >0 True, e a funcao 
# filter espera uma lista de valores e respectivos valores booleanos.
# Assim sendo filter apenas retornara os valores impares dessa range.
# que sera convertido para uma lista e depois impresso na tela.
print(list(filter(lambda x: x%2, range(1, 11))))

