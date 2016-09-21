#!/usr/python3.5
"""
Um dos maiores atrativos do PyQt e o GUI Builder (ferramenta para a construcao
de interfaces) Qt Designer. O arquivos XML gerados pelo Qt Designer (com a
extensao .ui) podem ser convertidos em modulos Python por meio do utilitario
pyuic.
Para abrir o qt designer: designer-qt4
Para gerar o modulo Python a partir do arquivo criado no Qt Designer:
    pyuic4 20.02_b_pyqt.ui -o 20.02_b_pyqt.py
No qual dialog.ui e o arquivo de interface e dialog.py e o modulo.

"""
import sys
import time
from PyQt4 import QtCore, QtGui
# modulo gerado pelo pyuic
from dialog import Ui_Dialog

class Main (QtGui.QMainWindow):
    '''janela principal'''
    def __init__ (self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # cria um objeto a partir da interface gerada pelo pyuic
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # conecta o metodo ao botao que foi definido por meio do Qt Designer
        self.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), self.show_msg)
        self.connect(self.ui.pushButton_2, QtCore.SIGNAL('clicked()'), self.show_fechar)

    def show_msg (self):
        '''metodo que evoca a caixa de mensagem'''
        reply = QtGui.QMessageBox.question(self, 'Mensagem', 'Hora:'+time.asctime().split()[3], QtGui.QMessageBox.Ok)

    def show_fechar (self):
        print('nada de mais')
        sys.exit(0)

if __name__ == "__main__":
    print(dir(Ui_Dialog))
    app = QtGui.QApplication(sys.argv)
    myapp = Main()
    myapp.show()
    sys.exit(app.exec_())

# tambem esta disponivel um binding LGPL similar ao PyQt, chamdo PySide.
