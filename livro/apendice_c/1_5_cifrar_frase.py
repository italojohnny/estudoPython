#!/usr/python3.5
'''
5. Escrever uma funcao que:
	* receba uma frase como parametro
	* retorne uma nova frase com cada palavra com as letras invertidas.
'''
def reverse1(t):
    r = t.split()
    for i in range(len(r)):
        r[i] = r[i][::-1]
    return ' '.join(r)

def reverse2(t):
    return ' '.join(s[::-1] for s in t.split())

f = 'The quick brown fox jumps over the lazy dog'
print(reverse1(f))
print(reverse2(f))
