#!/usr/python3.5
"""
MATPLOTLIB
existem varios pacotes de terceiros para a geracao de graficos disponiveis para
pyton, sendo que o mais popular deles eo pylab/matplotlib.
O pacote tem dois modulos principais:
    * matplotlib - modulo que oferece uma abstracao orientada a objetos aos
    recursos do pacote.
    * pylab - modulo que oferece uma coloecao de comandos que se assemlha a
    matlab e e mais adequado para o uso interativo.
"""
from pylab import *
ent = arange(0., 20.1, .1)

# calcula os cossenos da entrada
sai = cos(ent)

# plota a curva
plot(ent, sai)

# texto para o eixo x
xlabel('entrada')

# texto para o eixo y
ylabel('cosseno')

# texto no topo da figura
title('calculo de cossenos')

# ativa a grade
grid(True)

# apresenta a figura resultante na tela
#show()

# outro exemplo
# dados
ent1 = arange(0., 7., .1)
sai1 = cos(ent1)
sai2 = sin(ent1)
dif = sai1 - sai2

# dividea figura em 2 linhas e 1 coluna e seleciona a parte superior
subplot(211)

# plota a curva 
# primeira curva: ent1, sai1, 'bo:'
# segunda curva: ent1, sai2, 'g^-'
plot(ent1, sai1, 'bo:', ent1, sai2, 'g^-')

# cria uma legenda
legend(['cossenos', 'senos'])

# seleciona a parte inferior
subplot(212)
# desenha barras
# eixo x: arange(lend(dif)) +5
# eixo y: dif
# largura das barras: .5
bar(arange(len(dif)) +5, dif, .5, color='#ccbbaa')

# salva a figura
savefig('graf.png')

# o pacote tem funcoes para gerar graficos de barra, linha, dispersao, pizza e
# polar, entre outros.
