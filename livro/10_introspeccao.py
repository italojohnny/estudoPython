#!/usr/python3.5
'''
introspeccao ou reflecao, e a capacidade do software identificar e relatar suas
proprias estruturas internas, tais como tipos, escopo de variaveis, metodos e
atributos.

| type(obj)                   | tipo (classe) do obj
| id(obj)                     | identificador do obj
| locals()                    | dicionario de variaveis locais
| globals()                   | dicionario de variaveis globais
| vars(obj)                   | dicionario de simbolos do obj
| len(obj)                    | tamanho do obj
| dir(obj)                    | lista de estruturas do obj
| help(obj)                   | docstrings do obj
| repr(obj)                   | representacao do obj
| isinstance(obj, class)      | verdadeiro se obj deriva da classe
| issubclass(subclass, class) | verdadeiro se subcalsse herda classe

o identificador do objeto e um numero inteiro unico que e usado pelo
interpretador para identificar internamente os objetos.
'''
from types import ModuleType

def info(n_obj):
    obj = globals()[n_obj]
    print('nome obj:', n_obj)
    print('identificador:', id(obj))
    print('tipo:', type(obj))
    print('representacao:', repr(obj))

    if isinstance(obj, ModuleType):
        print('itens:')
        for item in dir(obj):
            print(item)
    print()

for n_obj in dir():
    info(n_obj)

# tambem tem um modulo chamdo types, que tem algumas definicoes de tipos basicos do interpretador
# Por meio da introspeccao e possivel determinar os campos de uma tabela de banco de dados, por exemplo
import types

def f ():
    return True

if isinstance(f, types.FunctionType):
    print('f e uma funcao')

'''
inspect
o modulo inspect prove um conjunto de funcoes de alto nivel para introspeccao
que permite investigar tipos, itens de colecoes, classes, funcoes, codigo-fonte
e a pilha de execucao do interpretadr.
'''
import os.path
import inspect
print('obj:', inspect.getmodule(os.path))
print('class?:', inspect.isclass(str))
print('membros:', end=' ')
for name, struct in inspect.getmembers(os.path):
    if inspect.isfunction(struct):
        print(name, end=' ')

'''
as funcoes que trabalham com a pilha do interpretador deve ser usadas com
cuidado, pois e possivel criar referencia ciclicas (uma variavel que aponta para
o item da pilha que tem a propria variavel). A existencia de referencias a itens
da pilha retarda a destruicao dos itens pelo coletor de lixo do interpretador.
'''
