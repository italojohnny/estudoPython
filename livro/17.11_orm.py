#!/usr/python3.5
"""
ORM (Object Relational Mapper)
e uma cmada que se posiciona entre o codigo com a logica da aplicacao e o modulo
DBI,  com o objetivo de reduzir as dificuldades geradas pelas diferencas entre a
representacao de objetos (da linguagem) e a representacao relacional (do banco
de dados).
Com o uso de um ORM:
    * a aplicacao se torna independente do sgbd.
    * o desenvolvedor nao precisa usar sql diretamente
    * a logica para gerenciamento das conexoes e realizada de froma transparente
    pelo orm
"""
from sqlalchemy import *
# URL => driver://username:password@host:port/database
# No SQLite
#   sqlite:// (memoria)
#   sqlite:///arquivo (arquivo em disco)
db = create_engine('sqlite:///progs.db')

# torna acessivel os metadados
metadata = MetaData(db)
# Ecoa o que SQLAlchemy esta fazendo
metada.bind.echo = True

# Tabela Prog
prog_table = Table('progs', metadata,
        Columm('prog_id', Integer, primary_key=True),
        Columm('name', String(80))
        )
# cria a tabela
prog_table.create()

# carrega a definicao da tabela
prog_table = Table('progs', metadata, autoload=True)

# insere dados
i = prog_table.insert()
i.execute({'name': 'yes'}, {'name': 'genesis'}, {'name': 'pink floyd'}, {'name': 'king crimson'})

# seleciona
s = prog_table.select()
r = s.execute()
for row in r.fetchall():
    print(row)
# alem do projetos de orms dedicados como o sqlalchemy, tambem existem orms
# integrados em frameworks maiores, como o django
