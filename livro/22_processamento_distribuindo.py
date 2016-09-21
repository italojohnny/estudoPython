#!/usr/python3.5
"""
PROCESSAMENTO DISTRIBUIDO
Geralmente a solucao para problemas que requerem muita potencia computacional
e a utilizacao de maquinas mais poderosas, porem esta solucao e limitada em
termos de escalabilidade. Uma alternativa e dividir os processos da aplicacao
entre varias maquinas que se comunicam atraves de uma rede, formando um cluster
ou um grid.
A diferenca baseica entre clster e grid e que o primeiro tem como premissa de
projeto ser um ambiente controlado, homogeneo e previsivel, enquanto o segundo
e geralmente heterogeneo, na controlado e imprevisivel. Um cluster e um
ambiente planejado especificamente para processamento distribuido, com maquinas
dedicadas em um lugar adequado. Um grid se caracteriza pelo uso de estacoes de
trabalho que podem estar em qualquer lugar.
Os modelos mais comuns de cluster sao:
    * o computacional
    * de recursos
    * de aplicacao ou hibrido
O modelo computacional tem como objetivo usar processadores e memoria dos
equipamento envolivdos para obter mais potencia computaciona. A implementacao
geralmente utiliza um sistema escalonador de filas (metascheduler) que realiza
o agendamento das tarefas a serem processadas pelos nós (maquinas que compoem
o modelo). Com isso a operacao tende a ser coninua, com interacao reduzida com
os usuarios. Um exemplo conhecido e o SET@home.
O cluster de recursos e usado para armazenar informacoes em um grupo de
computadores, tanto para obter mais performance de recuperacao de dados quanto
para expandir a capacidade de armazenamento. Este modelo pode ser usado para
prover infraestrutura para aplicacoes ou para atender a requisicoes feitas de
forma interativa por usuarios. Entre os servicos que podem operar dessa forma
estao os sistemas geranciadores de banco de dados (sgdb), como o mysql cluster.
O modelo hibrido e uma aplicacao projetada especificamente para funcionar em
varias maquinas ao mesmo tempo. Em vez de prover recursos diretame3nte, a
aplicacao utiliza os equipamentos para suportar suas proprias funcionalidades.
Com isso, a infraestrurua e usada de forma quese transparente pelos usuarios que
utilizam a aplicacao interativamente. Todos os nos rodam o aplicativo e podem
operar como servidores e clientes. O exemplo mais comum de arquitetura hibrida
sao os sistemas de compartilhamento de arquivos (file sharing) que usam
comunicacao peer to peer (p2p)
Independentemente do modelo utilizado, sistemas distribuidos devem atender a
quatro requisitos basicos:
    * comunicacao - as maquinas envolvidas deem se comunicar de forma a
    permitir a troca de informacoes entre elas
    * metadados - os dados sobre o processamento precisam ser mantidos de forma
    adequada
    * controle - os processos devem ser gerenciados e monitorados
    * seguranca - o sigilo, a integridade e a disponibilidade deem estar
    protegidos.
Existem diversas tecnologias voltadas para o desenvolvimento de aplicacoes
distribuidas, tais como xml-rpc, web services, objetos distribuidos, mpi e
outras.
"""
