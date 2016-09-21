#!/usr/python3.5
"""
THREADS
e uma linha de execucao que compartilha dua area de memoria com outras linhas,
ao contrario do processo tradicional, que tem apenas uma linha com area de
memoria propria.
O uso de threads oferece algumas vantagens em relacao aos processos
convencionais:
    * consomem menos recursos de maquina.
    * podem ser criadas e destruidas mais rapidamente
    * podem ser chaveadas mais rapidamente
    * podem se comunicar com outras threads de forma mais facil.
E comum utilizar threads para:
    * processamento paralelo, em casos como atender a varias conexoes em
    processos servidores.
    * executar operacoes de i/o assincronas; por exemplo, enquanto o usuario
    continua interagindo com a interface ao mesmo tempo que a aplicacao envia um
    documento para a impressora.
    * operacoes de i/o em paralelo.
O modulo da biblioteca-padrao threading prove classes de alto nivel de abstracao
e usa o modulo thread, que implementa as rotinas de baixo nivel e geralmente nao
e usuado diretamente.
"""
import os
import time
import threading

class Monitor (threading.Thread):
    def __init__ (self, ip):
        self.ip = ip
        self.status  = None
        threading.Thread.__init__(self)
    def run (self):
        ping = os.popen('ping -c 1 %s' % self.ip).read()
        if '0 received' in ping:
            self.status = False
        else:
            self.status = True

if __name__ == '__main__':
    monitores = []
    for i in range (1, 11):
        ip = '10.10.10.%d' % i
        monitores.append(Monitor(ip))
    for monitor in monitores:
        monitor.start()

    ping = True
    while ping:
        ping = False
        for monitor in monitores:
            if monitor.status  == None:
                ping = True
                break
        time.sleep(1)

    for monitor in monitores:
        if monitor.status:
            print("%s no ar" % monitor.ip)
        else:
            print("%s fora do ar" % monitor.ip)
"""
E importante observar que, quando o processo morre, todas as suas threads
terminam.
Esta disponvel tambem o modulo multiprocessing, que implementa classe para
criacao de processos e a comunicacao entre eles.
"""
