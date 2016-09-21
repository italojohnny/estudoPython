#!/usr/python3.5
"""
IMAGENS EM 3D
os formatos apresentados anteriormente (matricial e vetorial) representam
imagens bidimensionais no computador de forma adequada para a maior parte das
aplicacoes. Porem eles sao limitados em alguns aspectos, principlamente para
simulacoes, pois o mundo em que vivemos tem tres dimensoes.
uma representacao computacional de uma cena 3d geralmente e composta de objetos
que representam solidos, fontes de luz e caremas. Os objetos solidos geralmente
sao representados por malhas (meshes), que sao conjuntos de pontos (vertices).
Estes possuem cordenas x, y e z. Os pontos sao interligados por linhas (arestas)
que formam as superficies (faces) dos objetos. Conjuntos de linhas que
representam as malhas sao chamados de estruturas de arame (wireframes).
Objetos podem usar um ou mais materiais, e estes podem ter varias
caracteristicas, tais como cor, transparencia e sobreamente, que e a forma como
o material reponde a iluminacao da cena. Alem disso, o material pode ter uma ou
mais texturas associadas.
Texturas sao compostas de imagens de duas dimensoes que podem ser usadas nos
materiais aplicados as superficies dos objetos, alterando varias propriedades,
tais como reflexao, transparencia e enrugamentr (bump) da superficie.
Os objetos podem ser modificados por meio de transformacoes, tais como
translacao (mover de uma posicao para outra, rotacao (girar em torno de um eixo)
e redimensionamento (mudar de tamanho em uma ou mais dimensoes).
Para rendereizar, ou seja, gerar a imagem final, e necessario fazer uma serie de
calculos complexos para aplicar iluminacao e perspectiva aos objetos da cena.
Entre os algoritmos usado para renderizacao, um dos mais conhecidos e o chamado
raytrace, no qual os raios de luz sao calculados da camera ate as fontes de luz.
Com isso, sao evitados calculos desnecessarios dos raios que nao chegam ate a
camera.
um dos usos mais populares da tecnologia 3d e a animacao. A tecnica mais comum
de animacao em 3d e chamada de keyframe. Nela, o objeto a ser animado e
posicionado em locais diferentes em momentos-chaves da animacao e o software se
encarrega de calcular as posicoes nos quadros intermediarios por meio de
interpolacao.
Muitos aplicativos 3d utilizam bibliotecas que implementam a especificacoes
OpenGL (Open Graphics Library), que define uma API independente de plataforma e
de linguagem, para a manipulacao de graficos 3d, permitindo a renderizacao em
tempo real acelerada por hardware. Sua caracteritica mais marcante e a
performance. Mesa 3d e a implementacao livre mais conhecida e esta amplamente
disponivel em distribuicoes de linux e bsd.

VPYTHON
E um pacote que permite criar e animar modelos simples em 3d. Seu objetivo e
facilitar a criacao rapida de simulacoes e protoripos que nao requerem solucoes
complexas.
Prove iluminacao, controle de camera e tratamento de evento de mouse (rotacao e
zoom) automaticamente. Os objetos podem ser criados interativamente no
interpretador, que a janela 3d do vpython e atualizada de acordo.
"""
# sudo python -m pip install vpython
# nao consegui instalar tudo. Aparentemente o projeto foi descontinuado
from visual import *
coords = (-3, 3) # coordenadas para os vertices e arestas
cor1 = (0.9, 0.9, 1.0) # cordo vertice
cor2 = (0.5, 0.5, 0.6) # cor da arestas

for x in coords: # desenha esferasnos vertices
    for y in coords:
        for z in coords:
            visual.sphere(pos=(x, y, z), color=cor1) # pos e a posicao do centro da esfera

for x in coords: # desenha cilindros das arestas
    for z in coords:
        visual.cylinder(pos=(x, 3, z), color=cor2, radius=0.25, axis=(0, -6, 0)) # pos= posicao; radius= raio; axis= eixo

    for y in coords:
        visual.cylinder(pos=(x, y, 3), color=cor2, radius=0.25, axis=(0, 0, -6))

for y in coords:
    for z in coords:
        visual.cylinder(pos=(3, z, y), color=cor2, radius=0.25, axis=(-6, 0, 0))

"""
Os objetos 3d do vpython podem ser agrupados em quadros (frames), que podem ser
movidos e rotacionados.
E possivel animar os objetos 3d usando lacos. Para controlar a velocidade da
animacao, o vpython prove a funcao rate(), que pausa a animacao pelo inverso do
argumento em segundo.
"""


