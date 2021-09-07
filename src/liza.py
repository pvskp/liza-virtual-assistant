from sys import setdlopenflags
import speech_recognition as sr
import time
import datetime
import requests
import json
from os import system as execute

from src.functionalities.iot_functions import *
from src.functionalities.number_to_month import convert_number_to_month
from src.functionalities.dollar_currency import get_currency
from src.functionalities.weather import OpenWeather
from src.functionalities.wiki_search import Wikipedia

class Liza():
    def __init__(self, voice='mb-br4', rate=110, locale='Campinas') -> None:
        self.locale = locale
        self.voice = voice
        self.rate = rate
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 1200 # Sensibilidade do microfone
        self.recognizer.dynamic_energy_threshold = False

    def was_called(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        command = 'None'

        try:
            command = self.recognizer.recognize_google(audio,language='pt-br')
        except Exception:
            print("Não fui chamado")

        if ('Lisa' in command):
            return True

        else:
            return False

    def speak(self, text):
        execute(f'espeak -s {self.rate} -v {self.voice} "{text}"')


    def listening(self):
        command = "Comando não reconhecido"
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        try:
            print("Ouvindo...")
            command = self.recognizer.recognize_google(audio, language='pt-br')
            print(command)

        except Exception as listeningError:
            print(listeningError)
            self.speak("Desculpe não entendi")

            return 'None'

        return command.lower()

    def time(self):
        now = datetime.datetime.now()
        self.speak(f"Agora são {now.hour} horas e {now.minute} minutos")

    def date(self):
        now = datetime.datetime.now()
        self.speak(f"Hoje é dia {now.day} de {convert_number_to_month(now.month)} de {now.year}")

    def falar_bom_dia(self):
        self.speak("Bom dia Paulo")
        time.sleep(0.4)
        self.speak("Como está")

    def present_yourself(self):
        self.speak("Meu nome é Liza, fui desenvolvida para um projeto pessoal por Paulo Vinícius")

    def get_dollar_currency(self):
        reais, centavos = get_currency()

        self.speak(f"Atualmente o dólar está valendo {reais} reais e {centavos} centavos")

    def turn_on_ps4(self):
        self.speak('Ok, ligando o PS4')
        start_ps4()
        self.speak("Prontinho o ps4 está ligado")

    def standby_ps4(self):
        self.speak('Colocando PS4 em modo de repouso')
        standby_ps4()

    def weather(self):
        info = OpenWeather(city=self.locale)
        weather = info.get_weather()
        temp = info.get_temperature()

        if (weather == 'Clear'):
            self.speak(f"Em {self.locale} o clima está limpo e a temperatura é de aproximadamente {temp:.0f} graus celsius")
        
        else:
            self.speak("Me desculpe, ainda não sei identificar o tempo nestas condições")

    def wikipedia_search(self):
        question = self.listening()

        if (question == 'None'):
            return 'None'

        self.speak('Só um minuto')
        wiki = Wikipedia()
        answer = wiki.get_summary(f'{question}')
        
        if (answer != 'None'):
            self.speak(answer)

            return answer
        
        else:
            self.speak('Sua busca foi complexa demais tente novamente')
            return 'None'

