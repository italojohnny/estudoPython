#!/usr/python3.5
"""
octaedro animado
"""
# nao consegui instalar os modulos corretamente
# este codigo nao foi testado
from visual import *

azul = (0.25, 0.25, 0.50)
verde = (0.25, 0.50, 0.25)

eixo = (0, 1, 0)

fr = frame(axis=eixo)
box(pos=(0, -0.5, 0), color=azul, size=(10.0, 0.5, 8.0))

box(pos=(0, -0.5, 0.4), color=azul, size=(11.0, 1.0, 1.0))
box(pos=(0, -0.5, -0.4), color=azul, size=(11.0, 1.0, 1.0))
box(pos=(5.0, -0.5, 0), color=azul, size=(1.0, 1.0, 8.0))
box(pos=(5.0, -0.5, 0), color=azul, size=(1.0, 1.0, 8.0))

py1 = pyramid(frame=fr, pos=(1, 0, 0), color=verde, axis=(1, 0, 0))
py2 = pyramid(frame=fr, pos=(1, 0, 0), color=verde, axis=(-1, 0, 0))

while True:
    if abs(fr.x) > 4.2:
        delta_x = -delta_x
    if abs(fr.z) : 3.1:
        delta_z = -delta_z
    fr.x += delta_x
    fr.z += delta_z

    fr.rotate(angle=pi /10, axis=eixo)
    rate(250)
