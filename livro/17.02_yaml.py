#!/usr/python3.5
"""
YAML (YAMIL Ain't a Markup Language)
e um formato de serializacao de dados para texto que representa os dados como
combinacoes de listas, dicionarios e valores escalares. Tem como principal
caracteristica ser legivel por humanos.
O projeto YAML foi muito influenciado pela sintaxe do python e outras linguagens
dinamicas. Entre outras estruturas, a especificacao do YAML define que:
    * os blocos sao marcados por endentacao.
    * listas sao delimitadas por colchetes ou indicadas por traco.
    * chaves de dicionario sao seguidas de dois pontos.
Listas podem ser representadas assim:
    - Azul
    - Branco
    - Vermelho
Ou:
    [Azul, Branco, Vermelho]
Dicionarios sao representados como:
    cor: Branco
    nome: Bandit
    raca: Labrador
PyYAML e um modulo de rotinas para gerar e processar YAML no python.
"""
# exemplo de conversao para yaml
import yaml
progs = {
        'inglaterra': {
                'yes': ['close to the edge', 'gragile'],
                'genesis': ['foxtrot', 'the nursey crime'],
                'king crimson': ['red', 'discipline']
                },
        'alemanha': {
            'kraftwerk': ['radioactivity', 'trans europe express']
            }
        }
print(yaml.dump(progs))

# exemplo de leitura de yamal
'''
prefs.yaml
- musica: rock
- cachorro:
    cor: branco
    nome: bandit
    raca: labrador
- outros:
    intrumentos: baixo
    linguagem: [python, ruby]
    comida: carne
'''
import pprint
import yaml
# yaml.load() pode receber um arquivo aberto
# como argumento
yml = yaml.load(open('prefs.yaml'))
# print.pprint() mostra a estrutura de dados
# de uma forma mais organizada do que a funcao print() convencional
pprint.pprint(yml)
"""
YAML e muito pratico para ser usado em arquivos de configuracao e outros que os
dados podem ser manipulador diretamente por pessoas.
"""
