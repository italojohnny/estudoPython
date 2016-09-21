#!/usr/python3.5
"""
A partir da versao 5, o vpython passou a incluir recursos que permitem cenas
mais sofsticadas: materiais prontos (como madeira, por exemplo) e controle de
opacidade.
"""
# nao consegui instalar o modulo corretamente
# este codigo nao foi testado
from visual import *
scene.forward = (-0.1, -0.1, -0.1)
scene.lights = []
scne.ambient  (.1, .1, .2)
box(material=materials.wood)
sphere(radius=.2, pos=(-1, -0.3, 1), color=(.4, .5, .4), material=materials.rough, opacity=.5)
x = 2 *(2 *(1, 0), 2 *(0, 1))
mat = materials.texture(data=x, interpolate=False, mapping='rectangular')
box(axis=(0, 1, 0), size=(4, 4, 4), pos=(0, -3, 0), material=mat)
c = (1., .9, .8)
lamp = frame(pos=(0, 1, 0))
local_light(frame=lamp, pos=(2, 1, 0), color=c)
sphere(frame=lamp, radiu=0.1, pos=(2, 1, 0), color=c, material=materials.emissive)

while True:
    lamp.rotate(axis=(0, 1, 0), angle=.1)
    rate(10)


"""
O vpython tem varias limitacoes. Ele nao prove formas de criar e/ou manipular
materiais ou texturas mais complexas, nem formas avancadas de iluminacao ou
deteccao de colisoes. Para cenas mais sofsticadas, existem outras solucoes, como
blender, que e um aplicativo de modelagem 3d que usa python como linguagem
script.
"""
