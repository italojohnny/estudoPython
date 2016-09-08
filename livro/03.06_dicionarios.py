#!/usr/python3.5

# um dicionario e como uma listas, porem contem chaves unicas e para os valores.
# a chave pode ser qualquer valor imutavel: numeros, string, etc
# o valore pode ser qualquer tipo mutavel, numero, string, lista, tupla, outro dicionario etc

# sintaxe
dicionario = {'a': 'string', 'b':'inteiro', 'c':'lista'}

# acessando elementos
print('a: ', dicionario['a'])

# adicionando elemento
dicionario['d'] = 'outro dicionario'

# apagando elemento
del dicionario['b']

# obtendo os itens, chaves e valores
print('itens: ', dicionario.items())
print('chave: ', dicionario.keys())
print('valores: ', dicionario.values())

# exemplo
progs = {'yes': ['close to the edge', 'fragile'], 'genesis':['foxtrot', 'the nursery crime'], 'elp': ['brain salad surgery']}
progs['king crimson'] = ['red', 'discipline']

# items() retorna uma lista de tuplas com a chave e o valor
for prog, albuns in progs.items():
    print(prog, '->', albuns)
print (len(progs), 'bandas')

# procurar uma chave, se encontrar apaga ela
if 'elp' in progs:
    del progs['elp']

print ('agora', len(progs), 'bandas')

# matriz esparsa implementada com dicionario:
dim = 6, 12 # uma tupla com as dimensoes da matriz
mat = {} # um dicionario sem nenhum elemento

mat[3, 7] = 3
mat[4, 6] = 5
mat[6, 3] = 7
mat[5, 4] = 6
mat[2, 9] = 4
mat[1, 0] = 9

for lin in range(dim[0]):
    for col in range(dim[1]):
        print(mat.get((lin, col), 0), end=' ')
    print()

matriz = '''0 0 0 0 0 0 0 0 0 0 0 0
9 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 3 0 0 0 0
0 0 0 0 0 0 5 0 0 0 0 0
0 0 0 0 6 0 0 0 0 0 0 0'''
mat = {}

for lin, linha in enumerate(matriz.splitlines()):
    for col, coluna in enumerate(linha.split()):
        coluna = int (coluna)
        if coluna:
            mat[lin, col] = coluna
print(mat)
print('tamanho da matriz completa ', (lin+1)*(col+1))
print('tamanho da matriz esparsa: ', len(mat))
