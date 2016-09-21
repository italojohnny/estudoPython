#!/usr/python3.5
"""
FIREBIRD
e um sgbd client-servidor leve, porem com muitos recursos. Programas em python
podem ser comunicar com ele por meio do driver dbi apropriado
"""
import firebirdsql
#para criar a base
# isql -u sysdba -p masterkey
# create database '/tmp/cds.fdb';

# conecta o firebird
con = firebirdsql.connect(dsn='localhost:/tmp/cds.fdb', user='sysdba', password='masterkey')

# cira um objeto cursos
cur = con.cursor()
sql = '''create table cds (
    nome varchar(20),
    artista varchar(20),
    ano integer,
    faixas integer,
    primary key(nome, artista, ano)
);
'''
# cria uma tabela
cur.execute(sql)

# grava as modificacoes
con.commit()

dados = [
            ('iv', 'led zeppelin', 1971, 8),
            ('zenyatta mondatta', 'the police', 1980, 11),
            ('ok computer', 'radiohead', 1997, 12),
            ('in absentia', 'porcupine tree', 2002, 12),
        ]
# insere os registros e faz a interpolacao
insert = 'insert into cds (nome, artista, ano, faixas) values (?, ?, ?, ?)'
cur.executemany(insert, dados)
con.commit()

# recupera os resultados
cur.execute('select * from cds orderby ano')
for reg in cur.fetchall():
    print(' - '.join(str(i) for i in reg))

"""
como o firebird nao requer muita potencia e nem muito esforco para
administracao, ele pode ser usado tanto como servidor quanto ser empacotado
junto a um aplicativo desktop.
"""
