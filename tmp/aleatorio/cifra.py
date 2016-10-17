#!/usr/python3.5
'''
Script para cifrar frases e textos. Respeitando a pontuação e a posição da
primeira e última letra de cada palavra, o restante da palavra é embaralhada
aleatóriamente, desacentuada e numerada.
'''
def minimizar (l):
    return [i.lower() for i in l]

def asciilizar (l):
    '''remove acentuacao e caracteres especiais'''
    import unicodedata as rms
    return [rms.normalize('NFKD', i).encode('ascii', 'ignore').decode('utf8') for i in l]

def embaralhar (l):
    ''' '''
    from random import shuffle as mix
    import re
    from operator import eq

    resultado = []
    for i in l:
        nova = ''
        if len(i) > 3: # verificar se e possivel embaralhar
            # definir inicio e fim
            inicio = 0
            while not re.search(r'[a-zA-Z]', i[inicio]) and inicio <= len(i)-1:
                inicio +=1

            final = len(i)-1
            while not re.search(r'[a-zA-Z]', i[final]) and final >= 0:
                final -=1
            indices = [x for x in range(inicio+1, final)]
            mix(indices)

            copia = indices[:]
            mix(indices)
            while any(map(eq, copia, indices)):
                mix(indices)
            if final != len(i)-1:
                print('diferente')
            nova = nova.join(i[j]for j in [inicio]+indices+[final])
            print(indices, '\t\t', i, '\t', nova)
        else:
            nova = i

        resultado.append(nova)
    return resultado


def numerar (l):
    ''' '''
    matriz = {
            'a':'4', 'b':'8', 'c':'c', 'd':'d', 'e':'3', 'f':'f', 'g':'6',
            'h':'h', 'i':'1', 'j':'j', 'k':'k', 'l':'7', 'm':'m', 'n':'n',
            'o':'0', 'p':'9', 'q':'q', 'r':'r', 's':'5', 't':'t', 'u':'u',
            'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'2',
            }
    resultado = []
    for i in l:
        nova = ''
        for j in i:
            if j in matriz:
                j = matriz[j]
            nova = nova.join(j)
        resultado.append(nova)
    return resultado




#teste
f = 'OP, É mais facio enviar um sinal de sos por codigo morse'.split(' ')
#f = 'Qual é a língua mais bonita do mundo? Você não deve saber, não mesmo!'.split(' ')
f = minimizar(f)
f = asciilizar(f)
f = embaralhar(f)
#f = numerar(f)
print(f)
