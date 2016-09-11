#!/usr/python3.5
"""
PROPRIEDADES
sao atributos calculados em tempo de excecucao. As propriedades sao
criadas por meio da funcao / decorador property. O uso de propriedades permite:
    * validar a entrada do atributo;
    * criar atributos apenas de leitura;
    * simplificar o uso da classe;
    * mudar de um atributo convencional para uma propriedade sem a necessidade
    de alterar as aplicacoes que utilizam a classe.
"""
#
class Projetil_a (object):
    def __init__ (self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo

    def get_velocidade (self):
        return self.alcance / self.tempo

moab = Projetil_a(alcance=1000, tempo=60)
print(moab.get_velocidade())

#
class Projetil_b (object):
    def __init__ (self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo

    @property
    def velocidade (self):
        return self.alcance / self.tempo

moab = Projetil_b(alcance=1000, tempo=60)
print(moab.velocidade)

# 
class Projetil_c (object):
    def __init__ (self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo

    def setv(self, v):
        self.tempo = self.alcance / v

    def getv(self):
        return self.alcance / self.tempo

    velocidade = property(getv, setv)
moab = Projetil_c(10000, 60)
print(moab.velocidade)

moab.velocidade = 350
print(moab.tempo)

# Propriedades sao particularmente interessantes para quem desenvolve
# bibliotecas para serem usadas por outras pessoas
