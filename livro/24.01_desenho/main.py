#!/usr/python3.5
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import *
# codigo ainda com falhas para corrigir

cores_hex = [
        'FF9E73', 'FF7B40', 'FF4F00', 'BF5D30', 'A63400',
        'FFD473', 'FFC540', 'FFB100', 'BF9430', 'A67300',
        '67E467', '39E444', '00C90D', '26972D', '008209',
        '64AAD0', '3C9DD0', '086CA2', '235B79', '034569',
        '717DD7', '4B5CD7', '1729B0', '2E3884', '081472',
        '926CD6', '7945D6', '4811AE', '492A82', '2C0571',
        'FF7673', 'FF4540', 'FF0700', 'BF3330', 'A60400',
        'FFFFFF', '999999', '000000'

        ]

def hex2rgb (cor):
    cor = cor.lstrip('#')
    return (int(cor[:2], 16)/255., int(cor[2:4], 16)/255., int(cor[:4], 16)/255., 1.)

cores = [hex2rgb(cor) for cor in cores_hex]

class DesenhoWidget (Widget):
    def on_touch (self, touch):
        with self.canvas:
            Color(*self.cor, mode='rgba')
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.brush)

    def on_touch_move (self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]

class DesenhoApp (App):
    def build(self):
        tela = BoxLayout(orientation='horizontal')
        controles = BoxLayout(orientation='vertical', size_hint=[.1, 1.])
        palheta = GridLayout(cols=2, spacing=0)

        def define_cor (instance):
            desenho.cor = list(instance.background_color)
            desenho.cor[-1] = .6
            limpara.color = desenho.cor
            limparb.color = desenho.cor

        for cor in cores:
            cw = Button(text=' ', background_color=cor, background_normal='')
            cw.bind(on_press=define_cor)
            palheta.add_widget(cw)

        desenho = DesenhoWidget()
        desenho.cor = list(cores[0])
        desenho.cor[-1] = .6
        desenho.brush = 5.
        tela.add_widget(desenho)
        limpara = Button(text='X', background_color=(0., 0., 0., 1.), color=desenho.cor, background_normal='')
        palheta.add_widget(limpara)

        limparb = Button(text='X', background_color=(1., 1., 1., 1.), color=desenho.cor, background_normal='')
        palheta.add_widget(limparb)
        controles.add_widget(palheta)
        tela.add_widget(controles)

        def limpar1 (obj):
            desenho.canvas.clear()
        limpara.bind(on_release=limpar1)

        def limpar2 (obj):
            with desenho.canvas:
                Color(1., 1., 1., 1., mode='rgba')
                Rectangle(pos=desenho.pos, size=desenho.size)
        limparb.bind(on_release=limpar2)
        return tela

if __name__ == '__main__':
    DesenhoApp().run()

