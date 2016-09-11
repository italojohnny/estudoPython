#!/usr/python3.5
"""
DESCRITORES
e uma forma mais geral de definir como os atributos sao calculados por meio de
um protocolo. Com isso e possivel obter um codigo mais facil de reaproveitar do
que com properties.
O protocolo convenciona as seguinte assinaturas de metodos:
    * descriptor.__get__(self, obj, type=None) que retorna um valor;
    * descriptor.__set__(self, obj, val)       que retorna None;
    * descriptor.__delete__(set, obk)          que retorna None.
O descritor deve definir um ou mais desses metodos
"""

class Float:
    def __init__ (self, inicial=0):
        self.inicial = inicial
        self.data = {}

    def __get__ (self, instance, owner):
        return self.data.get(instance, self.inicial)

    def __set__ (self, instance, val):
        if not isinstance(val, float):
            raise TypeError('%s nao e float' % repr(val))
        self.data[instance] = val

class Vector:
    x = Float()
    y = Float()
    z = Float()
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__ (self):
        return 'vector(%.2f, %.2f, %.2f)' % (self.x, self.y, self.z)

    def modulo (self):
        return round((self.x + self.y + self.z)** .5, 2)

v = Vector(1., 2., 3.)
print(v)
print('modulo:', v.modulo())
v.x = 2.
print(v)
print('modulo:', v.modulo())
v.x = '3.'

# com isso e mais facil reaproveitar a validacao de tipo
