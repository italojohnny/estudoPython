#!/usr/python3.5
"""
MYSQL
e um sgbd cliente-servidor reconhecido pelo bom desempenho e e bastante usado
como backend para aplicacoes web.
"""
import pymysql

con = pymysql.connect(db='teste', user='root', passwd='')
cur = con.cursor()

cur.exeecute('show databases')
recordset = cur.fetchal()

for record in recordset:
    print(record)

con.close()

# o resultado e composto de uma lista de tuplas com as databases disponiveis
# no servidor
