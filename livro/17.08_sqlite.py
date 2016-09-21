#!/usr/python3.5
"""
SQLITE
na biblioteca-padra existe o modulo dbi para acessar o sqlite, que por sua vez e
uma biblioteca open source escrita em linguagem c que implementa um
interpretador sql e prove funcionalidades de banco de dados, usando arquivos,
sem a necessidade de um processo servidor separado ou de configuracao manual.
"""
import sqlite3

con = sqlite3.connect('email.db')
cur = con.cursor()

sql = '''
    create table emails (
        id integer primary key,
        nome varchar(100),
        email varchar(100)
    )
'''
cur.execute(sql)

sql = 'insert into emails values (null, ?, ?)'
recset = [('jane', 'jane@nowhere.org'), ('rock', 'rock@hardplace.com')]

for rec in recset:
    cur.execute(sql, rec)

con.commit()
cur.execute('select * from emails')
recset = cur.fetchall()

for rec in recset:
    print('%d: %s(%s)' % rec)

con.close()

"""
A vantagem mais significativa de usar o sqlite e a praticidade, principalmente
no uso em aplicativos locais para desktops, em que usar um sgbd convensional
seria desnecessario e complicado de manter.
"""
