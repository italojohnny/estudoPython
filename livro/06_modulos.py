#!/usr/python3.5

# importacao absoluta
import os
print(os.name)

# importacao relativa
from os import name
print(name)

# importar tudo relativamente
from os import *
print(name)

# importar um modulo no proprio diretorio
import modulo_01
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(modulo_01.media(lista)) # o funcao tem o mesmo nome do modulo

# imprimir variaveis, objetos e metodos de um modulo
print(dir(modulo_01))

# outro exemplo
from os.path import getsize, getmtime
from time import localtime, asctime
import modulo_02
mods  = modulo_02.find('time')
for mod in mods:
    tm = asctime(localtime(getmtime(mod)))
    kb = getsize(mod) / 1024
    print('%s: (%d kbytes, %s)' % (mod, kb, tm))

# dividir programas em modulos facilita o reaproveitamenteo e a localizacao de
# falhas no codigo.
# escopo de nomes
# O escopo de nomes em python e mantido por meio de namespaces, que sao
# dicionarios que relacionam os nomes dos objetos (referencias) e os objetos em
# si.
# Normalmente, os nomes estao definidos em dois dicionarios, que pode ser
# consultados atraves das funcoes locals() e globals(). Estes dicionarios sao
# atualizados dinamicamente em tempo de execucao.
