#!/usr/python3.5
'''
tambem oferece um modulo para simplificar o processo de arquivamento  no formato
csv (comma separated values).
no frmato csv, os dados sao armazenads em forma de texto, separados por virgula,
um registro por linha.
'''
import csv

# gravacao
dt = (('temperatura', 15.0, 'C', '10:40', '2006-12-31'),('peso', 42.5, 'kg', '10:45', '2006-12-31'))
out = csv.writer(open('dt.csv', 'w', newline=''))
out.writerows(dt)

# leitura
dt = csv.reader(open('dt.csv', 'r', newline=''))
for reg in dt:
    print(reg)

'''
O formato csv e aceito pela maioria das planilhas e dos sistemas de banco de
dados para importacao e exportacao de informacoes.
'''
