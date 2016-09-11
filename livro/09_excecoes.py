#!/usr/python3.5
'''
excecoes
quando ocorre uma falha no programa (como uma divisao por zero, por exemplo), em
tempo de execucao, uma excecao e gerada. Se a excecao nao for tratada, ela sera
propagada por meio das chamadas de funcao ate o modulo principal do programa,
interrompendo a excecucao.

a instrucao try permite o tratamento de excecoes em python. Se ocorrer uma
excecao em um bloco marcado com try, sera possivel tratar a excecao por meio da
intrucao except. Podem existir varios blocos except para o mesmo bloco try.

Se except receber o nome da excecao, so esta sera tratada. Se nao for passada
nenhuma excecao como parametro, todas serao tratadas.
'''
import traceback

try:
    fn = input('Nome do arquivo: ').strip()
    for i, s in enumerate(open(fn)):
        print(i + 1, s, end='')
except:
    trace = traceback.format_exc()
    print('aconteceu um erro:\n', trace)
    open('trace.log', 'a').write(trace)
    raise SystemExit

# execoes podem ser atribuidas a variaveis
try:
    a, b = 1, '2'
    c = a + b

except TypeError as e:
    print('ocorreu uma excecao:', e)

'''
o modulo tracebak oferece funcoes para manipular as mensagens de erro. A funcao
format_exc retorna a saida da ultima excecao formatada em uma string.

o tratamento de excecao pode conter um bloco else, que sera executado quando nao
ocorrer nenhuma excecao, e um bloco finally sera executado de qualquer forma,
tendo ocorrido uma excecao ou nao. Novos tipo de excecao podem ser definidos por
meio de heranca a partir da classe Exception.

a instrucao with pode ser usada para substituir a combinacao try/finally em
varias situacoes. Com with, podemos definir um objeto que sera usado durante a
execucao do bloco. O objeto precisa suportar o protocolo de gerenciamento de
contexto, o que significa que ele deve ter um metodo __enter__(), que e
executado no inicio do bloco, e outro chamado __exit__(), que e evocado ao final
do bloco.
'''
import random
# cria arquivo
with open('temp2.txt', 'w') as temp:
    for y in range(5):
        for x in range(5):
            print(' %.2f' % random.random(), file=temp, end='') # escrita redirecionada para o arquivo
        print(file=temp) # escreve no arquivo

# le arquivo
with open('temp2.txt') as temp:
    for i in temp:
        print(i, end='')
#print(file=temp)
# como o arquivo foi fechado ao final do bloco, a tentativa de gravacao gera uma excecao
