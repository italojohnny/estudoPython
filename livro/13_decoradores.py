#!/usr/python3.5
'''
DECORADORES
(decorators) sao funcoes que sao aplicadas em outras funcoes e retornam funcoes
modificadas. Tanto podem ser usadas para criar ou alterar caracteristicas das
funcoes (que sao objetos) quanto para "envolver" as funcoes acrescentando uma
camada em torno delas com novas funcionalidades.
O caracter "@" pode ser usado para automatizar o processso de aplicacao do
decorator

    def decorator(f):
        f.decorated = True
        return f

    @decorator
    def func(arg):
        return arg

com isso, foi criado um atribuyo novo na funcao, que pode ser usado depois,
quando a funcao for executada.
E possivel validar os argumentos de uma funcao a partir das anotacoes
'''

def dumpargs (f): # O parametro em si dessa funcao é a propria funcao decorada com o @dumpargs
    def func (*args): # agora definimos uma funcao que acontecera primeiro do que a decorada com @dumpargs
        print(args)
        return f(*args)
    return func # retornando essa funcao para acontecer primeiro do que a decorada com @dumpargs

@dumpargs
def multiply (*nums):
    m = 1
    for n in nums:
        m = m * n
    return m

print(multiply(1, 2, 3))

# exemplo de decorador usando anotacoes
# funcao decoradora
def valargs (f):
    # funcao que envolvera a outra
    print(f.__annotations__)
    def func (**kargs):
        for k in f.__annotations__.keys():
            if k in kargs.keys() and f.__annotations__[k] != type(kargs[k]):
                print(k, 'recebeu', type(kargs[k]), ', mas esperava receber', f.__annotations__[k])
                raise TypeError
        # retorna o resultado da funcao original
        return f(**kargs)
    # retorna a funcao modificada
    return func

# funcao com anotacoes
@valargs
def eq2g(a: int, b: int, c: int):
    """Retorna raises para equacoes de 2º grau"""
    if a == 0: # uma reta
        return -c/b,
    else:
        d = (b**2 - 4*a*c) ** 0.5
        x1 = (-b -d) / (2 * a)
        x2 = (-b +d) / (2 * a)
        return x1, x2

# alguns testes
print(eq2g(a=0, b=2, c=-2))
print(eq2g(a=0, b='2', c=-2))
