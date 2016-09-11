#!/usr/python3.5
"""
HERANCA SIMPLES
e um mecanismo que a orientacao a objeto prove, com objetivo de facilitar o
reaproveitamento de codigo. A ideia e que as classes sejam construidas formando
uma hierarquia.

A nova classe pode implementar novos metodos e atributos e herdar metodos e
atributos da classe antiga (que tambem pode ter herdado de classes anteriores),
porem esses metodos e atributos podem ser substituidos na nova classe.

A forma mais comum de heranca e chamada de heranca simples, na qual a nova
classe e derivada de apenas uma classe ja existente, porem e possivel criar
varias classes derivadas, criando uma hieraraquia de classes.

para localizar os metodos e atributos, a hierarquia e seguida de baico para
cima, de forma semelhante a da busca nos nemespaces local e global.
"""

class Pendrive:
    def __init__ (self, tamanho, interface='2.0'):
        self.tamanho = tamanho
        self.interface = interface

class MP3Player (Pendrive):
    def __init__ (self, tamanho, interface='2.0', turner=False):
        self.turner = turner
        Pendrive.__init__(self, tamanho, interface)

mp3 = MP3Player(1024)

print('%s\n%s\n%s' % (mp3.tamanho, mp3.interface, mp3.turner))

# a classe MP3Player herda de Pendrive o tamanho e interface
