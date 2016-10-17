#!/usr/python3.5

class Supcl1:
    '''uma classe muito simples'''
    varsup1 = 1

class Supcl2:
    '''outra classe muito simples'''
    varsup1 = 2

class Classe (Supcl1, Supcl2):
    '''isso é uma classe que herda de Supcl1 e Supcl2'''
    clsvar = []
    def __init__ (self, args):
        '''inicializador da classe'''
        self.args = args

    def __done__ (self):
        '''destrutor da classe'''
        del self.args

    def metodo (self, params):
        '''método de objeto'''
        self.args += params

    @classmethod
    def cls_metodo (cls, params):
        '''método de classe'''
        cls.clsvar = params

    @staticmethod
    def est_metodo (params):
        '''método estático'''
        return params


obj = Classe(0)
obj.metodo(-1)

Classe.cls_metodo(3)
Classe.est_metodo(4)
