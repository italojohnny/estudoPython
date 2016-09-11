#!/usr/python3.5
'''
geradores
as funcoes geralmente seguem o fluxo convencional de processamento, retorna
valores e encerra. Geradores funcionam de forma semelhante, porem lembram o
estado do processamento entre as chamadas, permanecendo em memoria e teroando o
proximo item esperando quando ativados. Os geradores apresentam varias vantagens
em relacao as funcoes convencionais:
    * lazy evaluation - geradores so sao processados quanso e realmente
    necessario, sendo assim, economizam recursos de processsamento.
    * reduzam a necessidade da criacao de listas.
    * permitem trabalhar coom sequencias ilimitadas de elementos.
geradores geralmente sao evocados por meio de um laco for. A sintaxe e
semelhante a da funcao tradicional, so que a instrucao yield substitui o return.
A cada nova iteracao, yield retorna o proximo valor.
'''

def gen_pares ():
    """
    gera numeros pares infinitamente...
    """
    i = 0
    while True:
        i += 2
        yield i

for n in gen_pares():
    print(n)
    if n >= 300000: break

# outro exemplo
import os

def find (path='.'):
    try:
        listdir = os.listdir(path)
    except PermissionError:
        listdir = []
    for item in listdir:
        fn =  os.path.normpath(os.path.join(path, item))
        if os.path.isdir(fn):
            for f in find(fn):
                yield f
        else:
            yield fn

for fn in find():
    print(fn)

'''
existem varios geradores que fazem parte da propria linguagem, como o built-in
range(). Alem disso, no modulo itertools, estao definidos varios geradores
uteis.
Para converter a saida do gerador em uma lista:
    lista = list(gerador())
assim, todos os itens serao gerados de uma vez.
um gerador pode delegar a geracao dos itens a outros geradores por meio do
comando yield from
'''

from time import time

def gen_a ():
    for x in range(0, 100, 1): yield x
    for x in range(0, 1000, 10): yield x
    for x in range(0, 10000, 100): yield x

def gen_b ():
    yield from range(0, 100, 1)
    yield from range(0, 1000, 10)
    yield from range(0, 10000, 100)

t = time()
for x in range(10000): a = list(gen_a())
print(time()-t)

t = time()
for x in range(10000): b = list(gen_b())
print(time()-t)

print('gen_a == gen_b?', a == b)

# o codigo com yield from e mais simples e eficiente
