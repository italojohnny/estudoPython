#!/usr/bin/python2.7
# coding: utf-8
"""
Python é uma linguagem bem genérica e fácil de ser utilizada. Qualquer usuário
pode aprender a programar em Python de uma meniera bem fácil, principalmente
porque a linguagem encapsula conceitos difíceis em implementaçõe fáceis.

Neste artigo vamos tratar da utilização de threads em Python. Threads são fluxos
de programas que excecutam em paralelo dentro de uma aplicação, isto é, uma
ramificação de uma parte da aplicação que é executada de forma independente e
escalonada independentemente do fluxo inicial da aplicação.

Imaginemos, por exemplo, uma aplicação que mede, de tempos em tempos, a condição
de determinados sensores. Supondo que cada sensor precisa ser medido com uma
frequência diferente, isto é, um a cada 30 segundos, outro a cada 45 segundos e,
por fim, um terceiro a cada 75 segundos.

Implementar isto de maneira sequencial é trabalhoso. Um jeito fácil, porém, é a
implementação de uma thread independente para a leitura do sensor a que ela está
ligada, sem se preocupar, ou mesmo saber, sobre os outros sensores.

Assim, nete caso, bastaria fazer uma classe por tipo de sensor, sendo que cada
classe seria uma thread. Para transformar uma classe em thread, são necessárias
duas modificações na classe:

    * A classe em questão estender à classe Thread do pacote threading
    * Implementar o método run(), que será chamado quando a thread iniciar

Em Python, o pacote que providencia as funcionalidades de thread é chamado
threading, e deve ser importado no começo do seu programa:

    from threading import Thread

Segue um exemplo báscio, de uma classe chamada Th que implementa Thread e o
método run(). O conteúdo do método run será executado em uma thread separada
sempre que o método start, definido na classe Thread e herdado pela classse Th
no nosso exemplo, for chamado:
"""

#from threading import Thread
#class Th(Thread):
#    def __init__ (self, num):
#        Thread.__init__(self)
#        self.num = num
#
#    def run (self):
#        print "Hello"
#        print self.num
#
#a = Th(1)
#a.start()

"""
A pesar de, no exemplo acima, o conteúdo do método run ser executado em uma
thread separada, não é possível comprovar isto apenas pela saída do programa.

Afim de comprovarmos que cada thread é executada de forma independente e
escalonada independentemente do fluxo inicial da aplicação, vamos analisar o
próximo exemplo. Nele criamos vários threads simples Th, com as do exemplo
acima, porém ao invés de simplesmente imprimirmos uma mensagem na thread ela vai
executar um número definido de vezes COUNTDOWN antes de finalizar sua execucao:
"""

from threading import Thread
import sys

COUNTDOWN = 5

class Th(Thread):
    def __init__ (self, num):
        sys.stdout.write("Making thread number %sn" % str(num))
        sys.stdout.flush()
        Thread.__init__(self)
        self.num = num
        self.countdown = COUNTDOWN

    def run (self):
        while self.countdown:
            sys.stdout.write("Thread %s (%s)n" % (str(self.num), str(self.countdown)))
