#!/usr/python3.5
"""
HERANCA MULTIPLA
a nova deriva de duas ou mais classes ja existentes.
"""

class Terrestre:
    def __init__ (self, velocidade=100):
        self.velocidade_em_terra = velocidade

class Aquatico:
    def __init__ (self, velocidade=5):
        self.velocidade_em_agua = velocidade

class Carro (Terrestre):
    rodas = 4
    def __init__ (self, velocidade=120, pistoens=4):
        self.pistoens = pistoens
        Terrestre.__init__(self, velocidade=velocidade)

class Barco (Aquatico):
    def __init__ (self, velocidade, helices=1):
        self.helices = helices
        Aquatico.__init__(self, velocidade=velocidade)

class Anfibio (Terrestre, Aquatico):
    def __init__ (self, velocidade_em_terra=80, velocidade_em_agua=4, pistoens=6, helices=2):
        Carro.__init__(self, velocidade=velocidade_em_terra, pistoens=pistoens)
        Barco.__init__(self, velocidade=velocidade_em_agua, helices=helices)

novo_anfibio=Anfibio()
for atr in dir(novo_anfibio):
    if not atr.startswith('__'):
        print(atr, '=', getattr(novo_anfibio, atr))

"""
A diferenca mais significativa em relacao a heranca simples e a ordem de
resolucao de metodos (em ingles, method resolution order - MRO).
A resolucao e feita a partir da esquerda, descendo ate encontrar a classe em
comum entre os caminhos dentro da hierarquia. Quando e encontrada uma classe em
comum a procura passa para o caminho a direita. Ao esgotar os caminhos, o
algoritmo prossegue para a classe em comum e repete o processo.
A heranca multipla e um recurso que gera muita controversia, pois seu uso pode
tornar o projeto confuso e obscuro.
"""
