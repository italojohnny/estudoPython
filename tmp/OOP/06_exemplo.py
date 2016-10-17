#!/usr/python3.5

class Terrestre:
    se_move_em_terra = True
    def __init__(self, velocidade=100):
        self.velocidade = velocidade

class Aquatico:
    se_move_na_agua = True
    def __init__(self, velocidade=5):
        self.velocidade = velocidade


class Carro (Terrestre):
    rodas = 4
    def __init__(self, velocidade=120, pistoes=4):
        self.pistoes = pistoes
        Terrestre.__init__(self, velocidade)

class Barco (Aquatico):
    def __init__ (self, velocidade=6, helices=1):
        self.helices = helices
        Aquatico.__init__(self, velocidade)


class Anfibio(Carro, Barco):
    def __init__(self, velocidade_em_terra=80, velocidade_em_agua=4, pistoes=6, helices=2):
        Carro.__init__(self, velocidade_em_terra, pistoes)
        Barco.__init__(self, velocidade_em_agua, helices)

if __name__ == '__main__':
    novo_anfibio = Anfibio()
    for atr in dir(novo_anfibio):
        if not atr.startswith('__'):
            print(atr, '=', getattr(novo_anfibio, atr))
