#!/usr/python3.5
"""
BANCO DE DADOS
sistemas gerenciadores de banco de dados (sgbds) sao reconhecidos por prover uma
forma de acesso consistente e confiavel para informacoes.
A maioria dos sgbds autais sao baseados no modelo relaciona, no qual as
informacoes sao representadas na forma de tabela. Geralmente, estas tableas
podem ser consultadas por meio de uma linguagem especializada para isso, chamada
sql (structured query language).
Geralmente os sgbds utilizam a arquitetura clinte-servidor. Os aplicativos usam
a api cliente para poder se comunicar com o servidor, que e o responsavel por
receber as consultas dos clientes, interpretar as sentencas sql e recuperar os
dados com um tempo de resposta adequado.
Para fazer isso, o servidor precisa realizar uma serie de outras tarefas, tais
como verificar credenciais, controlar o acesso, gerenciar conexoes de rede,
manter a integridade dos dados, otimizar as consultas e resolver questoes de
concorrencia.
No python, a integracao com sgbds e feita na maioria dos casos por meio de um
modulo dbi, que usa api cliente para se comunicar com o banco de dados.
"""

