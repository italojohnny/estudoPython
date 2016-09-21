#!/usr/python3.5
"""
DBI (database interface)
e uma especificacao que descreve como deve ser o comportamento de um modulo de
acesso a sistemas de banco de dados. O modulo contem a logica de comunicacao com
o sgbds.
A DBI define que o modulo deve ter uma funcao connect, que retorna objets de
conexao. A partir do objeto de conexao, e possivel obter um objeto cursor, que
permite a execucao de sentencas sql e a recuperacao dos dados (uma lista de
tuplas com os resultados, por default).
"""
