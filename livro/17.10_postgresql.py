#!/usr/python3.5
"""
POSTGRESQL
para sistemas que demandam recursos mais sofisticados do sgbd, o postgresql e a
solucao open source mais completa disponivel. O software segue a arquitetura
cliente-servidor e e distribuido sob a licenca bsd.
entre os recursos oferecidos pelo postgresql, destacam-se:
    * suporte a consultas complexas
    * tansacoes
    * controle de concorrencia multiversao
    * tipos de objetos definidos pelo usuario
    * heranca
    * views
    * stored procedures
    * triggers
    * full text search
Existem varios modulos que proveem acesso ao postgresql para o python, como o
py-postgresql e o psycopg
"""
import postgresql
# via tcp/ip
db = postgresql.open(host='localhost', database='test', user='postgres', password='q1w2e3')

# cria uma tabela
sql = '''create table tracks (
    id serial primary key,
    track varchar(100),
    band varchar(100)
)'''
db.execute(sql)

# comando de inclusao usa interpolacao
sql = db.prepare('insert into tracks value(default, $1, $2,)')

# dados
recset = [('kashmir', 'led zeppelin'), ('starless', 'king crismson')]

for rec in recset:
    sql(*rec)

# recurepa os registros
qry = db.prepare('select * from tracks')

# mostra
for rec in qry:
    print(rec)

db.close()

#===============================================================================
# exemplo psycopg
import psycopg2
# para bancos de dados locais (via unix domain sockets)
#con = pycopg2.connect(database='music'
# para tcp/ip
con = pycopg2.connect(host='localhost', database='test', user='postgres', password='q1w2e3')
cur.con.cursor()

# criar uma tabela
sql = '''create table tracks (
    id serial primary key,
    track varchar(100),
    band varchar(100)
)
'''
cur.execute(sql)
sql = 'insert into tracks values (default, %s, %s)'
recset = [
        ('siberian khatru', 'yes'),
        ("supper's read", 'genesis')
        ]
for rec in recset:
    cur.execute(sql, rec)
con.commit()

cur.execute('select * from tracks')
recset = cur.fetchall()
for rec in recset:
    print(rec)

con.close()

"""
como os modulos seguem a especificacao dbi, o codigo e praticamente igual nos
dois exemplos. O psycopg foi projetado com o objetivo de suportar aplicacoes
mais pesadas, com muitas insercoes e atualizacoes.
Tambem e possivel escrever funcoes para postgresql usando python que podem ser
utilizadas tanto em stored procedures quanto em triggers.
Existem varios projetos que apliam os recursos do postgresql, comoo o postgis,
que prove suporte a informacoes espaciais, usando em gis (geographic information
systems)
"""
