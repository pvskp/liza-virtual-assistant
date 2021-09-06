import requests
import json
from os import getcwd, path

class OpenWeather():
    def __init__(self,city='Campinas', unit='metric', lang='pt_br') -> None:
        self.city = city
        self.unit = unit
        self.lang = lang

        with open(path.abspath(getcwd())+'/credentials.json', 'r') as credentials:
            d = json.load(credentials)
            self.API_KEY = d['weather']['API_KEY'] 
        
        self.request_json()
    
    def request_json(self):
        weather_request = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&units={self.unit}&lang={self.lang}&appid={self.API_KEY}')
        self.weather_data = weather_request.json()
    
    def get_weather(self):
        return self.weather_data['weather'][0]['main']
    
    def get_temperature(self):
        return self.weather_data['main']['temp']

l = OpenWeather()

print(l.get_weather())