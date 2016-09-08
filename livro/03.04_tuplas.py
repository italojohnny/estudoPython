#!/usr/python3.5

# semelhantes as listas, porem imutaveis depois de criadas
# sintaxe
tupla = ('primeiro', 'segundo', 'terceiro', 'quarto', 'quinto') # quando uma tupla tiver apenas um item: t = (a,)

# listas podem ser convertidas para tuplas
novat = tuple([1, 2, 3, 4, 5, 6])

# atribuicao multipla
a, b, c, d, e, f = novat
print(a, '+', b, '+', c, '+', d, '+', e, '+', f, '=', a+b+c+d+e+f)

a, b, *resto = novat
print(a, '+', b, '+', resto)

*resto, a, b = novat
print(resto, '+', a, '+', b)

# a vantagem de usar tuplas ao inves de listas ea economia de recurso computacional
