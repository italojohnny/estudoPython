#!/usr/python3.5

import datetime
import xlrd

# abre o arquivo
workbook = xlrd.open_workbook('teste01.xls', encoding_override='latin1')

# primeira planilha
sheet = workbook.sheet_by_index(0)
# percorre a parte preenchida da planilha e imprime
rows = []
for row in range(sheet.nrows):
    for col in range(sheet.row_len(row)):
        celula = sheet.cell(row, col)
        # verifica o tipo
        if celula.ctype == xlrd.XL_CELL_DATE:
            datetuple = xlrd.xldate_as_tuple(celula.value, workbook.datemode)
            if datetuple[3:] == (0, 0, 0):
                celval = datetime.date(datetuple[0], datetuple[1], datetuple[2])
            else:
                celval = datetime.date(datetuple[0], datetuple[1], datetuple[2], datetuple[3], datetuple[4], datetuple[5])
        elif celula.ctype == xlrd.XL_CELL_EMPTY:
            celval = ''
        elif celul.ctype == xlrd.XL_CELL_BOOLEAN:
            celval = bool(celula.value)
        else:
            celval = celula.value
        print('%12s' % celval, end='')
    print()

