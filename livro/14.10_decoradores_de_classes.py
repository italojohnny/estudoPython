#!/usr/python3.5
"""
DECORADORES DE CLASSE
Os decoradores tambem podem ser aplicados em classes
"""
# Exemplo
import time
def logger(cls):
    ''' funcao decoradora de classes'''
    class Logged(cls):
        '''classe derivada que mostra os parametros de inicializacao'''
        def __init__(self, *args, **kargs):
            print('hora:', time.asctime())
            print('classe:', repr(cls))
            print('args:', args)
            print('kargs:', kargs)
            # executa a inicializacao da classe antiga
            cls.__init__(self, *args, **kargs)
    #retorna a nova classe
    return Logged

@logger
class Musica(object):
    def __init__(self, nome, artista, album):
        self.nome = nome
        self.artista = artista
        self.album = album

m = Musica('Hand of Doom', 'Black Sabbath', album='Paranoid')

# com isso, o decorador mudou o comportamento da classe
