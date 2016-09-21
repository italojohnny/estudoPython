#!/usr/python3.5
"""
XML (eXtensible Markup Language)
uma especificacao desenvolvida pela W3C (World Wide Web Consrtium), para uma
representacao de dados, em que o metadado e armazenado junto aos dados por meio
de marcadores (tags).
Em termos estruturais, um documento XML representa uma hierarquia formada de
elementos que podem ter ou nao atributos ou subelementeos.
Caracteristicas principais:
    * E legivel por software
    * pode ser integrada com outras linguagens
    * marcadores podem ser criados sem limitacoes
    * permite a criacao de arquivos para validacao de estrutura
E cistem varios modulos disponivel para python com suporte ao XML, inclusive na
biblioteca-padrao.
Entre as apis mais usadas, destaca-se a DOM.SAX.ElementTree.

DOM (Document Object Model)
um modelo de objeto para representacao de XML, independente de plataforma e
linguagem. O DOM foi projetado para permitir navegacao nao linear e modificacoes
arbitrarias. Por isso, o DOM exige que o documento XML esteja carregado na
memoria.
"""
import xml.dom.minidom
# cria o documento
doc = xml.dom.minidom.Document()

# para ler um documento que ja existe
#doc = xml.dom.minidom.parse('caninos.xml')

# cria os elementos
root = doc.createElement('Canino')
lobo = doc.createElement('Lobo')
raposa = doc.createElement('Raposa')
coiote = doc.createElement('Coiote')
cachorro = doc.createElement('Cachorro')

# cria os atributos
cachorro.setAttribute('nome', 'Bandit')
cachorro.setAttribute('raca', 'Labrador')
cachorro.setAttribute('cor', 'Branco')

# cria a estrutura
doc.appendChild(root)
root.appendChild(lobo)
root.appendChild(raposa)
root.appendChild(coiote)
root.appendChild(cachorro)

# para acrescentar texto ao elemento
tex = doc.createTextNode('Melhor amigo do homem...')
cachorro.appendChild(tex)

# mostra o xml formatado
print(doc.toprettyxml())

# minidom e uma implementacao do DOM mais simples que requer menos memoria
