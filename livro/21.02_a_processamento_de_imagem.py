#!/usr/python3.5
"""
PROCESSAMENTO DE IMAGEM
Pillow e uma biblioteca de processamento de imagens matriciais para python que
e um fork de um projeto mais antigo chamado PIL.
Pilow contem modulos que implementam:
    * ferramentas para cortar, redimensionar e mesclar imagens
    * algoritmos de conversao, que suportam diversos formatos.
    * filtros, tais como suavizar, borrar e detectar bordas.
    * ajustes, incluindo brilho e contrastes.
    * operacoes como paletas de cores.
    * desenho simples em 2d
    * rotinas para tratamento de imagens - equalizacao, contrastes automaticos,
    deformar, inverter e outras.
"""
# cria miniatura suavizada para cada jpeg na pasta corrente
import glob
from PIL import Image # modulo principal do PIL
from PIL import ImageFilter # modulo de filtros

# para cada arquivo jpeg
for fn in glob.glob("*.jpg"):
    f = glob.os.path.splitext(fn)[0]
    print('Processando:', fn)
    imagem = Image.open(fn)

    imagem.thumbnail((256, 256), Image.ANTIALIAS)

    imagem = imagem.filter(ImageFilter.SMOOTH)

    imagem.save(f+'_miniatura.png', 'PNG')
