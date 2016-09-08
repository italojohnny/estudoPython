#!/usr/python3.5

# sintaxe
lista = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']

# percorrer lista
for i in lista: print(i)

# modificar o ultimo elemento
lista[-1] = 'ultimo'

# incluindo
lista.append('novo')

# removendo
lista.remove('quarto')

# ordenar
lista.sort()

# inverter
lista.reverse()

# imprimir numerado
for i, texto in enumerate(lista): print(i+1, '->', texto) # enumerate retorna tupla de dois elementos a cada iteracao

# imprimir a partir do segundo
print(lista[1:])

lista = ['A', 'B', 'C']
print('lista: ', lista) 
while lista:
    print('Saiu', lista.pop(0), ', faltam', len(lista))
lista += ['D', 'E', 'F']
print('lista: ', lista)
while lista:
    print('Saiu', lista.pop(0), ', faltam', len(lista))
