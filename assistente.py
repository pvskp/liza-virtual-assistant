from weakref import WeakKeyDictionary
import pyttsx3
import speech_recognition as sr
import time

class Assistant():
    def __init__(self) -> None:
        self.text_to_speech = pyttsx3.init()        
        self.text_to_speech.setProperty('voice', 'mb-br1')
        self.text_to_speech.setProperty('rate', 90)
        self.recognizer = sr.Recognizer()

    def waiting_for_call(self):
        with sr.Microphone(chunk_size=3000) as source:
            audio = self.recognizer.listen(source, phrase_time_limit=2)

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
        with sr.Microphone(chunk_size=3000) as source:
            audio = self.recognizer.listen(source, phrase_time_limit=3)

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

    def falar_bom_dia(self):
        self.text_to_speech.say("Bom dia Paulo")
        time.sleep(0.4)
        self.text_to_speech.say("Como estás")

        self.text_to_speech.runAndWait()

def receber_comando(assistente):
    while True:
        if (assistente.waiting_for_call()):
            print("Fui chamado")
            comando = 'None'
            while comando == 'None':
                comando = assistente.listening()
                print(comando)
                if (comando == "Desligar assistente"):
                    assistente.speak("Desligando assistente")
                    break
                if (comando == "Bom dia"):
                    assistente.falar_bom_dia()

def main():
    assistente = Assistant()
    receber_comando(assistente)

if __name__ == '__main__':
    main()
