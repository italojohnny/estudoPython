#!/usr/python3.5


def func_01 ():
    """Doc isso e uma doc string. Sua finalidade e documentar qualquer estrutura em python """
    pass # essa palavra reservada so existe por causa da identacao forcada do pyton. Use quando nao tiver nada para escrever e nao quebrar o fluxo do codigo

def func_02 (a):
    return a * 2

def func_03 (a, b = 2):
    """Doc os argumentoss com valor default devem ficar no final da lista """
    return a + b

def func_04 (num):
    """Doc funcao fatorial recursiva """
    if num <= 1: return 1
    else: return (num * func_04(num -1))

def func_05 (n):
    """Doc funcao fatorial sem recursao """
    n = n if n > 1 else 1
    j = 1
    for i in range(1, n +1):
        j = j * i
    return j

# argumentos defaults devem vir por último
# argumentos passados sem identificadores sao recebidos pela na forma de uma lista
# argumentos passados com identificadores sao recebidos pela na forma de uma dicionario
# argumentos passados com identificadores na chamada da funcao devem vir no fim da lista de parametros

# exemplo de como receber todos os parametros
# *args - argumentos sem nome (lista)
# **kargs - argumentos com nome (dicionario)
def func_06 (*args, **kargs):
    print(args)
    print(kargs)
# no exemplo, kargs recebera os argumentos nomeados e args recebera os outros

# o interpretador tem definido uma funcao builtin, chamada sorted(), que ordena 
# sequencias. O comportamento pode ser modificado pelo argumento key, que pode
# receber uma funcao que define a chave de ordenacao
# comparando pelo ultimo elemento
def _key (x):
    return x[-1]


print('funcao que nao retorna nada: ', func_01())
print('funcao com argumento', func_02(2))
print('funcao com argumento default, omitindo um', func_03(4))
print('funcao com argumento default, passando todos', func_03(4,5))
print('funcao fatorial recursiva (7): ', func_04(7))
print('funcao fatorial recursiva (7): ', func_05(7))
func_06('peso', 10, unidade='k')

dados = [(4, 3), (5, 1), (7, 2), (9, 0)]
print('Lista: ', dados)
print('Ordenada: ', sorted(dados, key=_key))

# eval(): avalia codigo (fonte ou objeto) retornando o valor
print(eval('12. /2 +3.3'))
# com isso e possivel montar codigo para ser passado para o interpretador
# durante a execucao de um programa. Esse recurso deve ser usado com cuidado,
# pois trechos de codigomontados a partir de entradas do sistema podem abrir
# brechas de seguranca
