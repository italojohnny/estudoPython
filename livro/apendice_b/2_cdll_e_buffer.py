#!/usr/python3.5
import ctypes
"""
msvcrt e a biblioteca com a maioria das funcoes
padroes da linguagens C no windows
o windows coloca automaticamente
a extensao do arquivo
"""
clib = ctypes.cdll.msvcrt

"""
cria um buffer para receber o resultado
a referencia para o buffer sera passada para
a funcao, que preenche o buffer com o resultado
"""
s = ctypes.c_buffer(b'\000', 40)
"""
sscanf() e uma funcao que extrai valores
de uma string conforme uma mascara
"""
clib.sscanf(b'Testando sscanf!\n', b'Testando %s!\n', s)
# mostra o resultado
print(s.value)

