#!/usr/python3.5
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from cmath import *

color = ([.4, .5,.7, 1], [.7, .8, .1, 1], [.95, .98, 1, 1], [1, .7, 1])

class CalculadoraForm (GridLayout):
    def __init__ (self, **kwargs):
        super(CalculadoraForm, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        self.padding = [10, 10, 10, 10]
        self.spacing = [10, 10]
        self.resultado = Label(text='', font_size=25, color=color[2], size_hint_y=.5)
        self.add_widget(self.resultado)
        self.nums = []
        self.pad = GridLayout(cols=4, rows=7, spacing=[3, 3])

        def callback (instance):
            if instance.text == '=':
                self.resultado.text = str(eval(self.resultado.text))
            elif instance.text == 'C':
                self.resultado = ''
            elif instance.text == 'X':
                if self.resultado.text:
                    self.resultado.text = self.resultado.text[:-1]
            else:
                self.resultado.text += instance.text

        lista_botoes = ('(', ')', 'C', 'X', 'sin', 'cos', 'tan', 'abs', 'e', 'j', 'sqrt', 'log', '7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '.', '0', '=', '/')
        for x in lista_botoes:
            self.nums.append(Button(text=x, font_size=35, color=color[2]))
            if x.isdigit():
                self.nums[-1].background_color=color[1]
            elif x == 'C' or x == 'X':
                self.nums[-1].background_color=color[3]
            else:
                self.nums[-1].color = color[2]
                self.nums[-1].background_color=color[0]
            self.nums[-1].bind(on_press=callback)
            self.pad.add_widget(self.nums[-1])
        self.add_widget(self.pad)

class CalculadoraApp (App):
    def build (self):
        Window.clearcolor=(.1, .1, .1, 1)
        return CalculadoraForm()

if __name__ == '__main__':
    CalculadoraApp().run()
