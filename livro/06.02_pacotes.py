#!/usr/python3.5
'''
Pacotes (pakages) regulares sao pastas que sao identificadas pelo
interpretador pela presenca de um arquivo com o nome __init__.py. Os pacotes
funcionam como colecoes para organizar modulos de forma hieraquica.
+--------------------+
|componetes          | <-- esta pasta e um pacote
|                    |
|+------------------+|
||    __init__.py   || <-- identifica a pasta como pacote
|+------------------+|
|+------------------+|
||    sensor.py     || <-- componentes.sensor
||+----------------+||
|||        termico ||| <-- componentes.sensor.termico
||+----------------+||
|+------------------+|
|                    |
|+------------------+|
||    display.py    || <-- componentes.display
||+----------------+||
|||        crt     ||| <-- componentes.display.crt
||+----------------+||
|||        lcd     ||| <-- componentes.display.lcd
||+----------------+||
|||        oled    ||| <-- componentes.display.oled
||+----------------+||
|+------------------+|
+--------------------+

E possivel importar todos os modulos (tirando os que tem nome comecando por "__")
do pacote usando a declaracao from nome_do_pacote import *.

O arquivo __init__.py pode estar vazio ou conter codigo de inicializacao do
pacote ou definir uma variavel chamada __all__, que e uma lista de modulos que
pertencem ao pacote e que serao importados quando for usado "*" na importacao.

A partir da versao 3.3, e possivel usar pastas sem __init__.py como pacotes,
com a unica restricao de fazer parte de PYTHONPATH. Esse tipo de pacotes se
chama Implicit Namespace Package, que permite espalhar modulos por varias pastas,
mesmo que pertencam ao mesmo pacote.
'''
