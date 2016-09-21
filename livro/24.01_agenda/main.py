#!/usr/python3.5
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.modalview import ModalView
from kivy.storage.jsonstore import JsonStore
from datetime import date, timedelta

color = ([.4, .5, .7, 1],
        [.7, .8, 1., 1],
        [.9, .9, 1., 1],
        [1., .7, .8, 1])
font_size = 35

class Agenda (BoxLayout):
    def __init__ (self, **kwargs):
        super(Agenda, self).__init__(**kwargs)
        self.data = date.today()
        self.orientation = 'vertical'
        self.dados = JsonStore('agenda.json') # armazenamento em formato json
        self.topo = BoxLayout(orientation='horizontal', size_hint=(1, .2)) # tela principal
        self.calendario = GridLayout(cols=7)
        self.anterior = Button(text='<<', background_color=color[0], font_size=font_size)
        self.proximo = Button(text='>>', background_color=color[0], font_size=font_size)
        self.corrente = Label(text = '%02d/%d' % (self.data.month, self.data.year), font_size=font_size, size_hint=(2, 1))
        self.topo.add_widget(self.anterior)
        self.topo.add_widget(self.corrente)
        self.topo.add_widget(self.proximo)
        self.gera_calendario()
        self.add_widget(self.topo)
        self.add_widget(self.calendario)

    def gera_calendario (self):
        self.calendario.clear_widgets()
        data_cursor = date(self.data.year, self.data.month, 1)
        for x in ('D', 'S', 'T', 'Q', 'Q', 'S', 'S'):
            self.data_txt = Label(text=x, color=color[2], font_size=font_size)
            self.calendario.add_widget(self.data_txt)
        if data_cursor.weekday() < 6:
            for x in range(data_cursor.weekday() +1 %7):
                self.data_txt = Label(text='')
                self.calendario.add_widget(self.data_txt)
        while data_cursor.month == self.data.month:
            data = data_cursor.isoformat()
            fundo = color[1] if self.dados.exists(data) and self.dados[data]['tarefas'] else color[0]
            self.tarefa = Button(text= str(data_cursor.day), background_color=fundo, color=color[2], font_size=font_size)
            self.tarefa.bind(on_press=self.tarefas)
            self.calendario.add_widget(self.tarefa)
            data_cursor += timedelta(days = 1)

    def ir_proximo (self, instance):
        if self.data.month == 12:
            self.data = date(self.data.year +1, 1, self.data.day)
        else:
            self.data = date(self.data.year, self.data.month +1, self.data.day)
        self.corrente.text = '%02d%d' % (self.data.month, self.data.year)
        self.gera_calendario()

    def ir_anterior (self, instance):
        if self.data.month == 1:
            self.data = date(self.data.year -1, 12, self.data.day)
        else:
            self.data = date(self.data.year, self.data.month -1, self.data.day)
            self.gera_calendario()

    def tarefas (self, instance):
        self.data = date(self.data.year, self.data.month, int(instance.text))
        janela = ModalView(spacing=10)
        principal = BoxLayout(orientation = 'vertical', spacing=10)
        topo = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, .1))
        lista = GridLayout(cols=1, spacing=10)
        sair = Button(text='x', color=color[2], background_color=color[3], font_size=font_size, size_hint=(.2, 1))
        sair.bind(on_press=janela.dismiss)
        topo.add_widget(sair)
        data = '%02d/%02d/%02d' % (self.data.day, self.data.month, self.data.year)
        topo.add_widget(Label(text=data, color=color[2], background_color=color[0], font_size=font_size, size_hint=(.3, 1)))
        tarefa = TextInput(text='', color=color[2], background_color=color[0], font_size=font_size, size_hint=(.5, 1))
        topo.add_widget(tarefa)
        inclui = Button(text='salvar', color=color[2], background_color=color[0], font_size=font_size, size_hint=(.2, 1))
        topo.add_widget(inclui)

        def tarefa_apaga (instance):
            data = self.data.isoformat()
            tarefas = self.dados[data]['tarefas']
            tarefas.remove(instance.tarefa)
            self.dados[data] = {'tarefas': tarefas}
            tarefa_lista()
        def tarefa_lista ():
            lista.clear_widgets()
            data = self.data.isoformat()
            if data in self.dados and self.dados[data]['tarefas']:
                for t in self.dados[data]['tarefas']:
                    l = Label(text=t, color=color[2], background_color=color[0], font_size=font_size, spacing=10, size_hint=(.9, .1))
                    x = Button(text='x', color=color[2], background_color=color[3], font_size=font_size, spacing=10, size_hint=(120, 120))
                    x.tarefa = t
                    x.bind(on_press=tarefa_apaga)
                    b = GridLayout(rows=1, spacing=10, size_hint_y=None, height=120)
                    b.add_widget(l)
                    b.add_widget(x)
                    lista.add_widget(b)
            else:
                lista.add_widget(Label(text='nenhuma tarefa.', color=color[2], background_color=color[0], font_size=font_size))
        def tarefa_inclui (instance):
            data = self.data.isoformat()
            if tarefa.text.strip():
                tarefas = self.dados[data]['tarefas'] if self.dados.exists(data) else[]
                self.dados[data] = {'tarefas': tarefas}
                tarefa_lista()
            inclui.bind(on_press=tarefa_inclui)
            principal.add_widget(topo)
            tarefa_lista()
            principal.add_widget(lista)
            janela.add_widget(principal)
            janela.open()
class AgendaApp (App):
    def build (self):
        return Agenda()

if __name__ == '__main__':
    AgendaApp().run()
