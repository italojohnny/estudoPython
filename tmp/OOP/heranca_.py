#!/usr/python3.5

class Vida:
    pass

class Dominio (Vida):
    pass

class Reino (Dominio):
    pass

class Filo (Reino):
    pass

class Classe (Filo):
    pass

class Ordem (Classe):
    pass

class Familia (Ordem):
    pass

class Genero (Familia):
    pass

class Especie (Genero):
    def __init__ (self):
        print('oi')

    def teste (self):
        print('oi de novo')



def main ():
    Especie().teste()


if __name__ == '__main__': main()
