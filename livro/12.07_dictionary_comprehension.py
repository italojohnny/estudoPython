#!/usr/python3.5
'''
DICTIONARY COMPREHENSION
e uma expressao que gera um dicionario como saida, com um estrutura simiar a
list comprehension.
Pode ser usado para evitar o consumo de processamento com listas temporarias na
criacao de dicionarios
'''

# cria um dicionario, onde a key sera o caracter representada pela  variavel a+65 (esse 65 serve para pular na tabela ascci onde comeca o alfabeto)
# e o value sera a variavel a, gerada pelo range de 0 a 25
# no comeco do dicionario e definido sua key e value, depois segue igual ao list comprehensio
alf = { chr(a+65): a for a in range(26)}
print(sorted(alf.keys()))
print(alf)
