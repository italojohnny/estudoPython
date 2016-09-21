#!/usr/python3.5
"""
COLECOES
alem de metodos especiais para objetos escalares, existem tambem metodos
especiais para lidar com objetos que funcionam como colecoes (da mesma forma que
as listas e os dicionarios), possibilitando o acesso aos itens que fazem parte
da colecao
"""

class Mat:
    def __init__ (self):
        self.itens = []
        self.default = 0

    def __getitem__ (self, xy):
        if isinstance(xy, slice):
            x1, x2 = xy.start, xy.stop
            r = []
            for x in range(x1, x2 +1):
                r.append(self.row(x))
            return r
        else:
            i = self.index(xy)
            if i is None:
                return self.default
            return self.itens[i][-1]

    def __setitem__ (self, xy, data=0):
        i = self.index(xy)
        if not i is None:
            self.itens.pop(i)
        self.itens.append((xy, data))

    def __delitem__ (self, xy):
        i = self.index(xy)
        if i is None:
            return self.defaut
        return self.itens.pop(i)

    def index (self, xy):
        i = 0
        for item in self.itens:
            if xy == item[0]:
                return i
            i += 1
        else:
            return None

    def dim (self):
        x = y = 0
        for xy, data in self.itens:
            if xy[0] > x: x = xy[0]
            if xy[0] > y: y = xy[1]
        return x, y

    def keys (self):
        return [xy for xy, data in self.itens]

    def values (self):
        return [data for xy, data in self.itens]

    def row (self, x):
        X, Y = self.dim()
        r = []
        for y in range(1, Y +1):
            r.append(self[x, y])
        return r

    def col (self, y):
        X, Y = self.dim()
        r = []
        for x in range(1, X +1):
            r.append(self[x, y])
        return r

    def sum (self):
        return sum(self.values())

    def avg (self):
        X, Y = self.dim()
        return round(self.sum() / (X * Y), 2)

    def __repr__ (self):
        r = 'Dim: %s\n' % repr(self.dim())
        X, Y = self.dim()
        for x in range(1, X +1):
            for y in range(1, Y +1):
                r += ' %s = %3.1f' % (repr((x, y)), float(self.__getitem__((x, y))))
            r += '\n'
        return r

if __name__ == '__main__':
    mat = Mat()
    print('2 itens preenchidos:')
    mat[1, 2] = 3.14
    mat[3, 4] = 4.5
    print(mat)

    print('Troca e remocao:')
    del mat[3, 4]
    mat[1, 2] = 5.4
    print(mat)
    print('preenchendo a 3 coluna:')
    for i in range(1, 4):
        mat[i+1, 3] = i

    print(mat)
    print('3 coluna:', mat.col(3))
    print('fatia com 2 a 3 linha', mat[2:3])
    print('somatoria:', mat.sum(), 'media', mat.avg())

#A matriz esparsa cresce ou diminui conforme os indices dos elementos
