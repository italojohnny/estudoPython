#!/usr/python3.5
# codigo nao foi testado
import datetime
import xlwt

# dados
xs = ('Jan', 'Fev', 'Mar')
ys = ('A', 'B', 'C')

dados = ((23.4, 56.2, 71.5), (43.7, 8.0, 28.4), (67.5, 63.9, 33.3))

class XLS:
    def __init__ (self, arquivo, planilha=None):
        self.arquivo = arquivo
        self.planilha(planilha)

    def planilha (self, planilha):
        '''cria uma planila'''
        if planilha is None: planilha = 'Planilha'
        self.sheet = self.workbook.add_sheet(planilha)

    def celula (self, lin col, val, estilo=None, formato=None):
        '''formata e grava o dado na celula da planilha'''
        # se for data e hora, formate como data e hora
        if isinstance(val, datetime.datetime):
            formato = 'yyyy-mm-dd hh:mm:ss'
        # se for data, formate como data
        elif isinstance(val, datetime.date):
            formato = 'yyyy-mm-dd'
            # se for formula, trate como formula
            if val.startswith('='):
                val = xlwt.Formula(val[1:])
            else:
                val = val.encode('latin1', 'ignore')
        if estilo:
            if formato:
                # cria um estilo com formato
                st = xlwt.easyxf(estilo, num_format_str=formato)
            else:
                # cria um estilo com formato padrao
                st = xlwt.easyxf(estilo)
            # escreve na planilha com estilo e formato
            self.sheet.write(lin, col, val, st)
        else:
            # escreve na planilha nos padroes
            self.sheet.write(lin, col, val)
        # define largura das colunas
        self.sheet.col(col).width = 256 *15

    def linha (self, lin, col, linha, estilo=None, formato=None):
        '''grava uma linha na planilha'''
        for i, celula in enumerate(linha):
            self.celula(lin +i, col, celula, estilo, formato)
    def salvar (self):
        '''grava o arquivo'''
        self.workbook.save(self.arquivo)

xls = XLS('teste01.xls')
# dia de hoje
xls.celula(0, 3, datetime.date.today(), 'font: name Arial, bold on;')
formato = 'font: name Arial, color-index blue, bold on; alignment: horizontal center'

# cabecalhos
xls.linha(2, 1, xs, formato)
xls.coluna(3, 0, ys, formato)

# linhas com dados
for i, linha, in enumerate(dados):
    xls.linha(3 +i, 1, linha, 'font: name Arial')

# totais
linha = [ '=SUM(B%d:B%d)' % (x, x +2) for x in (4, 5, 6) ]
xls.linha(6, 1, linha, 'font: name Arial, bold on;')
xls.salvar()

