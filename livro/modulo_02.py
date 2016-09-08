#!/usr/python3.5
"""
modulo_02 => rotinas utilitarias para modulos
"""
import os.path
import sys
import glob

def find (txt):
    """
    encontra modulo que tem o nome contendo o parametro
    """
    resp = []
    for path in sys.path:
        mods = glob.glob('%s/*.py' % path)
        for mod in mods:
            if txt in os.path.basename(mod):
                resp.append(mod)
    return resp
