#!/usr/python3.5
"""Cria uma imagem com varios gradientes de cores"""
from PIL import Image
from PIL import ImageDraw

# largura e altura
l, a = 512, 512

# cria uma imagem nova com fundo branco
imagem = Image.new('RGBA', (l, a), 'white')

# o objeto desenho age sobre o objeto imagem
desenho = ImageDraw.Draw(imagem)

# calcula a largura da faica de cor
faixa = l / 256

# desenha um gradiente de cor
for i in range(0, l):
    rgb = (0.25 * i / faixa, 0.5 * i / faixa, i / faixa) # calcula a cor da linha
    print(rgb)
    cor = '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

    desenho.line((0, i, l, i), fill=cor) # desenha uma linha colorida, primeiro argumento e uma tupla com as coordenadas de unici e fim da linha

for i in range(l, l // 2, -l // 10):
    area = (l - i, a - i, i, i)
    recorte = imagem.crop(area).transpose(1)
    imagem.paste(recorte, area)
imagem.save('desenho.png', 'PNG')
