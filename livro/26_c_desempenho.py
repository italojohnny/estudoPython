#!/usr/python3.5
import timeit

# lista dos quadrados de 1 a 1000
cod = '''s = []
for i in range(1, 1001):
    s.append(i ** 2)
'''
print(timeit.Timer(cod).timeit())

# com generator expression
cod = 'list(x ** 2 for x in range(1, 1001))'
print(timeit.Timer(cod).timeit())

# com list comprehension
cod = '[x ** 2 for x in range(1, 1001)]'
print(timeit.Timer(cod).timeit())
