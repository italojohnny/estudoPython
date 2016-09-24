#!/usr/python3.5
'''
Exemplo de geracao de relatorio em PDF com o editor de texto (Writer), por meio
da Python UNO Bridge:
'''
# Para iniciar o LibreOffice como servidor:
# writer -headless
# "-accept=pip,name=py1;urp;StarOffice.ServiceManager"
import os
import uno
from com.sun.star.beans import PropertyValue

# dados...
mus = [('Artista', 'Faixa'), ('King Crimson', 'Starless'), ('Yes', 'Siberian Khatru'), ('Led Zeppellin', 'No Quarter'), ('Genesis', 'Supper\'s Ready')]

# obtem o numero e o tamano dos registros
rows = len(mus)
cols = len(mus[0])

# inicio do "boiler Plata"... Contexto de componente local
loc = uno.getComponentContext()

# para resolver urls
res = loc.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', loc)

# contexto para a url
con = res.resolve('uno:pip,name=py1;urp;StarOffice.ComponentContext')

# documento corrente
desktop = con.ServiceManager.createInstanceWithContext('con.sun.star.frame.Desktop', con)

# fim de "boiler plate"... Cria um documento novo no Writer
doc = desktop, loadComponentFromURL('private:factory/swriter', '_blank', 0, ())

# Cursor de texto
cursor = doc.Text.createTextCursor()

# muda as propriedades do Texto
cursor.setPropertyValue('CharFontName', 'Verdana')
cursor.setPropertyValue('CharHeight', 20)
cursor.setPropertyValue('CharWeight', 180)

# insere o texto no documento
doc.Text.insertString(cursor, 'Musicas favoritas\n', 0)

# cria tabela
tab = doc.createInstance('com.sun.star.text.TextTable')
tab.initialize(rows, cols)
doc.Text.insertTextContent(cursor, tab, 0)

# preenche a tabela
for row in range(rows):
    for col in range(cols):
        cel = chr(ord('A') +col) +str(row +1)
        tab.getCellByName(cel).setString(mus[row][col])

# propriedades para exportar o documento
props = []
p = PropertyValue()
p.Name = 'Overwrite'
p.Value = True # Sobrescreve o documento anterior
props.append(p)
p = PropertyValue()
p.Name = 'FilterName'
p.Value = 'write_pdf_Export' # writer para pdf
props.append(p)

# url de destino, no qual o arquivo PDF sera salvo
url = uno.systemPathFileUrl(os.path.abspath('musicas.pdf'))

# salva o documento como pdf
doc.storeToUrl(url, tuple(props))

# fecha o documento
doc.close(True)

