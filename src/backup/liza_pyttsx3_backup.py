import pyttsx3
import speech_recognition as sr
import time
import datetime
from number_to_month import convert_number_to_month
import requests
import json
from iot_functions import *

class Liza():
    def __init__(self, VOICE) -> None:
        self.text_to_speech = pyttsx3.init()        
        self.text_to_speech.setProperty('voice', VOICE) #Linux -> 'mb-br4' from mbrola
        self.text_to_speech.setProperty('rate', 50)
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
            self.speak("Desculpe, não entendi")
            return "None"

        return command.lower()

    def speak(self, text):
        self.text_to_speech.say(text)
        self.text_to_speech.runAndWait()

    def time(self):
        now = datetime.datetime.now()
        self.speak(f"Agora são {now.hour} horas e {now.minute} minutos")

    def date(self):
        now = datetime.datetime.now()
        self.speak(f"Hoje é dia {now.day} de {convert_number_to_month(now.month)} de {now.year}")

    def falar_bom_dia(self):
        self.speak("Bom dia Paulo")
        time.sleep(0.4)
        self.speak("Como estás")

    def present_yourself(self):
        self.speak("Meu nome é Liza, fui desenvolvida para um projeto pessoal por Paulo Vinícius")

    def get_dollar_currency(self):
        dollar_currency = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        dollar_currency = dollar_currency.json()
        value_in_reais = dollar_currency['USDBRL']['bid']
        reais = int((float(value_in_reais) // 1))
        centavos = (int((float(value_in_reais) % 1)*100))

        self.speak(f"Atualmente o dólar está valendo {reais} reais e {centavos} centavos")

    def turn_on_ps4(self):
        self.speak('Ok, ligando o PS4')
        start_ps4()
        self.speak("Prontinho o ps4 está ligado")

    def standby_ps4(self):
        self.speak('Colocando PS4 em modo de repouso')
        standby_ps4()