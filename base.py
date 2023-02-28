from plugin import davinci_translate

class Translating:
    def __init__(self, text_to_translate, lang) -> None:

        self.text_to_translate =  text_to_translate
        self.lang = lang

    def traducir(self):
        
        return davinci_translate(
            language = self.lang,
            sentence = self.text_to_translate
        )



