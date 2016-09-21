#!/usr/python3.5
"""
SVG (Scalble Vector Graphics)
e um formato aberto, baseado no xml, que descreve imagens vetoriais, na forma de
estruturas compostas de instrucoes de alto nivel que representam primitivas
geometricas. O formato foi proposto pelo w3c, a entidade que define os padroes
vigentes na internet, como o html e o proprio xml.
arquivos svg podem armazenar varios tipos de informacao vetorial, incluindo
poligonos basicos, que sao representados por linhas que delimitam uma area
fechada, tais como retangulos, elipses e outras formas simples. Alem disso, ele
tambem suporta caminhos (paths), que sao figuras, com preenchimento ou nao,
compostas de linhas e/ou curvas definidas por pontos, que sao codificados por
meio de comandos de um caractere ('L' significa "Line To", por exemplo) e um par
de cordenadas X e Y, o que gera um codigo muito compacto.
Texto Unicode pode ser incluido em um arquivo svg, com efeitos visuais, e a
especificacao inclui tratamento de texto bidirecional, vertical e seguindo
caminhos curvos. O texto pode ser formatado com fontes de texto externas, mas,
para amenizar o problema, existe uma fonte interna, que esta sempre disponivel.
As figuras geometricas, os caminhos e o texto podem ser usados como contornos,
internos ou externos, que podem usar tres tipos de preenchimento:
    * cores solidas, que podem ser opacas ou com transparencia.
    * gradientes, que podem ser lineares ou radiais.
    * padroes, que sao imagens bitmap ou vetoriais que se repetem ao longo do
    objeto.
Tantos os gradientes quantos os padroes podem ser animados.
O svg tambem permite que o autor inclua metadados com informacoes a respeito da
imagem, tais como titulo, descricao e outros, com o objetivo de facilitar a
catalogacao, indexacao e recuperacao dos arquivos.
Todos os compnentes de arquivos svg podem ser lidos e alterados usando scripts
da mesma forma que o html, tendo como padrao a linguagem ECMAscript. A
especificacao tambem preve tratamento de eventos de mouse e teclado, que, junto
de hyperlinks, permite adicionar interatividade aos graficos.
O formato tambem suporta animacao por meio do ecmascript, que pode transformar
os elementos da imagem e temporizar o movimento. Isso tambem pode ser feito por
meio de recursos proprios do svg, usando tags.
Para o svg, filtros sao conjuntos de operacoes graficas que sao aplicadsa a um
determinado grafico vetorial, para produzir uma imagem matricial com o
resultado. Tais operacoes graficas sao chamadas primitivas de filtro, que
geralmente realizam uma forma de processamento de imagem, como, por exemplo, o
efeito Gaussin Blue, e por geram um bitmap com transparencia (padrao rgba) como
sainda, que e gerado novamente se necessario. O resultado de uma primitiva pode
ser usado como entrada para outra primitivas, permitindo a concatenacao de
varias para gerar o efeito desejado.
Cairo e uma biblioteca de codigo abert para geracao de imagens em 2d para varios
formados, inclusive svg, e pycaioro e o projeto que faz interface para o python
com a biblioteca.
"""
# sudo pacman -S python-cairo
from math import pi
from cairo import SVGSurface, Context, Matrix

cores =('#dddddd', '#306090', '#609030', '#906030')
origens = ((350, 650), (650, 650), (500, 350))
raio = 300
largura = 1000
altura = 1000

def web2rgb(cor):
    if cor.startswith('#'):
        cor = cor[1:]
    rgb = (cor[:2], cor[2:4], cor[4:])
    rgb = list(map(lambda x: int(x, 16)/256, rgb))
    return rgb

s = SVGSurface('circulos.svg', largura, altura)
c = Context(s)

m = Matrix(yy=-1, y0=altura)
c.transform(m)

c.save()
c.set_source_rgb(*web2rgb(cores[0]))
c.paint()
c.restore()

for i, o in enumerate(origens):
    c.save()
    c.set_line_width(1.0)
    c.arc(o[0], o[-1], raio, 0, 2 * pi)
    c.stroke_preserve()
    cor = web2rgb(cores[i +1]) +[0.5]
    c.set_source_rgba(*cor)
    c.fill()
    c.restore()

s.write_to_png('circulos.png')
s.finish()
