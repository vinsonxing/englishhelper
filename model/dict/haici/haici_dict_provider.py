from model.dict.dict_provider import DictProvider
from model.dict.haici.haici_translation_helper import HaiCiTranslationHelper


class HaiCiDictProvider(DictProvider):

    def __init__(self):
        super(HaiCiDictProvider, self).__init__('http://dict.cn/')
        self.__selector = HaiCiTranslationHelper()

    def get_translation_selector(self):
        return self.__selector

