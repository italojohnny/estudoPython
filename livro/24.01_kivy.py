#!/usr/python3.5
"""
PLATAFORMAS PORTATEIS
Com a expansao do mercado de equipamentos portateis (smartphones e tablets), a
demanda pela criacao de aplicativos para sistemas que funcinam nesses
equipamentos tambem cresceu. Eles tem em cmum um poder de processamento
razoavel, suporte a multimidia, interface de toque e acesso a internet. Com
python, e possivel produzir programas de forma portavel para os principais
sistemas (Android e IOS)

KIVY
e um framework que simplifica a criacao e a distribuicao de aplicacoes para
estas plataformas. O sistema pode ser desenvolvido e testado em um PC ou em um
Mac rodando um sistema desktop, para ser usado em portateis.
A arquitetura do Kivy e orientada a eventos que podem estar associados a
elementos de interface ou ao relogio. Todo objeto de interface tem um canvas
associado, que e um conjunto de instrucoes OpenGL.
Um projeto em Kivy e uma pasta que contem um modulo principal que deve ter o
nome main.py e para funcionar adequadamente no Android, um arquivo chamado
android.txt, com configuracoes.

Para testar os aplicatiovs sem precisar postar na loja de aplicativos, existe o
Kivy Launcher. Para ele reconhecer o aplicativo, basta copiar a pasta do
aplicativo para uma pasta chamada kivy na raiz do armazenamento.

Para separar a camada de apresentacao da logica da aplicacao, o Kivy tem uma
linguagem propria para definir a interface, chamado kv. a linguagem kv
descreve as propriedades dos objetos e fica em um arquivo com o nome da
aplicacao (sem App) e com a extensao .kv.

Em kv, os nomes de classes definidas pelo desenvolvedor sao referenciados entre
'<' e '>',  e controles sao definidos pelos seus tipos. Funcoes e atributos
podem ser chamados com a sintaxe do pytho. Os atributos são definidos em pares
com o nome do atributo seguido de dois-pontos e o conteudo.

O canvas para o kivy e uma sequencia de instrucoes graficas de alto nivel, que
ele repetira quando houver redesenho do elemtno de tela correspondente.

Alem do Kivy, existem outras solucoes python para portateis, como o QPython, que
prove um ambiente com interpretador e shell.
"""
