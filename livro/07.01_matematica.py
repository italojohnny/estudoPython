#!/usr/python3.5

import math  # funcoes: logaritmicas, exponenciais, trigonometriacas, hiperbolicas e conversoes angulares, etc.
import cmath # semelhante a math, mas modificado para numeros complexos

for cpx in [3j, 1.5+1j, -2-2j]:
    plr = cmath.polar(cpx)
    print('complexo: ', cpx)
    print('forma polar: ', plr, '(em radianos)')
    print('amplitude: ', abs(cpx))
    print('angulo: ', math.degrees(plr[1]), '(graus)\n')

import random
import string

print(random.choice(string.ascii_uppercase)) # escolhe uma letra 
print(random.randrange(1, 11)) # escolhe um numero de 1 a 11
print(random.random()) # escolhe um float no intervalo de 0 a 1

# Na biblioteca padrao ainda existe o modulo decimal, que define operacoes com
# numeros reais com precisao fixa

from decimal import Decimal
t = 5.
for i in range(50):
    t = t - 0.1
print('float: ', t)

t = Decimal('5.')
for i in range(50):
    t = t - Decimal('0.1')
print('decimal: ', t)

# com este modulo, e possivel reduzir a introducao de erros de arredondamento
# originados da aritmetica de ponto flutuante.
# tambem esta disponivel o modulo factions, que trata de numeros racionais

from fractions import Fraction
f1 = Fraction('-2/3')
f2 = Fraction(3, 4)
f3 = Fraction('.25')
print("Fraction('-2/3') = ", f1)
print("Fraction('3, 4') = ", f2)
print("Fraction('.25') = ", f3)

# soma
print(f1, '+', f2, '+', f1+f2)
print(f2, '+', f3, '+', f2+f3)

# As fracoes podem ser inicializadas de varias formas: como string, como um par
# de inteiros ou como um numero real. O modulo tambem tem uma funcao chamada
# gcd(), que calcula o maior divisor comum (MDC) entre dois inteiro.
