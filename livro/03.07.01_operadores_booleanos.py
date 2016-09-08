#!/usr/python3.5

# operadores booleanos
# and, or, not, is e in.
print('AND')
# and: retorna um valor verdadeiro se e somente se receber duas expressoes verdadeiras
if True and False: print('opcao1')
else: print('opcao2')

if False and True: print('opcao1')
else: print('opcao2')

if True and True: print('opcao1')
else: print('opcao2')

if False and False: print('opcao1')
else: print('opcao2')

print('OR')
# or: retorna um valor falso se e somente se receber duas expressoes que forem falsas
if True or False: print('opcao1')
else: print('opcao2')

if False or True: print('opcao1')
else: print('opcao2')

if True or True: print('opcao1')
else: print('opcao2')

if False or False: print('opcao1')
else: print('opcao2')

print('NOT')
# not: inverte retorno, ser for verdadeiro, vira falso; se falso, verdadeiro
if not True: print('opcao1')
else: print('opcao2')

if not False: print('opcao1')
else: print('opcao2')

print('IN')
# retorna verdadeiro se receber um item e uma lista e o item ocorrer uma ou mais vezes na lista e falso em caso contrario
if 4 in (2, 4, 5): print('opcao1')
else: print('opcao2')

if 3 in (2, 4, 5): print('opcao1')
else: print('opcao2')

print('IS')
# retorna verdadeiro se receber duas referencias ao mesmo objeto e falso em caso contrario
if 2 is 2: print('opcao1')
else: print('opcao2')

if 2 is 3: print('opcao1')
else: print('opcao2')

# ainda existe all() e any()
# all() retorna True quando todos os resultados forem verdadeiro
# any() retorna True quando qualquer valor for verdadeiro
