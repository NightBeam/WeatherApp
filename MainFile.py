from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.window import Window
from WeatherForecaster import Weather_Forecaster
import json
import datetime


Config.set('graphics', 'width', '256')
Config.set('graphics', 'height', '512')
Config.set('graphics', 'resizable', 'false')
Config.write()


class WithDatasWorker():
    def __init__(self,_path, _reading_method):
        self.path = _path
        self.reading_method = _reading_method

    @property
    def OpenFileJson(self, datas=None):
        if(self.reading_method == str('r')):
            with open(str(self.path), "r") as reader:
                htmldatas = json.load(reader)
                return htmldatas
        elif(self.reading_method == str('w')):
            with open(str(self.path), "w") as writer:
                 json.dump(datas, writer)



class WeatherApp(App):
    datasReader = WithDatasWorker('datas.json','r')
    datasWriter = WithDatasWorker('datas.json','w')

    def build(self):
        lo = BoxLayout(orientation='vertical')
        self.a = Label(color=[.41,.69,.93],font_size=(20),pos_hint={'center_x':0.2,'center_y':0.5})
        self.b = Button(text='Узнать', on_press=self.click,background_color=[.41,.69,.93],size_hint=(1,0.3))
        lo.add_widget(self.a)
        lo.add_widget(self.b)
        return lo

    def click(self, event):
        htmldatas = self.datasReader.OpenFileJson
        now = datetime.datetime.now()
        #tomorrow = htmldatas['date']
        #if()

        wF = Weather_Forecaster(htmldatas['links'], htmldatas['headers'][0])
        a1= wF.GetSpeedWind()
        a2= wF.GetWeatherNow()
        self.a.text ='''        {}
        {}'''.format(a1,a2)


WeatherApp().run()
