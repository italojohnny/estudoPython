#!/usr/python3.5

class Projetil (object):
    def __init__ (self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo

    def getv (self):
        return self.alcance/self.tempo

    def setv (self, v):
        self.tempo = self.alcance /v

    velocidade = property(getv, setv)

moab = Projetil(10000, 60)
print(moab.velocidade)

moab.velocidade = 350
print(moab.tempo)

