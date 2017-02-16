#!//usr/bin/python2.7
import re

def enum (*_tuple, **_dict):
    for i in _tuple:
        if not isinstance(i, str) or (isinstance(i, str) and re.search(r'\s', i)):
            raise "ERRO: Caso use tupla, use apenas strings sem espaco"
    
    # TODO verificar se dicionario possue valores repetidos. Se sim, excecao!

    enums = dict(zip(_tuple, range(len(_tuple))), **_dict)
    return type("Enum", (), enums)

if __name__ == "__main__":

    status = enum("ZERO", "ONE", "TWO", "THREE")
    naruto = enum(
            SENIN=0,
            RONIN=0,
            HOKAGE=2,

            )

    print status.ZERO
    print naruto.SENIN
    print naruto.RONIN
