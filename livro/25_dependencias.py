#!/usr/python3.5
"""
DEPENDENCIAS
e uma pratica comum o uso de varios pacotes de terceiros na construcao de um
aplication, e com isso surgiram ferramentas para lidar com essas dependencias.

AMBIENTES VIRTUAIS
e uma copia completamente funcional do interpretador que permite o
desenvolvimento de um projeto sem interferir em outros projetos na mesma
instalacao de python.
O utilitario mais usado para criar e manter ambientes virtuais no python e o
virtualenv. Ele cria uma pasata dentro da pasata do projeto, onde existe uma
copia do interpretador e outros arquivos necessarios, e uma pasta site-packages
exclusiva para os pacotes do projeto.
O comando virtualenv cria a pasta activate para ativar o ambiente virtual e
deactivate para voltar a usar o interpretador de forma convencional. Enquanto o
ambiente virtual estiver ativado, os comandos de gerencia de pacotes (como pip)
agirao sobre os arquivos da pasta criada pelo virtualenv.

Como o pacote novo foi instalado com o ambiente virtual ativado, ele foi
colocado no site-packages do ambiente e se tornou parte do ambiente, portanto
so ficara disponivel com o ambiente ativado.
A partir da versão 3.3, a distruibuicao oficial passou a incluir um modulo
chamado venv como funcionalidade semelhante.

EMPACOTAMENTO E DISTRIBUICAO
Geralmente e bem mais simples distribuir aplicacoes na forma de binario, em que
rodar um executavel para iniciar a aplicacao, do que instalar todas as
dependencias necessarias em cada maquina em que se deseja executar a aplicação.
Existem varios softwares que permitem gerar exceutaveis a partir de um programa
feito em python, como  cx_freeze.
O cx_freeze e portavel, podendo rodar em (e gerar executaveis para ambientes
unix.)
O cx_freeze e um utilitario de linha de comando.
    FreezePython -00 -c sim.py
A opcao -c faz com que o bytecode seja comprimido no formato zip e -00 ativa a
otimizacao.
    FreezePython -00 -include-modules=atk,cairo,pango,pangocairo simgtk.py
O cx_freeze nao e um compilador. O que ele faz e empacotar os bytecodes da
aplicacao, suas dependencias e o interpretador em (pele menos) um arquivo
executavel (e arquivos auxiliares) que nao dependem do ambiente em que foram
gerados. Com isso, a distribuição do aplicatiov se torna bem mais simples.
Entretanto nao existe ganho de desempenho em gerar executaveis, exceto pela
carga de aplicacao para a memoria em alguns casos.
Ele tambem nao gera programas de instalacao. Para isso e necessario o uso de um
software especifico. Os instaladores sao gerados por aplicativos que se
encarregam de automatiazar a tarefas comuns do processo de instalacao. Sao
exemplos de software dessa categoria: Inno Setupe e NSIS.
"""
