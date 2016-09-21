#!/usr/python3.5
"""
fib.py
Implementa Fibonacci.
"""
def fib(n):
    """ Fibonacci
    Se n <= 1, fib(n) = 1
    Se n > 1, fib(n) = fib(n -1) ) + fib(n -2)

    Exemplo de uso:
    >>> fib(0)
    1
    >>> fib(1)
    1
    >>> fib(10)
    189
    >>> fib('')
    Traceback (most recent call last):
        File "/usr/lib/python3.5/doctest.py", line 1321, in __run
        compileflags, 1), test.globs)
        File "15_testes_automatizados.py", line 36, in fib
            raise TypeError
    TypeError
    """
    if not type(n) is int:
        raise TypeError
    if n > 1:
        return fib(n -1) + fib(n -2)
    else:
        return 1

