#!/usr/python3.5
"""
CLASSES
Objetos sao abstracoes computacionais que representam entidades, com sua
qualidades (atributos) e as acoes (metodos) que estas podem realizar. A classe
e a estrutura basica do paradigma de orientacao a objetos, que representa o tipo
do objeto, um modelo do qual os objetos sera criados.

Os atributos sao estruturas de dados que armazenam dados sobre o objeto e os
metodos sao funcoes associadas ao objeto, que descrevem como o objeto se
comporta.

Novos objetos sao criados a partir das classes por meio de atribuicao. O objeto
e uma instancia da classe, que possui caracteristicas proprias. Quando um novo
objeto e criado, o construtor da classe e executado. O construtor e um metodo
especial, chamado __new__(). Apos a chamada ao construtor, o metodo __init__() e
chamado para inicializar a nova instancia.

Um objeto continua existindo na memoria enquanto houver pelo menos uma
referencia a ele. O interpretador python possui um recurso chamado coletor de
lixo (Garbage Colletor) que limpa da memoria objetos sem referencias. Quando o
objeto e apagado, o metodo especial __done__() e evocado. Funcoes ligadas ao
coletor de lixo podem ser encontradas no modulo gc.

E python:
    * quase tudo e objeto, mesmo os tipos basicos, como numeros inteiros;
    * tipos e classes sao unificados;
    * os operadores sao na verdade chamadas para metodos especiais;
    * as classes sao abertas (menos para os tipos built-ins).

Metodos especiais sao identificados por nomes no padrao __metodo__() (dois
underlines no inicio e no final do nome) e definem como os objetos derivados da
classe se comportarao em situacoes particulares, como em sobrecarga e
operadores.

As classes sao derivadas da classes object e podem utilizar recursos como
propriedades (properties) e metaclasses. Propriedades sao atributos calculados
em tempo de execucao por meio de metodos, enquanto as metaclasses sao classes
que geram classes. Com isso, permite personalizar o comportamento das classes.
"""

class Supcl1:
    """ Uma classe muito simples """
    varsup1 = 1

class Supcl2:
    """ Outra classe muito simples """
    varsup1 = 2

class Classe (Supcl1, Supcl2):
    """ Isto e uma classe que herda de Supcl1 e Supcl2 """
    clsvar = []

    def __init__ (self, args):
        ''' construtor da classe '''
        self.args = args

    def __done__ (self):
        ''' destrutor da classe '''
        del self.args

    def metodo (self, params):
        ''' metodo do objeto '''
        self.args += params

    @classmethod
    def cls_metodo (cls, params):
        ''' metodo de classe '''
        cls.clsvar = params

    @staticmethod
    def est_metodo (params):
        ''' metodo estatico '''
        return params

obj = Classe (0)
obj.metodo(-1)
Classe.cls_metodo(3)
Classe.est_metodo(4)

"""
Metodos de objeto podem usar atributos e outros metodos do objeto. A variavel
self, que representa o objeto, tambem precisa ser referenciada de forma
explicita. O nome self e uma convencao, assim como cls, podendo ser troado por
outro nome qualquer, porem e considerado como boa pratica manter o nome.

Metodos de classe podem usar apenas atributos e outros metodos de classe. O
argumento cls representa a classe em si e precisa ser passada explicitamente
como primeiro parametro do metodo.

Medodos estaticos sao aqueles que nao tem ligacao com atributos do objeto ou da
classe. Funciona como as funcoes comuns.
"""

class Cell (object):
    """Classe para celulas de planilhas"""
    def __init__ (self,formula='""', formato='%s'):
        '''construtor'''
        self.formula = formula
        self.formato = formato

    def __repr__ (self):
        '''retorna representacao em string da celula'''
        return self.formato % eval(self.formula)

print(Cell('123*2'))
print(Cell('23*2+2'))
print(Cell('abs(-1.45 / 0.3)', '%2.3f'))

"""
O metodo __repr__() e usado internamente pelo comando print para obter uma
representacao  do objeto em forma de texto.
Em python, nao existem variaveis e metodos privados (que so podem ser acessados
a partir do proprio objeto). Em vez disso, e usado uma convencao. Usar um nome
que comece com underline deve ser condiderado parte da implementacao interna do
objeto, portanto, esta sujeito a mudancas sem aviso previo. Alem disso, a
linguagem oferece uma funcionalisade chamada name mangling, que acrescenta uma
underline e o nome da classe na frente de nomes iniciam com dois underlines
"""

class Calc:
    def __init__ (self, formula, **vars):
        self.formula = formula
        self.vars = vars
        self.__recalc()

    def __recalc (self):
        self.__res = eval(self.formula, self.vars)

    def __repr__ (self):
        self.__recalc()
        return str(self.__res)

formula = '2*x + 3*y + z**2'
calc = Calc(formula, x=2, y=3, z=1)
print('fomula:', calc.formula)
print('x =', calc.vars['x'], '-> calc =', calc)

calc.vars['x'] = 4
print('x =', calc.vars['x'], '-> calc =', calc)
print(dir(calc))

"""
O metodo __recal() aparece como _Calc__recalc() e o atributo __res como
_Calc__res para fora do objeto.
"""
