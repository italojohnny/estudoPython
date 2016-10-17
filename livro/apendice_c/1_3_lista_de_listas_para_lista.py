#!/usr/python3.5
'''
3. Implementar uma funcao que receba uma lista de listas de comprimentos
quaisquer e retorne uma lista de uma dimensao.
'''
import cProfile
import timeit
cod1 = '''
def planifica_lista (l):
    nova_lista = []
    for i in range(0, len(l)):
        if not isinstance(l[i], list):
            nova_lista.append(l[i])
        else:
            tmp = planifica_lista(l[i])
            for j in range(0, len(tmp)):
                nova_lista.append(tmp[j])
    return nova_lista
'''
cod2 = '''
def flatten (it):
    if isinstance(it, list):
        ls = []
        for item in it:
            ls = ls + flatten(item)
        return ls
    else:
        return [it]
'''
def planifica_lista (l):
    nova_lista = []
    for i in range(0, len(l)):
        if not isinstance(l[i], list):
            nova_lista.append(l[i])
        else:
            tmp = planifica_lista(l[i])
            for j in range(0, len(tmp)):
                nova_lista.append(tmp[j])
    return nova_lista

def flatten (it):
    if isinstance(it, list):
        ls = []
        for item in it:
            ls = ls + flatten(item)
        return ls
    else:
        return [it]


# testando
l_f = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l_m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l_d = [1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]]
l_e = [[[[[[[[[1], 2], 3], 4], 5], 6], 7], 8], 9]

print(l_e)

print('-------------------------------')
print(planifica_lista(l_e))
cProfile.run('planifica_lista(l_e)')
print(timeit.Timer(cod1).timeit())


print('-------------------------------')
print(flatten(l_e))
cProfile.run('flatten(l_e)')
print(timeit.Timer(cod2).timeit())
