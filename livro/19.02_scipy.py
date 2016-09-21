#!/usr/python3.5
"""
SCIPY
e um pacote que expande o numpy com outras funcionalidades voltadas para a area
cientifica.
Entre os modulos que fazem parte do pacote, temos:
    * linalg - funcoes de algebra linear
    * fftpack - transformada de fourier
    * integrate - funcoe de integracao
    * interpolate - funcoes de interpolacao
    * optimize - funcoes de optimizacao
    * signal - processamento de sinais
    * special - funcoes especiais (airy, bessel, etc)
"""
from numpy import arange, cos, sin

# sudo python -m pip install scipy
# duas funcoes do scipy para processamento de sinais
from scipy.signal import cspline1d, cspline1d_eval

# sudo python -m pip install matplotlib
# sudo pacman -S tk
# duas funcoes do matplotlib para gerar um grafico
from pylab import plot, show

x0 = arange(20) # X original
y0 = cos(x0) * sin(x0 /2) # Y a partir de X
dx = x0[1] -x0[0] # diferenca original
x1 = arange(-1, 21, 0.1)

# coeficientes para arranjo de 1 dimensao
cj = cspline1d(y0)

# avalia o spline para um novo conjunto de pontos
y1 = cspline1d_eval(cj, x1, dx=dx, x0=x0[0])

plot(x1, y1, '-g', x0, y0, '^y') # desenha
show() # mostra o grafico

# alem do scipy, existe tambem o scientificpython, que e outro pacote que
# implementarotinas para uso cientifico
