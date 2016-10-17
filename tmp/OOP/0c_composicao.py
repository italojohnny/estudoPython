#!/usr/python3.5
'''
COMPOSIÇÃO
representada na UML com um relacionamento com losango fechado (pintado de preto)

+----------+            +----------+
|  Conta   |            | Historico|
+----------+    tem um  +----------+
+----------+<x>---------+----------+
+----------+            +----------+

Historico depende de uma Conta para existir; pois Historico sera instânciado
com a criação de uma Conta.
'''

class Historico:
    def __init__ (self):
        self.data_abertura = ""
        self.transacoes = []

class Conta:
    def __init__ (self):
        self.cliente = ""
        self.historico = Historico()
