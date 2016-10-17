#!/usr/python3.5

class Time:
    def campeonato (self):
        print('Campeonato Brasileiro de Futebol')
    def nome (self):
        print('Um time de futebol')
    def tradicao (self):
        print('Um time decente sempre traz titulos para sua torcida')

class Atletico (Time):
    def nome (self): # O POLIMORFISMO ESTA EM REESCREVER O METODO HERDADO
        print('Clube Atletico Mineiro')
    def tradicao (self): # O POLIMORFISMO ESTA EM REESCREVER O METODO HERDADO
        print('Nao ganha nada desde 1971')

class Cruzeiro (Time):
    def nome (self): # O POLIMORFISMO ESTA EM REESCREVER O METODO HERDADO
        print('Cruzeiro Esporte Clube')

def main ():
    cam = Atletico()
    cru = Cruzeiro()

    print('Cam:')
    cam.nome()
    cam.campeonato()
    cam.tradicao()

    print('Cru:')
    cru.nome()
    cru.campeonato()
    cru.tradicao()

if __name__ == "__main__": main()
