#!/usr/python3.5
"""
INTERFACE GRAFICA
as interfaces graficas com usuario (GUI, Graphic User Interface) se
popularizaram no ambiente desktop em virtude da facilidade de uso e da
produtividade. Existem hoje muitas bibliotecas disponiveis para a construcao de
aplicacoes gui, tais como gtk+, qt, tk, e wxwidges.

ARQUITETURA
interfaces graficas geralmente utilizam a metafora do desktop, um espaco em duas
dimensoes que e ocupada por janelas retangulares que representam aplicativos,
propriedades ou documentos.
As janelas podem conter diversos tipos de controle (objetos utilizados para
interagir com o usuario ou para apresentar informacoes) e responder de acordo.
Os eventos podem ser resultado da interacao do usuario, como cliques e arrastar
de mouse ou digitacao, ou ainda de eventos de sistema, como relogio da maquina.
A reacao a um evento qualquer e definida por meio de funcoes callback (funcoes
que sao passadas como argumento para outras rotinas).
controles mais usados:
    * rótulos (label) -retangulo que exibe texto
    * caixa de texto (text box) - area de edicao de texto
    * botao (button) - area que pode ser ativada interativamente
    * botao de raio (radio button) - tipo especial de botao com o qual sao formados grupos nos quais apenas um botao pode ser apertado de cada vez.
    * botao de verificacao (check button) - botao que pode ser marcado e desmarcado
    * barras de rolagem (scroll bars) - controles deslizantes horizontais ou verticais, usados para intervalos de valores numericos
    * botao giratorio (spin button) - caixa de texto com dois botoes com setas ao lado que incrementam e descrementam o numero na caixa
    * barra de status (status bar) - barra para exibicao de mensagens geralmente na parte inferior da janela
    * imagem (image) - area para exibicao de imagens
controles podem ter acelaradores (teclas de atalhos) associados a eles.
containers mais usados:
    * barra de menu (menu bar) - sistema de menus, geralmente na parte superiror da janela
    * fixo (fixed) - os objetos permanecem fixos nas mesmas posicoes
    * table (table) - colecao de compartimentos para fixar os objetos, distribuidos em linhas e colunas
    * caixa horizontal (horizontal box) - semelhante a tabela, porem apenas com uma linha
    * caixa vertical (vertical box) -  semelhante a tabela, porem apenas com uma coluna
    * caderno (notebook) - varias areas que podem ser visualizadas uma de cada vez quando selecionadas por meio de abas, geralmente na parte superior
    * barra de ferramentas (toolbar) - area com botoes para acesso rapido aos principais recursos d aplicativo
Para lidar com events de tempo, as interfaces graficas implementam um recurso chamado temporizador (timer) que evoca a funcao callback depois de um certo tempo programado
"""
