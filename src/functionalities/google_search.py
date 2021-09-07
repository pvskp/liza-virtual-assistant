import requests
import json
from os import path, getcwd

class OnlineSearch():
    def __init__(self, geolocation_parameter='pt-BR', country_parameter='countryBR') -> None:
        self.request_json()
        self.API_KEY = self.google_credentials['API_KEY']
        self.SEARCH_ENGINE_ID = self.google_credentials['search_id']
        self.geolocation_parameter = geolocation_parameter
        self.country_parameter = country_parameter


    def request_json(self):
        with open(path.abspath(getcwd())+'/credentials.json') as credentials:
            d = json.load(credentials)
            self.google_credentials = d['google_search']
    
    def google_seach(self, text):
        text = text.replace(' ', '+')
        search = requests.get(f'https://customsearch.googleapis.com/customsearch/v1?key={self.API_KEY}&cx={self.SEARCH_ENGINE_ID}&g1={self.geolocation_parameter}&cr={self.country_parameter}&q={text}')
        return search.json()

    #TODO: implementar quick-search com web scrapping do google.
