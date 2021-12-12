import requests
from bs4 import BeautifulSoup
import json

class Weather_Forecaster:
    def __init__(self, _link, _headers):
        self.link = _link
        self.head = _headers


    def GetWeatherNow(self):
        getNow = BeautifulSoup(self.html,'html.parser')
        now = getNow.find('div', class_='_1HBR _3p4E').text
        return now

    def GetSpeedWind(self):
        getSpeed = BeautifulSoup(self.html,'html.parser')
        speed = getSpeed.find('div', class_='_1lue wind nu4F _1-2z').find('span', class_='_25L5 _11I5').text
        return speed

    @property
    def __GetHtmlFromSite(self):
        get_html = requests.get(self.link, headers=self.head)
        return get_html.content

    html = __GetHtmlFromSite
