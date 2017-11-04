from model.dict.haici.haici_translation_helper import HaiCiTranslationHelper

from model.dict.haici.haici_dict_provider import HaiCiDictProvider
from model.querier.querier import Querier


class HaiCiQuerier(Querier):
    def __init__(self):
        super(HaiCiQuerier, self).__init__()
        self.__helper = HaiCiTranslationHelper()
        self.__dict = HaiCiDictProvider()

    def get_dict(self):
        return self.__dict

    def get_translation_helper(self):
        return self.__helper
