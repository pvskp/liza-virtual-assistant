import pyttsx3
import speech_recognition as sr
import time

class Assistant():
    def __init__(self) -> None:
        self.text_to_speech = pyttsx3.init()        
        self.text_to_speech.setProperty('voice', 'mb-br1')
        self.text_to_speech.setProperty('rate', 90)
        self.recognizer = sr.Recognizer()

    def listening(self):
        command = "Comando não reconhecido"
        with sr.Microphone() as source:
            self.recognizer.pause_threshold = 1
            audio = self.recognizer.listen(source)
        try:
            print("Ouvindo...")
            command = self.recognizer.recognize_google(audio, language='pt-br')
            print(command)

        except Exception as listeningError:
            print(listeningError)
            self.speak("Desculpe, não entendi")

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
    ## TODO: ativar modo de escuta apenas quando seu nome for chamado
    while True:
        comando = assistente.listening()
        print(comando)
        if (comando == "Desligar assistente"):
            assistente.speak("Desligando assistente")
            break
        if (comando == "Bom dia"):
            assistente.falar_bom_dia()
        time.sleep(1)

def main():
    assistente = Assistant()
    receber_comando(assistente)

if __name__ == '__main__':
    main()
