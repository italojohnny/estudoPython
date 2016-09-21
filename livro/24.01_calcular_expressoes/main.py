#!/usr/python3.5
# exemplo de calcular expressoes
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class CalcForm (BoxLayout):
    def callback (self):
        try:
            self.resultado.text = str(eval(self.formula.text))
        except:
            self.resutado.text = '-'

class CalcApp (App):
    def build (self):
        return CalcForm()

if __name__ == '__main__':
    CalcApp().run()
