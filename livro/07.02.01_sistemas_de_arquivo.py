#!/usr/python3.5
'''
Os sistemas operacionais modrnos armazenam os arquivos em estruturas hierarquicas
chamadas sistemas de arquivo (file system).

varias funcionalidades relacionadas a sistemas de arquivo esta implementadas no
podulo os.path, tais como:
    os.path.basename() retorna o componente final de um caminho
    os.path.dirname()  retorna um caminho sem o componete final
    os.path.exists()   retorna True se o caminho existe ou False
    os.path.getsize()  retorna o tamanho do arquivo em bytes.

O glob e outro modulo relacionado ao sistema de arquivo:
'''
import os.path
import glob

for arq in sorted(glob.glob('*.py')):
    print(os.path.getsize(arq), '\t', arq)

'''
A funcao glob.glob() retorna uma lista com os nomes de arquivo que atendem ao
criterio passado como parametro, de forma semelhante ao comando ls disponivel
nos sistemas unix.
'''
