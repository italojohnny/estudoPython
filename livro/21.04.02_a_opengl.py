#!/usr/python3.5
"""
PYOPENGL
AS bibliotecas OpenGl implementam uma API de baixo nivel para manipulacao de
imagens 3d, permitindo o acesso aos recursos disponiveis no hardware de video,
e tambme torna o codigo independente deplataformas, pois emula por software as
funcionalidades que nao estiverem disponiveis no equipamento. Entre esses
recursos temos: primitivas (linhas e poligonos), mapeamento de texturas,
operacoes de transformacao e iluminacao.
OpenGL funciona em um contexto que tem seu estado alterado atraves das funcoes
definidas na especificacao. Este estado e mantido ate que sofra uma nova
alteracao.
Complementando a biblioteca principal, o OpenGL, Utility Library (GLU) e uma
biblioteca com funcoes de alto nivel, enquanto o OpenGL Utility Toolkit (GLUT)
define rotinas independentes de plataforma para gerenciamento de janelas,
entrada e contexto.
GLUT e orientada a eventos, aos quais e possivel se associar funcoes callback,
que executam as chamadas OpenGL. A biblioteca tem uma rotina que monitora os
eventos e evoca as funcoes quando necessario
PyOpenGL e um pacote que permite que programas em python utilizem as bibliotecas
OpenGL, GLU e GLUT
"""
# sudo pacman -S python-opengl
from sys import argv
from OpenGL.GL import *
from OpenGL.GLUT import *

def display ():
    '''funcao callback que desenha na janela'''
    # glClear limpa a janela com valores predeterminados
    # GL_COLOR_BUFFER_BIT define que o buffer aceita escrita de cores
    # GL_DEPTH_BUFFER_BIT define que o buffer de profundidade sera usado
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    rgba = [.8, .6, .4, .5]
    # glMaterial especifica os parametros do materia que serao usados no modelo de iluminacao da cena (no formato rgba)
    # GL_FRONT define que a face afetada pela funcao e a frontal
    # GL_AMBIENT especifica que o parametro e a reflexao de ambiente
    glMaterialfv(GL_FRONT, GL_AMBIENT, rgba)
    # GL_DIFFUSE especifica que o parametro e a reflexao difusa do material
    glMaterialfv(GL_FRONT, GL_DIFFUSE, rgba)
    # GL_SPECULAR especifica que o parametro e a reflexao especular
    #glMaterialfv(GL_FRONT, GL_SPECULAR, rgba)
    # GL_EMISSION especifica que o parametro e a emissao do material
    #glMaterialfv(GL_FRONT, GL_EMISSION, rgba)
    # GL_SHININESS especifica que o expoente usado pela reflexao especular
    # Desenha uma esfera solida, com raio 0.5 e 128 divisoes, na horizontal e na vertical
    glutSolidSphere(0.5, 128, 128)
    # forca a execucao dos comandos opengl
    glFlush()

#inicilaliza a biblioteca glut
glutInit(argv)

# glutInitDisplayMode configura o mdo de exibicao
# GLUT_SINGLE define o buffer como simples; (tambem pode ser duplo, com GLUT_DOUBLE)
# GLUT_RGB seleciona o modo rgb
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
# cria a janela principal
glutCreateWindow(b'Esfera')
# configura a funcao callback que desenha na janela atual
glutDisplayFunc(display)
# limpa a janela com a cor especificada
glClearColor(.25, .15, .1, 1.)
# muda a matriz corrente para GL_PROJECTION
glMatrixMode(GL_PROJECTION)
# carrega uma matriz identidade na matriz corrente
glLoadIdentity()

# configura os parametros para as fontes de luz
# GL_DIFFUSE define o parametro usado a luz difusa (no formato rgba)
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1., 1., 1., .5])

# os tres parametros definem a posicao da fonte luminosa
# o quarto define se a fonte e direcional (0) ou posicional (1)
glLightfv(GL_LIGHT0, GL_POSITION, [-5., 5., -5., 1.])

# aplica os parametros de iluminacao
glEnable(GL_LIGHTING)

# inclui a fonte de luz 0 no calculo da iluminacao
glEnable(GL_LIGHT0)

# inicia o laco de eventos da GLUT
glutMainLoop()

