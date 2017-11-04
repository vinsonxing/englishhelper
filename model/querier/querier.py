from model.translation_extractor import TranslationExtractor
from model.formatter.default_output_formatter import DefaultOutputFormatter


class Querier:
    def __init__(self):
        self.__formatter = None

    def get_dict(self):
        pass

    def set_formatter(self, f):
        self.__formatter = f

    def get_translation_helper(self):
        pass

    def query(self, words):
        words = self._to_valid_type(words)
        return list(map(self._query, words))

    def query_and_output(self, words):
        words = self._to_valid_type(words)
        for w in words:
            self._query_and_output(w)

    ##### privates #####
    def _query(self, word):
        helper = self.get_translation_helper()
        dict = self.get_dict()
        content = dict.query(word)
        extractor = TranslationExtractor(word, content, helper)
        return extractor.get_tanslation()

    def _to_valid_type(self, w):
        if isinstance(w, str):
            return [w]
        elif isinstance(w, list):
            return w
        else:
            raise TypeError

    def _query_and_output(self, word):
        self._get_formatter().format(self._query(word))

    def _get_formatter(self):
        if self.__formatter is None:
            return DefaultOutputFormatter()
        else:
            return self.__formatter

