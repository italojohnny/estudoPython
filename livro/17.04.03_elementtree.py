#!/usr/python3.5
"""
ELEMENTTREE
o mais pythonico dos tres, representa uma estrutura xml como uma arvore de
elementos que sao tratados de forma semelhante as listas e nos quais os
atributos sao chaves, similares aos dicionarios.
"""
from xml.etree.ElementTree import Element, ElementTree

# geracao de xml
root = Element('canino')
lobo = Element('lobo')
raposa = Element('raposa')
coiote = Element('coiote')
cachorro = Element('cachorro', nome='bandit', raca='labrador', cor='branco')

root.append(lobo)
root.append(raposa)
lobo.append(coiote)
lobo.append(cachorro)

ElementTree(root).write('caninos2.xml')

# leitura de xml
tree = ElementTree(file='caninos2.xml')
root = tree.getroot()

# lista os elementos
print(root.getchildren())

# encontra o lobo
lobo = root.find('lobo')

# encontra o cachorro
cachorro = lobo.find('cachorro')
print(cachorro.tag, cachorro.attrib)

# remove a raposa
root.remove(root.find('raposa'))
print(root.getchildren())

# o xml e muito util por facilitar a interoperabilidade entre sistemas, mesmo
# que estes sejam desenvolvidos em tecnologia diferentes.
