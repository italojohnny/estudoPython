#!/usr/python3.5
"""
COMPUTACAO GRAFICA
(GC) e a area da ciencia da computacao que estuda a geracao, a representacao e a
manipulacao de conteudo visual em sistemas computacionais e tem aplicacao em
varias areas do conhecimento humano.
Simulacoes, por exemplo, sao sistemas que empregam calculos matematicos para
imitar um ou mais aspectos de um fenomeno ou processo que existe no mundo real.
Simulacoes permitem entender melhor como o experimento real funciona e verficar
cenarios alternativos com outras condicoes.
Jogos de computador podem ser encarados como uma forma de simulação interativa
que faz uso de recursos visuais para aumentar a sensacao de realismo (conhecida
como imersao) e, com isso, enriquecer a experiencia do jogador.
Outra aplicacao e a visualizacao. Como dizia um antigo ditado popular, "uma
imagem vale por mil palavras", e isso e mais verdadeiro ainda quando e
necessario interpretar grandes quantidades de dados, como acontece em diversas
atividades cientificas, medicas e de engenharia.
Areas como geografia, cartografia e geologia demandam por GIS (Geographic
Information System / Sistemas de informacoes geograficas), que representam
topologias e dados associados, tais como altura, umidade e outros.
A engenharia e atividades afins usam ferramentas CAD (Computer, Aided
Design/Projeto Assistido por computador) para facilitar a criacao de desenhs
tecnicos para componentes ou pecas de maquinaria.
Alem disso, varias formas de arte se beneficiam da cg,como o cinema,
principalmente para a criacao de efeitos especiais. A cg também permitiu o
surgimento de novas formas de arte que usam um ambiente digital como midia,
como, por exemplo, a animacao em tres dimensoes (3d).

MATRIZES VERSUS VETORES
E muito comum representar uma informacao visual em forma bidimensional (2D),
seja em fotos, graficos impressos ou em um monitor. Existem duas formas para a
representacao de imagens bidimensionais amplamente utilizadas, cada qual com
suas vantagens e desvantagens.
A primeira e matricial, tambem conhecida como mapa de bits (bitmap) ou raster,
na qual a imagem e representada como uma matriz bidimensional de pontos com
informacoes sobre cor, chamada de elementos de imagem (picture element,
geralmente abreviado como pixel). Esta forma requer algoritmos sofisticados para
ser manipulada e armazenada, em razao do volume de dados, e a complexidade das
operacoes, como interpolar valores durante um redimensionamento, por exemplo.
A segunda forma de representacao sao as imagens vetoriais, que sao descristas
por meio de entidades matematicas que compoem a geometria da imagem (linhas,
poligonos, texto e outros). Esta forma e menos exigente em termos de recursos
computacionais e nao apresenta problemas associados a redimensionamento, porem
nao permite muitas operacoes que o mapa de bits viabiliza.
Entre outras formas de representacao levaram ao surgimento de varios formatos de
arquivo para armazenamento de imagens, inclusive abertors, como o png (Portable
Network Graphics), que suporta imagens raster, com transparencia inclusive, e o
SVG (Scalable Vectorial Graphics), para imagens vetoriais, mapas de bits e ate
animacoes. Ambos sao homologados pelo w3c (world wide web consortium).
Existem hoje varias bibliotecas voltadas para cg disponiveis em python que estao
em estado avancado de maturidade.
"""
