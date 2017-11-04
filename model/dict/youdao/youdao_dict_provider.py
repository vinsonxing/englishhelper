from model.dict.dict_provider import DictProvider
from model.dict.youdao.youdao_translation_helper import YouDaoTranslationHelper


class YouDaoDictProvider(DictProvider):

    def __init__(self):
        super(YouDaoDictProvider, self).__init__('http://dict.youdao.com/w/')
        self.__selector = YouDaoTranslationHelper()

    def get_translation_selector(self):
        return self.__selector

