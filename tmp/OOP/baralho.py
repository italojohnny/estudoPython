#!/usr/python3.5

class Carta:
    def __init__ (self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__ (self):
        return '<%s de %s>'%(self.valor, self.naipe)


class Baralho:
    naipes = 'paus copas espadas ouro'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__ (self):
        self.cartas = [Carta(n, v) for v in self.valores for n in self.naipes]

    def __len__ (self):
        return len(self.cartas)

    def __getitem__ (self, pos):
        return self.cartas[pos]


b = Baralho()
print(len(b))
print(b[0], b[1], b[2])

for carta in reversed(b):
    print(carta)
