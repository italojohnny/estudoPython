#!/usr/python3.5
'''
GENERATOR EXPRESSION
e uma expressao que se assemelha ao list comprehension, porem funciona como um
gerador.
Usa menos recurso do que o list comprehension e equivalentes, pois os itens sao
gerados um de cada vez, apenas quando necessario, economizando principalmente
memoria.
'''

nums = range(12)

gen = (x**2 for x in nums if x%2)

print(type(gen))

for num in gen:
    print(num, end=' ')
print()
instrumentais =[
        ('king crimson', 'fracture'),
        ('metallica', 'call of ktulu'),
        ('yes', 'mood for a day'),
        ('pink floyd', 'one of this days'),
        ('rush', 'yyz')
        ]
print(sorted(faixa[-1]+' / '+faixa[0] for faixa in instrumentais if faixa[0].upper() < 'N'))
