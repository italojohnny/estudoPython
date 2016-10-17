#!/usr/python3.5

import time

def logger (cls):
    class Logger (cls):
        def __init__ (self, *args, **kargs):
            print('hora:', time.asctime())
            print('classe:', repr(cls))
            print('args:', args)
            print('kargs:', kargs)

            cls.__init__(self, *args, **kargs)
    return Logger

@logger
class Musica (object):
    def __init__ (self, nome, artista, album):
        self.nome = nome
        self.artista = artista
        self.album = album

m = Musica('Hand of Doom', 'Black Sabbath', album='Paranoid')
