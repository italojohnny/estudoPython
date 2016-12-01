#!/usr/python3.5

from abc import ABCMeta, abstractmethod

class Nave (metaclass=ABCMeta):
    @abstractmethod
    def move (self, x0, x1, v):
        pass

class Zeppelin (Nave):
    def move (self, x0, x1, v):
        d = x1 - x0
        t = v * d
        return t

class Hovercraft (Nave):
    pass

z = Zeppelin()
h = Hovercraft()
