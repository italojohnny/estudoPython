#!/usr/bin/python2.7
import re

def enum (*_tuple, **_dict):
    for i in _tuple:
        if not isinstance(i, str) or (isinstance(i, str) and re.search(r'\s', i)):
            raise Exception("Caso use tupla, use apenas strings sem espaco.")

    if _tuple and len(set(_tuple)) != len(_tuple):
        raise Exception("Caso use tupla, nao repita os valores.")
    
    if _dict and len(set(_dict.values())) != len(_dict.values()):
        raise Exception("Caso use dicionario, nao repita os valores das chaves.")

    enums = dict(zip(_tuple, range(len(_tuple))), **_dict)
    return type("Enum", (), enums)

if __name__ == "__main__":

    status = enum("ZERO", "ONE", "TWO", "THREE")
    naruto = enum(
            GENIN=0,
            CHUUNIN="1",
            JOUNIN=2,
            HOKAGE=3

            )

    print status.ZERO

