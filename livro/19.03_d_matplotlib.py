#!/usr/python3.5
# outro exemplo
# sudo python -m pip install pillow
from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot

mapa = Basemap(projection='ortho', lat_0=10, lon_0=-10, resolution='l', area_thresh=1e3)

# preenche o mapa com relevo
mapa.bluemarble()
mapa.drawmapboundary()
lxy = (('Rio\nde\nJaneiro', -43.11, -22.54), ('Londres', 0.07, 50.30))

# transposta
lxy = list(zip(*lxy))

# converte as coordenadas
x, y = mapa(lxy[1], lxy[2])
lxy = lxy[0], x, y

# marca no mapa
mapa.plot(x, y, 'w^')

# escreve os nomes
for l, x, y in zip(*lxy):
    pyplot.text(x +2e5, y -6e5, l, color='#eeeeec')

pyplot.savefig('map2.png', dip=150)

"""
alem de modulos de terceiros, tambem e possivel usar a planilha do libreoffice
para gerar graficos com o python por meio da api chamada python-UNO bride.
"""
