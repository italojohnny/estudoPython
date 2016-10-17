#!/usr/python3.5
'''
1. Implementar um programa que receba um nome de arquivo e gere estatisticas
sobre o arquivo (numero de caracteres, numero de linhas e numero de palavras)
'''
import sys

def estatisticas (arquivo):
    caracteres = linhas = palavras = 0
    try:
        arquivo = open(arquivo, 'r')

    except:
        print('falha ao abrir o arquivo')
        sys.exit(1)

    for i in arquivo:
        linhas += 1
        caracteres += len(i)
        palavras += len(i.split(' '))

    return caracteres, linhas, palavras

print('caracteres: %d\nlinhas: %d\npalavras: %d\n' % estatisticas(sys.argv[1]))

