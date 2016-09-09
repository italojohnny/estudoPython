#!/usr/python3.5
'''
python contem dois modulos para lidar com tempo:
    time     - implementa funcoes que permitem utilizar o tempo ferado pelo sistema
    datetime - implementa tipos de alto nivel para realizar operacoes de data e hora
'''

import time

print(time.localtime())
print(time.asctime())

ts1 = time.time() # retorna tempo do sistema em segundos
tt1 = time.gmtime(ts1) # converte segundos para struct_time
print(ts1, '->', tt1)

tt2 = time.gmtime(ts1 * 3600.) # soma uma hora
ts2 = time.mktime(tt2) # converte struct_time para segundos
print(ts2, '->', tt2)

print('o programa levo', time.clock(), 'segundos ate agora...') # retorna tempo desde que o programa iniciou em segundos

for i in range(5):
    time.sleep(1)
    print(i+1, 'segundo(s)')

'''
em datetime, estao definidos quatro tipos para representar o tempo:
    datetime  - data e hora
    date      - apenas data
    time      - apenas hora
    timedelta - diferenca entre tempos
'''

import datetime
# datetime() recebe (ano, mes, dia, hora, minuto, segundo) e retorna obj datetime
dt = datetime.datetime(2020, 12, 31, 23, 59, 59)
data = dt.date()
hora = dt.time()

dd  = dt - dt.today()

print('data:', data)
print('hora:', hora)
print('quanto tempo falta para 31/12/2020', str(dd).replace('days', 'dias'))

# os objs dos tipos date e datetime retornam datas em formato ISO

