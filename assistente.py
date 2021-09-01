import pyttsx3
import speech_recognition


class Assistant():
    def __init__(self) -> None:
        self.text_to_speech = pyttsx3.init()        
        self.text_to_speech.setProperty('voice', 'mb-br4')
        self.text_to_speech.setProperty('rate', 100)


    def speak(self, text):
        self.text_to_speech.say(text)
        self.text_to_speech.runAndWait()

    def falar_bom_dia(self):
        self.text_to_speech.say("Bom dia, Paulo!")
        self.text_to_speech.runAndWait()


def main():
    assistente = Assistant()
    assistente.falar_bom_dia()

main()
