#!/usr/python3.5
'''
script para gerar cores em hex no padrao rgb
'''
list_colors = []
salto = 1
for r in range(0, 256, salto):
    for g in range(0, 256, salto):
        for b in range(0, 256, salto):
            nome = '#'
            nome+= str(hex(r)[2:].zfill(2)).upper()
            nome+= str(hex(g)[2:].zfill(2)).upper()
            nome+= str(hex(b)[2:].zfill(2)).upper()
            list_colors.append(nome)
list_colors.append('#FFFFFF')
