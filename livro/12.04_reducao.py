#!/usr/python3.5
'''
REDUCAO
significa aplicar uma funcao que recebe dois parametros, nos dois primeiros
elementos de uma sequencia, aplicar noamente a funcao usando como parametros o
resultado do primeiro par e o terceiro elemento, seguindo assim ate o final da
sequencia. O resultado final da reducao e apenas um elemento.
'''
from functools import reduce
print(reduce(lambda x, y: x + y, range(10)))
# range(10) equivale a uma lista de 0 ate 9
# x + y  = x+y
# 0 + 0  = 0 (na primeira vez, o mesmo valor e passado para as duas variaveis de lambda
# 1 + 0  = 1 (na segunda vez em diante, o resultado anterior e o novo valor e passado para lambda)
# 2 + 1  = 3 (...e assim segue sucessivamente ate o final da sequencia)
# 3 + 3  = 6
# 4 + 6  = 10
# 5 + 10 = 15
# 6 + 15 = 21
# 7 + 21 = 28
# 8 + 28 = 36
# 9 + 36 = 45 (por fim, 45 sera o resultado final retornado)

# semelhantemente existe a funcao sum, mas ela so funciona para numeros
print(sum(range(10)))

# por curiosidade, com reduce() pode se calcular fatorial
# porem, o modulo math ja traz funcao pronta para isso
def fatorial (n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print (fatorial(6))
