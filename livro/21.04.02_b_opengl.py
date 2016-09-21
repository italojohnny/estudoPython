#!/usr/python3.5
"""
a biblioteca tambem oferece rotinas para fazer transformacoes, o que permite
animar os objetos da cena.
"""
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ar = 0. # angulo de rotacao do objeto
dr = 1. # variacao da rotacao

def resize (x, y):
    '''funcao callback que e evocada quando a janela muda de tamanho'''
    glViewport(0, 0, x, y) # limpa a vista
    glMatrixMode(GL_PROJECTION) # seleciona a matriz de projecao
    glLoadIdentity() # limpa a matriz de projecao
    gluPerspective(45., float(x) /float(y), 0.1, 100.0) # calcula o aspecto da perspectiva
    glMatrixMode(GL_MODELVIEW) # seleciona a matriz de visualizacao

def draw ():
    '''funcao que desenha os objetos'''
    global ar, dr
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # limpa a janela e o buffer de profundidade
    glLoadIdentity() # limpa a matriz de visualizacao
    glTranslatef(-0.5, -0.5, -4.) # move o objeto (translacao) x, y e z (deslocamento)
    glRotatef(ar, 1.0, 1.0, 1.0) # rotacao (em graus) grau, x, y e z (eixos)
    glScalef(ar/1000, ar/1000, ar/1000) # escala x, y e z

    for i in range(0, 360, 10):
        glRotatef(10, 1.0, 1.0, 1.0)
        glBegin(GL_QUADS) # inicia a criacao de uma face retangular
        glColor3f(.7, .5, .1) # define a cor que sera usada para desenhar
        glVertex3f(0., 0., 0.) # cria vertice da face
        glColor3f(.7, .3, .1)
        glVertex3f(1., 0., 0,)
        glColor3f(.5, .1, .1)
        glVertex3f(1., 1., 0.)
        glColor3f(.7, .3, .1)
        glVertex3f(0., 1., 0.)
        glEnd() # encerra a criacao de uma face retangular

    if ar > 1000: dr = 1 # inverte a variacao
    if ar < 1: dr = 1
    ar = ar +dr

    glutSwapBuffers() # troca o buffer, exibindo o que acabou de ser usado

def keyboard (*args):
    '''funcao callback para tratar eventos de teclado'''
    if args[0] == '\27': raise SystemExit # testa se a tecla ESC foi pressionada

if __name__ == '__main__':
    glutInit(argv) # inicializa a glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) # seleciona o modo de exibicao
    glutInitWindowSize(640, 480) # configura a resolucao da janela do glut
    window = glutCreateWindow(b'Transforms') # cira a janela do glut
    glutDisplayFunc(draw) # configura a funcao callback que desenha a janela atula
    # para exibir em tela cheia
    #glutFullScreen()
    glutIdleFunc(draw) # registra a funcao para tratar redesenhar a janela quando nao ha mada a fazer
    glutReshapeFunc(resize) # registra a funcao para redesenhar a janela quando ela for redimensionada
    glutKeyboardFunc(keyboard) # registra a funcao para tratar eventos do teclado
    glClearColor(0., 0., 0., 0.) # limpa a imagem (fundo preto)
    glClearDepth(1.) # limpa o buffer de profundidade
    glDepthFunc(GL_LESS) # configura o tipo de teste de profundidade
    glEnable(GL_DEPTH_TEST) # ativa o teste de profundidade
    glShadeModel(GL_SMOOTH) # configura o sobreamento suave
    glMatrixMode(GL_PROJECTION) # seleciona a matriz de projecao
    glLoadIdentity()
    gluPerspective(45., 640. /480., .1, 100.)
    glMatrixMode(GL_MODELVIEW) # seleciona a matriz de visualizacao
    glutMainLoop() # inicia o laco de eventos glut

"""
OpenGL pode ser integrada com toolkits graficos, como QTt, em vez de usa a glut,
e como isso ser incorporada em aplicacoes GUI convencionais
"""

