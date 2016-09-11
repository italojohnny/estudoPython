#!/usr/python3.5
'''
LIST COMPREHENSION
e uma construcao que equivale a uma notacao matematica na forma
$S = \{x^2\ \forall\  x\  \text{em}\ \mathbb{N}\ \text{,}\ x\ \geq 20\}$ 
ou seja, S e o conjunto formado por x ao quadrado para todo x no conjunto dos
numeros naturais, se x for maior igual a 20.

lista = [<expressao> for <referencia> in <sequencia> if <condicao>]


List Comprehension e mais eficiente do que usar as funcoes map() e filter(),
tanto em termos de uso de processador quanto em consumo de memoria
'''

lista = [x**2 for x in range(100) if x >= 20]
print(lista)

nomes = ['iTaLo', 'jOhnNy', 'dOs', 'aNjOs']
print([n[0].upper()+n[1:].lower() for n in nomes if len(n) > 3])


print([x if not x%2 else None for x in range(100) if x > 50])
