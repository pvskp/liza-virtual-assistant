import requests
import json
from os import getcwd, path, read
from src.functionalities.read_credentials import *

class OpenWeather():
    def __init__(self,city='Campinas', unit='metric', lang='pt_br') -> None:
        self.city = city
        self.unit = unit
        self.lang = lang
        self.API_KEY = read_credentials('weather')['API_KEY']
        
        self.request_json()
    
    def request_json(self):
        weather_request = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&units={self.unit}&lang={self.lang}&appid={self.API_KEY}')
        self.weather_data = weather_request.json()
    
    def get_weather(self):
        return self.weather_data['weather'][0]['main']
    
    def get_temperature(self):
        return self.weather_data['main']['temp']
