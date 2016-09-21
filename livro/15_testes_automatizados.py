#!/usr/python3.5
"""
TESTES AUTOMATIZADOS
A atividade de testar software e uma tarefa repetitiva, demorada e tediosa. Por
isso, surgiram varias ferramentas para automatizar teste. Existem dois modulos
para teste automatizados que acompanham python: doctest e unittest.

O modulo doctest usa as Doc Strings que estao presentes no codigo para definir
os testes de codigo. A funcao testmode() do doctest() procura por um trecho de
texto que seja semelhante a uma sessao interativa de python, executada a mesma
sequencia de comandos, analisa a saida e faz um relatorio dos testes que
falharam, com os erros encontrados.
"""

# Exemplo
#"""
#fib.py
#Implementa Fibonacci.
#"""
#def fib(n):
#    """ Fibonacci
#    Se n <= 1, fib(n) = 1
#    Se n > 1, fib(n) = fib(n -1) ) + fib(n -2)
#
#    Exemplo de uso:
#    >>> fib(0)
#    1
#    >>> fib(1)
#    1
#    >>> fib(10)
#    189
#    >>> fib('')
#    Traceback (most recent call last):
#        File "/usr/lib/python3.5/doctest.py", line 1321, in __run
#        compileflags, 1), test.globs)
#        File "15_testes_automatizados.py", line 36, in fib
#            raise TypeError
#    TypeError
#    """
#    if not type(n) is int:
#        raise TypeError
#    if n > 1:
#        return fib(n -1) + fib(n -2)
#    else:
#        return 1
#
#def _doctest():
#    """Evoca o doctest"""
#    import doctest
#    doctest.testmod()
#
#if __name__ == "__main__":
#    # Os testes sera executados se este modulo
#    # for evocado diretamente pleo python
#    _doctest()
"""
Se todos os testes forem bem-sucedidos, nao havera relatorio de testes.
Exemplo de relatorio de erros dos testes (a Doc string foi alterada de proposito
para gerar um erro):

**********************************************************************
File "15_testes_automatizados.py", line 30, in __main__.fib
Failed example:
    fib(10)
Expected:
    189
Got:
    89
**********************************************************************
1 items had failures:
    1 of   4 in __main__.fib
***Test Failed*** 1 failures.


Usando o modulo unittest, os teste sao criados por meio de uma subclasse da
classe unittest.TestCase. Os testes sao definidos como metodos da subclasse. Os
metodos precisam ter seus nomes iniciando com 'test' para que sejam
identificados como rotinas de teste.

Os metodos de teste devem evocar ao terminar um dos metodos:
    * assert_      - verifica se uma condicao e atingida
    * assertEqual  - verifica se o resultado e igual ao parametro passado
    * AssertRaises - verifica se a excecao e a esperada

Se houver um metodo chamado setUp, este sera executado antes de cada teste;
assim sera possivel reinicializar variaveis e garantir que um teste nao
prejudique o outro. O final dos testes, o unittest, gera o relatorio com os
resultados encontrados.
"""
# exemplo
'''
fibtest.py
usa unittest para testar fib.py
'''
import fib
import unittest

class TestSequenceFunctions (unittest.TestCase):
    # Metodos que definem os teste.
    def setUp (self):
        self.seq = range(10)

    def test0 (self):
        self.assertEqual(fib.fib(0), 1)
    def test1 (self):
        self.assertEqual(fib.fib(1), 1)
    def test10 (self):
        self.assertEqual(fib.fib(10), 89)

    def testseq (self):
        fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for x, y in zip(fibs, [fib.fib(x) for x in self.seq]):
            self.assertTrue(x is y)

    def testtype (self):
        self.assertRaises(TypeError, fib.fib, '')

if __name__ == '__main__':
    unittest.main()

"""
No relatorio, o terceiro teste falhou, pois 'fib.fib(10)' retornou 100 em vez de
89, como seria esperado.
O unittest oferece uma solucao muito semelhante a bibliotecas de testes
implementadas em outras linguagens, enquanto o doctest e mais simples de usar e
se integra bem com a documentacao (as sessoes do doctest podem servir como
exemplo de uso).
"""
