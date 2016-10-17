#!/usr/python3.5

class Calc:
    def __init__ (self, formula, **vars):#carece explicação o **vars
        self.formula = formula
        self.vars = vars
        self.__recalc()

    def __recalc (self):
        self.__res = eval(self.formula, self.vars)

    def __repr__ (self):
        self.__recalc()
        return str(self.__res)

formula = '2*x +3*y +z**2'
calc = Calc(formula, x=2, y=3, z=1)

print('formula:', calc.formula)
print('x =', calc.vars['x'], '-> calc =', calc)

calc.vars['x'] = 4
print('x =', calc.vars['x'], '-> calc =', calc)
print(dir(calc))
