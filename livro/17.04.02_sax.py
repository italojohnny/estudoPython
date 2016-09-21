#!/usr/python3.5
"""
SAX (Simple API for XML)
e uma api de analise sintatica seal para xml que permite apenas leitura do
documento xml. Consome menos memoria que a DOM, porem tem menos recursos.
"""
import xml.sax
# classe proecessa a arvore xml
class Handler (xml.sax.handler.ContentHandler):
    def __init__ (self):
        xml.sax.handler.ContentHandler.__init__(self)
        self.prefixo = ''

    # e chamado quando uma nova tag e encontrada
    def startElement (self, tag, attr):
        self.prefixo += ' '
        print(self.prefixo + 'Elemento:', tag)
        for item in attr.items():
            print(self.prefixo + ' - %s: %s' % item)

    # e chamando quando texto e encontrado
    def characters (self, txt):
        if txt.strip():
            print(self.prefixo + 'txt:', txt)

    # e chamado quando o fim de uma tag e encontado
    def endElement (self, name):
        self.prefixo = self.prefixo[:-2]

parser = xml.sax.make_parser()
parser.setContentHandler(Handler())
parser.parse('caninos.xml')

# Com sax nao e necessario trazer o documento inteiro para a memoria
