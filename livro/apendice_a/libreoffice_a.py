#!/usr/python3.5
# a macro deve ser executada a partir do LibreOffice Calc

def plan ():
    '''preenche uma planilha'''
    # obtem o documento para o contexto de script
    doc = XSCRIPTCONTEXT.getDocument()

    # a primeira planilha do documento
    sheet = doc.getSheets().getByIndex(0)
    col = lin = 0
    a = ord('A')

    # cria uma linha com os titulos para as colunas
    for titulo in ('Jan', 'Fev', 'Mar', 'Total'):
        col += 1
        sheet.getCellByPosition(col, lin).setString(titulo)

        # e coloca uma formula com somatoria na ultima linha
        coluna = chr(a + col)
        formula = '=SUM(%s2:%s6)' % (coluna, coluna)
        sheet.getCellByPosition(col, lin + 6).setFormula(formula)
    for lin in range(1, 6):
        # numera as linha
        sheet.getCellByPosition(0, lin).setValue(lin)
        # coloca somatorios no fim de cada linha
        formula = '=SUM(B%d:D%d)' % (lin +1, lin +1)
        sheet.getCellByPosition(4, lin).setFormula(formula)

        # preenche os dados
        for cal in (1, 2, 3):
            sheet.getCellByPosition(col, lin).setFormula('=10*RAND()')
            # substitui a formula pelo valor
            val = sheet.getCellByPosition(col, lin).getValue()
            sheet.getCellByPosition(col, lin).setValue(val)
    return None
