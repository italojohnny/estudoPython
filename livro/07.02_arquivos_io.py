#!/usr/python3.5

'''
Os arquivos no python sao representados por objetos que oferecem metodos para
diversas operacoes de arquivos. Arquivos podem ser abertos para leitura
('r', que e o default), gravacao ('w') ou adicao ('a'), em modo texto ou
binario ('b').
    sys.stdin  representa a entrada padrao
    sys.stdout representa a saida padrao
    sys.stderr representa a saida de erro padrao
A entrada, a saida e o erro padrao, sao tratados pelo python como arquivos
abertos. A entrada em modo de leitura e os outros em modo de gravacao.
'''
import sys
temp = open('temp.txt', 'w') # cria um objeto do tipo file
for i in range(100):
    temp.write('%03d\n' % i) # escreve no arquivo
temp.close()                 # fecha o arquivo

temp = open('temp.txt', 'r') # abre arquivo no modo leitura
for x in temp:
    sys.stdout.write(x)
temp.close()

# A cada iteracao no segundo laco, o objeto retorna uma linha do arquivo de cada vez

import os.path
fn = input('Nome do arquivo: ').strip() # retorna a string digitada
if not os.path.exists(fn):
    print('Tente outra vez...')
    sys.exit()

for i, s in enumerate(open(fn)):
    print(i+1, s, end='')

# e possivel ler todas as linhas com o metodo readlines()>
print(open('temp.txt').readlines())

'''
Os objetos do tipo arquivo tambem contem um metodo seek(), que permite ir para
qualquer posicao no arquivo.
O modulo io implementa de forma separada as operacoes de arquivo e as rotinas
de manipulacao de texto.
'''
