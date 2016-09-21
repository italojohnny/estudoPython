#!/usr/python3.5
"""
NOSQL
com a popularizacao de aplicacoes que usam grandes quantidades de dados (big
data), sistemas de banco de dados baseados em modelos nao relacionais voltaram a
chamar atencao. Dependendo da situacao, os sistemas nosql, podem ter um
desempenho melhor que os relacionais. Solucoes nosql sao baseados em estruturas
de dados tais como documentos, grafos, arvores, dicionarios, entre outras.
Entre os bancos de dados nosql mais populares esta o projeto de codigo aberto
mongodb, que e baseado em documentos no formato bson (que e bastante similar ao
json). O banco pode ser acessado em python pela biblioteca pymongo.
"""
from pymongo import MongoClient

# conecta com o mongodb
client = MongoClient('localhost', 27017)
# define o banco em uso
db = client['test']

prog_list = [
        {
            'Nome': 'Kraftwek',
            'Pais': 'Alemanha',
            'Albuns': ['Radioctivity', 'Trasn Europe Express']
        },
        {
            'Nome': 'Genesis',
            'Pais': 'Inglaterra',
            'Albuns': ['Foxtrot', 'The Nursery Crime']
        },
        {
            'Nome': 'King Crimson',
            'Pais': 'Inglaterra',
            'Albuns': ['Red', 'Discipline']
        },
        {
            'Nome': 'Yes',
            'Pais': 'Inglaterra',
            'Albuns': ['Close To The Edge', 'Fragile']
        }
]
# define a colecao a ser usada
progs = db.progs
# limpa a colecao
progs.remove({})

# insere os registros
ids = progs.insert(prog_list)
# identificadores automaticamente gerados pelo mongodb
print(ids)

# find_one() localiza o primeiro item na colecao que atenda aos prametros
print(progs.find_one())
print(progs.find_one({'Pais': 'Inglaterra'}))

# find retorna um iterado com todos os itens que atendemaos parametros
print(list(progs.find({'Pais': 'Inglaterra'})))

# a bibliote implementa as conversoes adequadas de tipos e acesso as funcoes do
# mongodb, como indexacao e agregacao

from pymongo import MongoClient, DESCENDING, ASCENDING
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client['test']
data = [
        {
            'grandeza': 'temperatura',
            'valor': 22.7,
            'data': datetime(2014, 4, 4, 12, 0, 0)
        },
        {
            'grandeza': 'temperatura',
            'valor': 56.3,
            'data': datetime(2014, 4, 4, 12, 0, 0)
        },
        {
            'grandeza': 'temperatura',
            'valor': 45.1,
            'data': datetime(2014, 4, 4, 12, 0, 0)
        },
        {
            'grandeza': 'temperatura',
            'valor': 18.9,
            'data': datetime(2014, 4, 4, 12, 0, 0)
        },
]
temp = db.temp
temp.remove({})
# criando indices
temp.create_index([('valor', DESCENDING), ('data', ASCENDING)])

# pesquisa com varios parametros
qry = temp.find({'grandeza': 'temperatura', 'valor': {'$gt': 20.0, '$lt': 50.0}})
print(qry.count(), 'itens encontrados')
print(list(qry))

# dados de data e hora podem ser tratados com os recursos normais do python,
# pois o pymongo se encarrega de fazer as conversoes necessarias
