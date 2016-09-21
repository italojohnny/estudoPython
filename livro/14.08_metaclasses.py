#!/usr/python3.5
"""
METACLASSES
em uma linguagem orientada a objetos em que (quase) tudo sao objetos e todo
objeto tem uma classe, e natural que as classes tambem sejam tratadas como
objetos.
Metaclasse e uma classe cujas instancias sao classes; sendo assim, a metaclasse
define o comportamento das classes derivadas a partir dela. Em python, a classe
type e uma metaclasse e pode ser udada para criar outras metaclasses.
"""
class Singleton (type):
    def __init__ (cls, name, bases, dic):
        type.__init__(cls, name, bases, dic)

        def __copy__ (self):
            return self

        def __deepcopy__ (self, memo=None):
            return self

        cls.__copy__ = __copy__
        cls.__deepcopy__ = __deepcopy__

    def __call__ (cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)
            return cls.__instace

import pymysql
class Con(metaclass=Singleton):
    def __init__ (self):
        self.con = pymysql.connect(user='root')
        self.db = self.con.cursor()

class Log (metaclass=Singleton):
    def __init__ (self):
        self.log = open('msg.log', 'w')

    def write (self, msg):
        self.log.write(str(msg) +'\n')


con1 = Con()
Log().write('con1 id  %d' % id(con1))
con1.db.execute('show processlist')
Log().write(con1.db.fetchall())

con2 = Con()
Log().write('con2 id %d' % id(con2))
con1.db.execute('show processlist')
Log().write(con2.db.fetchall())

import copy
con3 = copy.copy(con1)
Log().write('con3 id = %d' % id(con3))
con3.db.execute('show processlist')
Log().write(con3.db.fetchall())

# com isso, todas as referencias apontam para o mesmo objeto, e o recurso (a
# conexao de banco de dados) e reaproveitado.
