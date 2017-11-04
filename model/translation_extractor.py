from bs4 import BeautifulSoup

from entity.translation import Translation
from model.dict.translation_helper import TranslationHelper


class TranslationExtractor:
    def __init__(self, word, content, helper):
        self.__word = word
        self.__content = content
        if not isinstance(helper, TranslationHelper):
            raise TypeError
        self.__helper = helper
        self.__soup = BeautifulSoup(content, "lxml")

    def get_pronounces(self):
        """
        extract pronounces from give content
        example: [<span class="phonetic">[hʌmp]</span>, <span class="phonetic">[hʌmp]</span>]
        :return: a list contains pronounce in English and American English
        """
        pronounce = self.__soup.select(self.__helper.get_pronounce_selector())

        def convert(p): return self.__helper.pronounce_text(p)

        return list(map(convert, pronounce))

    def get_meanings(self):
        """
        extract meanings from give content
        :return:
        """
        meanings = self.__soup.select(self.__helper.get_meaning_selector())

        def convert(m): return self.__helper.meaning_text(m)

        return list(map(convert, meanings))

    def get_tanslation(self):
        translation = Translation()
        p = self.get_pronounces()
        m = self.get_meanings()
        translation.pronounces = p
        translation.meanings = m
        translation.word = self.__word
        return translation
