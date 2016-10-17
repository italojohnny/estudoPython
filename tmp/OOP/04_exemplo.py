#!/usr/python3.5

class User:
    '''uma classe bem simples'''
    def __init__ (self, name):
        '''inicializa a classe, atributo nome'''
        self.name = name

# um novo método para a classe
def set_password (self, password):
    self.password = password


print("Classe original:", dir(User))
print('===========================')
#O novo método é inserido na classe
User.set_password = set_password
print("Classe modificada:", dir(User))

user = User('guest')
user.set_password('guest')

print('Objeto:', dir(user))
print('Senha:', user.password)



