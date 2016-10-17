#!/usr/python3.5
'''
AGREGAÇÃO
representada na UML com um relacionamento com losango aberto

+----------+            +----------+
|  Conta   |            |  Cliente |
+----------+    tem um  +----------+
+----------+< >---------+----------+
+----------+            +----------+

Cliente não depende de uma Conta para existir; pois primeiro se cria um Cliente
e depois uma Conta, passando Cliente como parametro para essa conta; Vinculando
a este Cliente a Conta.
'''

class Cliente:
    def __init__ (self):
        self.nome = ""
        self.cpf = ""

class Conta:
    def __init__ (self, cliete):
        self.cliente = cliente
        self.numero = 0

fulano = Cliente()
contaDoFulano = Conta(fulano)
