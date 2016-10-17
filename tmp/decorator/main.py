#!/usr/python3.5

#-------------------------------------------------------------------------------
def dumpargs (f):       #(1) funcao decorator que recebe uma funcao
    def func (*args):   #(3) funcao que sera executado antes da funcao decorada
        print(args)     #(4) imprime os parametros da funcao decorada
        return f(*args) #(5) retorna para a funcao decorada os argumentos dela
    return func         #(2) retorna a funcao (3)

@dumpargs               #(6) decora uma funcao. (3),(4),(5)
def multiply (*nums):   #(7)
    m = 1               #
    for n in nums:      #
        m = m * n       #
    return m            #

print(multiply(1, 2, 3))#

#-------------------------------------------------------------------------------
def valgars (f):
    def func (**kargs):
        for k in f.__annotations__.keys():
            if k in kargs.keys() and f.__annotations__[k] != type(kargs[k]):
                print(k, 'recebeu', type(kargs[k]), ', mas esperava receber', f.__annotations__[k])
                raise TypeError
        return f(**kargs)
    return func

@valgars
def eq2g(a: int, b: int, c: int):
    if a == 0:
        return -c/b,
    else:
        d = (b**2 - 4*a*c) **0.5
        x1 = (-b -d) / (2 * a)
        x2 = (-b +d) / (2 * a)
        return x1, x2

print(eq2g(a=0, b=2, c=-2))
print(eq2g(a=0, b='2', c=-2))
