from src.translation.en_br import en_us
from src.translation.pt_br import pt_br


class Translator(object):
    # singleton instance
    instance = None
    # consts
    pt_br_language_option: str = 'pt_br_language_option'
    en_us_language_option: str = 'en_us_language_option'

    @staticmethod
    def get_instance():
        if not Translator.instance:
            Translator.instance = Translator()
        return Translator.instance

    def __init__(self):
        self.lang_data: dict = {
            Translator.pt_br_language_option: pt_br,
            Translator.en_us_language_option: en_us,
        }
        self.lang_option: str = Translator.pt_br_language_option

    def set_language(self, lang_option: str):
        self.lang_option = lang_option

    def translate(self, text_key: str) -> str:
        return self.lang_data[self.lang_option].get(text_key, None)


_: callable = Translator.get_instance().translate
