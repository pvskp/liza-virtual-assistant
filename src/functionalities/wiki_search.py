import wikipedia

#TODO: lidar com definições em outras línguas da wikipédia

class Wikipedia():
    def __init__(self, language='pt') -> None:
        self.language = language
        wikipedia.set_lang(f'{self.language}')

    def get_summary(self, text):
        try:
            summary = wikipedia.summary(f'{text}')
            return summary[:summary.index('.')] # Retorna o texto somente até o primeiro ponto final.

        except:
            return 'None'