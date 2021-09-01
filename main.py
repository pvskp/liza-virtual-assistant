from assistente import Liza

VOICE = 'mb-br4'

def receber_comando(assistente):
    while True:
        if (assistente.was_called()):
            print("Fui chamado")
            assistente.speak("Estou ouvindo")
            comando = 'None'
            while (comando == 'None'):
                comando = assistente.listening()
                if (comando == 'bom dia'):
                    assistente.falar_bom_dia()
                elif ('hora' in comando):
                    assistente.time()
                elif (('data' in comando) or ('que dia' in comando)):
                    assistente.date()
                elif (('apresente' in comando) or ('quem é você') in comando):
                    assistente.present_yourself()
                elif (('cotação' in comando) and ('dólar' in comando)):
                    assistente.get_dollar_currency()
                elif (('liga' in comando) and ('ps4' in comando)):
                    assistente.turn_on_ps4()

def main():
    assistente = Liza(VOICE)
    receber_comando(assistente)

if __name__ == '__main__':
    main()
