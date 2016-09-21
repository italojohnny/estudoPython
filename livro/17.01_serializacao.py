#!/usr/python3.5
"""
ARMAZENAMENTO DE DADOS
ha muitas solucoes disponiveis de persistencia para a linguagem. Persisntencia
pode ser definida como a manutencao do estado de uma estrutura de dados entre
execucoes de uma aplicacao. A persistencia libera o desenvolvedor de escrever
codigo explicitamente para armazenar e recuperar estruturas de dados em arquivos
e ajuda a manter o foco na logica da aplicacao.

SERIALIZACAO
e a forma mais simples e direta de persistencia, e consiste em gravar em disco
uma imagen (dump) do objeto que pode ser recarregada (load) posteriormente. E
implementada de varias formas, sendo que a mais comum e por meio do modulo
chamado pickle.
exemplos de serializacao:
    * o programa tenta recuperar o dicionario setup usando o objeto do arquivo
    setup.pkl
    * se conseguir, imprime o dicionario.
    * se nao conseguir, criar uma configuracao-padrao e salva em setup.pkl.
"""

import pickle
try:
    setup = pickle.load(open('setup.pkl', 'rb'))
    print(setup)

except:
    setup = {'timeout': 10, 'server': '10.0.0.1', 'port':80}
    pickle.dump(setup, open('setup.pkl', 'wb'))
    print('arquivo nao encontrado')

"""
Na primeira execucao, ele cria o arquivo. Nas prosteriores, ele imprime o
dicionario.
Entre os modulos da biblioteca-padrao, tambem esta disponivel o modulo de
persistencia chamado shelve, que fornce uma classe de objetos persistentes
similares ao dicionario.
Existem frameworks em python de terceiros que oferecem formas de persistencia
como recursos mais avancados, como o ZODB. Todas elas armazenam dados em formas
binarias, que nao sao diretametne legiveis por seres humanos.
Para armazenar dados em forma de texto, existem modulos para python para ler e
gravar estruturas de dads em formatos json, yaml e xml

"""


