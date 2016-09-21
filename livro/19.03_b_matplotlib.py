#!/usr/python3.5
import os
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg

def pie (filename, labels, values):
    '''Gera um diagrama de pizza e salva em arquivo'''
    # use a biblioteca anti-grain geometru
    matplotlib.use('Agg')

    # cores personalizadas
    colors = ['seagreen', 'lightslategray', 'lavender', 'khaki', 'burlywood', 'crnflowerblue']

    # altera as opcoes padrao
    matplotlib.rc('patch', edgecolor='#406785', linewidth=1, antialiased=True)

    # altera as dimensoes da imagem
    matplotlib.rc('figure', figsize=(8., 7.))

    # inicializa a figura
    fig = Figure()
    fig.clear()
    axes = fig.add_subplot(111)

    if values:
        # diagrama
        chart = axes.pie(values, colors=colors, autopct='%2.0f%%')

        # legenda
        pie_legend = axes.legend(labels)
        pie_legend.pad = 0.3

        # altera o tamanho da fonte
        for i in range(len(chart[0])):
            chart[-1][i].set_fontsize(12)
            pie_legend.texts[0].set_fontsize(10)
    else:
        # mensagem de erro: Desliga diagrama
        axes.set_axis_off()

        # mostra a mensagem
        axes.text(0.5, 0.5, 'Sem dados', 
                horizontalalignment='center',
                  verticalalignment='center', fontsize=32, color='#6f7c8c')

    # salva figura
    canvas = FigureCanvasAgg(fig)
    canvas.print_figure(filename, dpi=600)

if __name__ == '__main__':
    pie('fig1.png', [], [])
    pie('fig2.png', ['A', 'B', 'C', 'D', 'E'], [6.7, 5.6, 4.5, 3.4, 2.3])

