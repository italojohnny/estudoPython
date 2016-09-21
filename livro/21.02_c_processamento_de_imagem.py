#!/uisr/python3.5
# criando uma imagem usando numpy
import numpy
from PIL import Image
from PIL import ImageFilter

def coords (xy, tam):
    X, Y = tam
    x = int((1. +xy[0]) * (X -1.) /2.)
    y = int((1. +xy[1]) * (Y -1.) /2.)
    return x, y

if __name__ == '__main__':
    tam = 900, 600 # dimensoes
    imag = numpy.zeros(tam[::-1] + (3,), numpy.uint8) # cria um arranjo apenas com zerros, com as dimensoes transpostas: tam[::-1] e o reverso de tam e (3,) e uma tupla para representar (r, g, b)
    imag.fill(255) # preenche de branco
    xs = numpy.arange(-1., 1., 0.00005) # dados do eixo x
    vmed = 0.6 # onda moduladora; valor mediof
    amp = 0.4 # amplitude
    fm = 2. # frequencia
    mod = vmed +amp *numpy.cos(fm *numpy.pi *xs)
    fc = 8. # frequencia da portadora
    ci = 32. # numero de curvas internas
    i = 0 # contador

    for delta_y in numpy.arange(1. /ci, 1. +1. /ci, 1. /ci):
        ys = mod *delta_y *numpy.sin(fc *numpy.pi *xs)
        xys = zip(xs, ys)

        for xy in xys:
            x, y = coords(xy, tam)[::-1]
            imag[x, y] = (250 -100 *delta_y, 150 -100 *delta_y, 50 +100 *delta_y)
            i += 1
    for x, y in zip(xs, mod):
        imag[coords((x, y), tam)[::-1]] = (0, 0, 0) # desenha as envoltorias
        imag[coords((x, -y), tam)[::-1]] = (0, 0, 0)

        imag[coords((x, 1.), tam)[::-1]] = (0, 0, 0) # bordas superior e inferior
        imag[coords((x, -1.), tam)[::-1]] = (0, 0, 0)
        i += 4

    for y in xs:
        imag[coords((1., y), tam)[::-1]] = (0, 0, 0)
        imag[coords((-1., y), tam)[::-1]] = (0, 0, 0)
        i += 2
    print(i, 'pontos calculados')
    # cria a imagem a partir do arranjo
    imagem = Image.fromarray(imag, 'RGB')
    imagem = imagem.filter(ImageFilter.SMOOTH)
    imagem.save('curvas.png', 'PNG')

"""
Oberservacoes:
    * a biblioteca trabalha com o conceito de bandas, que sao camadas que
    compoem a imagem. Cada imagem pode ter varias bandas, mas todas devem ter as
    mesmas dimensoes e a mesma profundidade.
    * O sistema de coordenadas se origina no canto superior esquerdo.
A lem do PIL, tambem e possivel usar o ImageMagick com python. Com um proposta
diferente, ImageMagick e um conjunto de utilitarios para processar imagens
raster, feito basicamente para uso por meio de linha de comando ou por meio de
linguagens de programacao.
"""
