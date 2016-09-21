#!/usr/python3.5
import cProfile

def rgb1 ():
    '''funcao usando range()'''
    rgbs = []
    for r in range(256):
        for g in range(256):
            for b in range(256):
                rgbs.append('#%02x%02x%02x' % (r, g, b))
    return rgbs

def rgb2 ():
    '''funcao usando uma lista varias vezer'''
    rgbs = []
    ints = range(256)
    for r in ints:
        for g in ints:
            for b in ints:
                rgbs.append('#%02x%02x%02x' % (r, g, b))
    return rgbs

def rgb3 ():
    '''gerador usando range()'''
    for r in range(256):
        for g in range(256):
            for b in range(256):
                yield '#%02x%02x%02x' % (r, g, b)

def rgb4 ():
    '''gerador usando apenas uma lista'''
    for i in range(256 ** 3):
        yield '#%06x' % i

def rgb5 ():
    '''funcao usando while'''
    rgbs = []
    rgb = 0
    while rgb < 256 ** 3:
        rgbs.append('#%06x' % rgb)
        rgb += 1
    return rgbs

def rgb6 ():
    '''funcao usando list comprehension'''
    return ['#%06x' % i for i in range(256 ** 3)]

if __name__ == '__main__':
    # benchmarks
    print('==================RGB1==================')
    cProfile.run('rgb1()')
    print('==================RGB2==================')
    cProfile.run('rgb2()')
    print('==================RGB3==================')
    cProfile.run('rgb3()')
    print('==================RGB4==================')
    cProfile.run('rgb4()')
    print('==================RGB5==================')
    cProfile.run('rgb5()')
    print('==================RGB6==================')
    cProfile.run('rgb6()')
