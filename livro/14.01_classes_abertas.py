#!/usr/python3.5
"""
CLASSES ABERTAS
as classes que nao sao built-in's podem ser alteradas em tempo de excecuao
gracas a natureza dinamica da linguagem. E possivel acrescentar metodos e
atributos novos, por exemplo. A mesma logica se aplica aos objetos.
"""

class User (object):
    def __init__ (self, name):
        self.name = name

def set_password (self, password):
    self.password = password

print('classe original:', dir(User))

User.set_password = set_password
print('classe original:', dir(User))

user = User('guest')
user.set_password('guest')

print('objeto:', dir(user))
print('senha:', user.password)

# a classe modificada passou a ter um novo metodo: set_passowrd()

