#!/usr/python3.5
'''
2. Implementar uma funcao que retorne verdadeiro se o numero for primo (falso
caso contrario). Testar de 1 a 100.
'''
def verificar_primo (n):
    '''retorna True se n e um numero primo, se nao, retorna falso'''
    if n == 1:
        return False
    for i in range(2, n):
        #print(n, '/', i, '=', n%i)
        if n % i == 0:
            return False
    return True

# testando de 1 a 100
for i in range(1, 1000):
    if verificar_primo(i):
        print(i, end=', ')
print()
