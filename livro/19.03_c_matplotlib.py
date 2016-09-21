#!/usr/python3.5
'''
existem add ons para o matplotlib que expandam a biblioteca com novas
funcionalidades, como e o caso do base basemap.
'''
# sudo pacman -S geos
# sudo pacman -S python-pyproj
# download https://sourceforge.net/projects/matplotlib/files/matplotlib-toolkits/basemap-1.0.7/basemap-1.0.7.tar.gz/download
# tar -xvf basemap-1.0.7.tar.gz
# cd basemap-1.0.7/
# export GEOS_DIR=/usr/lib/ 
# sudo python setup.py install 
from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot
from numpy import arange

# cria um mapa usando Basemap
mapa = Basemap(projection='robin', lat_0=-20, lon_0=-50, resolution='l', area_thresh=1e3)

# desenha a costa dos continentes
mapa.drawcoastlines(color='#777799')

# desenha as fronteiras
mapa.drawcountries(color='#ccccee')

# pinta os continentes
mapa.fillcontinents(color='#ddddcc')

# desenha os meridianos
mapa.drawmeridians(arange(0, 360, 30), color='#ccccee')

# desenha os paralelos
mapa.drawparallels(arange(-180, 180, 30), color='#ccccee')

# desenhaos libites do mapa
mapa.drawmapboundary()

# salva a imagem
pyplot.savefig('map1.png', dpi=150)

