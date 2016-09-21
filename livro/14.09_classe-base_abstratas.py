#!/usr/python3.5
"""
CLASSES-BASE ABSTRATAS
python suporta abstract base classes, que sao metaclasses que permitem forcar a
implementacao de determinados metodos e atributos das classes e subclasses
derivadas.
O modulo abc define a metaclasse ABCMeta e os decoradores abstractmethod e
abstractproperty que identificam os metodos e as propriedades que devem ser
implementadas.
"""

from abc import ABCMeta, abstractmethod

class Nave (metaclass=ABCMeta):
    @abstractmethod
    def mover (self, x0, x1, v):
        pass

class Zeppelin (Nave):
    def mover(self, x0, x1, v):
        d = x1 - x0
        t = v * d
        return t

class Hovercraft (Nave):
    pass

z = Zeppelin()
#h = Hovercraft()

"""
A avaliacao da existencia dos metodos abstratos ocorre durante o processo de
criacao de objetos a partir da classe, porem esta nao leva em conta os
parametros dos metodos.
"""
