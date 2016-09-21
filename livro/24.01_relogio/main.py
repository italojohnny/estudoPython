#!/pyhton3.5
# sudo pacman -Ss kivy
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import datetime

class RelogioApp (App):
    def build (self):
        def my_callback (dt):
            now = datetime.datetime.now()
            self._txt = '%02d:%02d:%02d' % (now.hour, now.minute, now.second)
            self.txt.text = self._txt
        Clock.schedule_interval(my_callback, 1/10.)
        self.txt = Label(text='')
        self.txt.font_size = 60
        return self.txt

if __name__ == '__main__':
    RelogioApp().run()
