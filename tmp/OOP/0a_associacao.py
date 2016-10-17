#!/usr/python3.5
'''
ASSOCIAÇÃO
represantada na UML por uma linha que liga duas classes

+----------+            +----------+
| Cliente  |            | Consulta |
+----------+            +----------+
+----------+------------+----------+
+----------+            +----------+

Ela é implementada por um método em uma das classes que recebe como parametro um
objeto da classe associada.
'''

class Cliente:
    def __init__ (self, nome):
        self.nome = nome

class Consulta:
    def buscar (self, cliente):
        print('buscando informcaoes do cliente %s' % cliente.nome)


fulando = Cliente('italo')
consulta = Consulta()
consulta.buscar(fulando)
