#!/usr/python3.5
'''
1. Implementar duas funcoes:
	* Uma que converta temperatura em graus Celsius para Fahrenheit.
	* Outra que converta temperatura em graus Fahrenheit para Celsius.
	Lembrando que: F=9C/5+32.

'''

def F_to_C (C):
    '''converte Fahrenheit para Celsius'''
    return ((C-32)/9)*5

def C_to_F (F):
    '''converte Celsius para Fahrenheit'''
    return 9*F/5+32

# testando as funcoes
for i in range(1, 100):
    print(i, 'ºC = ', C_to_F(i), 'ºF')
    print(i, 'ºF = ', F_to_C(i), 'ºC')
    print()
