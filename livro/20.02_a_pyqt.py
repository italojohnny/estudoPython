#!/usr/python3.5
"""
PYQT
qt e um toolkit desenvolvido em C++ e e utilizado por diversos programas,
incluindo o ambiente de desktop grafico KDE e seus aplicativos. Embora o qt seja
mais usado para a criacao de aplicativos gui, ele tambem inclui bibliotecas com
outras funcionalidades, como acesso a banco de dados, comunicacao de rede e
controle de threads, entre outras. PyQt e uma binding que permite o uso do Qt no
Python, disponivel sob a lincenca GPL.
O Qt na versao 4 contem dois modulos principal, chamados QtGui, que define as
rotinas de interface, e QtCore, que define estruturas essenciais para o
funcionamento do toolkit, como, por exemplo, os sinais (eventos).
"""
# sudo pacman -S python-pyqt4 
import sys
from PyQt4 import QtGui, QtCore

class Main (QtGui.QWidget):
    '''Janela principal'''
    def __init__ (self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        # muda a geometria da janela
        self.setGeometry(200, 200, 200, 100)
        # muda o titulo
        self.setWindowTitle('Teste')

        # cria um botao
        quit = QtGui.QPushButton('Fechar', self)
        quit.setGeometry(10, 10, 60, 35)

        # conecta o sinal gerado pelo botao com a funcao que encerra o programa
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))

# cria um objeto 'aplicacao Qt', que trata os eventos
app = QtGui.QApplication(sys.argv)

# cria a janela principal
qb = Main()
qb.show()

# inicia a 'aplicacao Qt'
sys.exit(app.exec_())
