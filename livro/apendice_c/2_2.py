#!/usr/python3.5
'''
2. Implementar um modulo com duas funcoes:
	* matrix_sum(*matrices),  que retorna a matriz soma de matrizes de duas
	dimensoes.
	* camel_case(s), que converte nomes para CamelCase.
'''
def matrix_sum (*matrices):
    '''soma matrizes de duas dimensoes'''
    mat = matrices[0]
    for matrix in matrices[1:]:
        for x, row in enumerate(matrix):
            for y, col in enumerate(row):
                mat[x][y] += col
    return mat

def camel_case (s):
    '''formata strings DestaForma'''
    return ''.join(s.title().split())

if __name__ == '__main__':
    print(matrix_sum([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print(camel_case('close to the edge'))
