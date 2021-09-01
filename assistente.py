import pyttsx3
import speech_recognition as sr
import time
import datetime
from number_to_month import convert_number_to_month


class Assistant():
    def __init__(self) -> None:
        self.text_to_speech = pyttsx3.init()        
        self.text_to_speech.setProperty('voice', 'mb-br4')
        self.text_to_speech.setProperty('rate', 50)
        self.recognizer = sr.Recognizer()

    def was_called(self):
        with sr.Microphone(chunk_size=5000) as source:
            audio = self.recognizer.listen(source, phrase_time_limit=4)

        command = 'None'

        try:
            command = self.recognizer.recognize_google(audio,language='pt-br')
        except Exception as listeningError:
            print("Não fui chamado")

        if ('Paulo' in command):
            return True
        else:
            return False

    def listening(self):
        command = "Comando não reconhecido"
        with sr.Microphone(chunk_size=5000) as source:
            audio = self.recognizer.listen(source, phrase_time_limit=4)

        try:
            print("Ouvindo...")
            command = self.recognizer.recognize_google(audio, language='pt-br')
            print(command)

        except Exception as listeningError:
            print(listeningError)
            self.speak("Desculpe, não entendi")
            return "None"

        return command

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
        self.text_to_speech.say("Bom dia Paulo")
        time.sleep(0.4)
        self.text_to_speech.say("Como estás")

        self.text_to_speech.runAndWait()

def receber_comando(assistente):
    while True:
        if (assistente.was_called()):
            print("Fui chamado")
            assistente.speak("Estou ouvindo")
            comando = 'None'
            while comando == 'None':
                comando = assistente.listening()
                if (comando == "Bom dia"):
                    assistente.falar_bom_dia()
                elif ('hora' in comando):
                    assistente.time()
                elif (('data' in comando) or ('dia' in comando)):
                    assistente.date()

def main():
    assistente = Assistant()
    receber_comando(assistente)

if __name__ == '__main__':
    main()
