#!/usr/python3.5
# set: sequencia mutavel univoca (sem repeticao) nao ordenada
# frozenset: sequencia imutavel univoca nao ordenada
# os dois tipos implementam operacoes de conjuntos, tais como uniao, intersecao e diferenca

# conjunto de dados
s1 = set(range(3))
s2 = set(range(10, 7, -1))
s3 = set(range(2, 10, 2))
print('s1: ', s1,'\ns2: ', s2, '\ns3: ', s3)

uniao = s1.union(s2)
print('uniao de s1 com s2: ', uniao)

diferenca = uniao.difference(s3)
print('diferenca da unicao com s3: ', diferenca)

intersecao = uniao.intersection(s3)
print('intersecao da uniao com s3: ', intersecao)

if s1.issuperset([1,2]):
    print('s1 inclui 1 e 2')

if s1.isdisjoint(s2):
    print('s1 e s2 nao tem elementos em comun')

# quando listas sao convertidas para sets, as repeticoes sao descartadas
