#!/usr/python3.5
"""
O pacote inclui tambem um modulo de plotagem de graficos chamado graph
"""
# nao consegui instalar o modulo corretamente
# o codigo nao foi testado
from visual.graph import *

g1 = gcurve(color=(.8, .6, .3))
g2 = gvbars(delta=0.02, color=(.6, .4, .6))

for x in arange(0., 10.1, .1):
    g1.plot(pos=(x, 3 *sin(x) +cos(5 *x)))
    g2.plot(pos=(x, tan(x) *sin(4 *x)))

