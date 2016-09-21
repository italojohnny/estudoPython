#!/usr/profile3.5
import cProfile

def fib1 (n):
    '''fibonacci calculado de forma recursiva'''
    if n > 1:
        return fib1(n -1) + fib1(n -2)
    else:
        return 1

def fib2 (n):
    '''fibonacci calculado por um loop'''
    if n > 1:
        fibs = {0:1, 1:1}
        for i in range(2, n +1):
            fibs[i] = fibs[i -1] + fibs[i -2]
        return fibs[n]
    else:
        return 2

if __name__ == '__main__':
    print('----------fib1---------')
    cProfile.run('fib1(30)')
    print('----------fib2---------')
    cProfile.run('fib2(30)')
