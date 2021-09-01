from time import process_time_ns
from assistente import Liza

VOICE = 'mb-br4'

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
                elif (('apresente' in comando) or ('quem é você') in comando):
                    assistente.present_yourself()

def main():
    assistente = Liza(VOICE)
    receber_comando(assistente)

if __name__ == '__main__':
    main()
