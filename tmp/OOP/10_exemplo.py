#!/usr/python3.5

class Float:
    def __init__ (self, inicial=0):
        self.inicial = inicial
        self.data = {}

    def __get__ (self, instance, owner):
        return self.data.get(instance, self.inicial)

    def __set__ (self, instance, val):
        if not isinstance(val, float):
            raise TypeError ("%s não é float" % repr(val))
        self.data[instance] = val

class Vetor:
    x = Float()
    y = Float()
    z = Float()

    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__ (self):
        return "Vetor(%.2f, %.2f, %.2f)" % (self.x, self.y, self.z)

    def modulo (self):
        return round((self.x + self.y + self.z) **.5, 2)


v = Vetor(1., 2., 3.)
print(v)
print("Módulo:", v.modulo())

v.x = 2.
print(v)
print("Módulo:", v.modulo())

v.y = '3.'

