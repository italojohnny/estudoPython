#!/usr/python3.5
'''
alem do sistema de arquivos, os modulos da biblioteca-padrao tambem fornecem
acesso a outros servicos providos pelos sistema operacional
'''
import os
import sys
import platform

def uid ():
    """
    uid() -> retorna a identificacao do usuario
    corrente ou None se nao for possivel identificar
    """
    us = {'Windos': 'USERNAME', 'Linux': 'USER'}
    u = us.get(platform.system())
    return os.environ.get(u)

print('usuario: ', uid())
print('plataforma: ', platform.platform())
print('diretorio atual: ', os.path.abspath(os.curdir))
exep, exef = os.path.split(sys.executable)
print('interpretador: ', exef)
print('diretorio do interpretador: ', exep)

# exemplo de execucao de processo
from subprocess import Popen, PIPE
host = '127.0.0.1'
cmd = 'ping -c 1'
if sys.platform == 'win32':
    cmd = 'ping -n 1'

lista= (cmd+' '+host).split()
py = Popen(lista, stdout=PIPE)
print(py.stdout.read())

'''
o modulo subprocess prove uma forma generica de execucao de processos, na funcao
Popen(), que permite a comunicacao com o processo por meio de pipes do sistema
operacional.
'''
