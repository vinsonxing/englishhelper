from model.dict.youdao.youdao_dict_provider import YouDaoDictProvider

from model.dict.youdao.youdao_translation_helper import YouDaoTranslationHelper
from model.querier.querier import Querier

class YouDaoQuerier(Querier):

    def __init__(self):
        super(YouDaoQuerier, self).__init__()
        self.__helper = YouDaoTranslationHelper()
        self.__dict = YouDaoDictProvider()

    def get_dict(self):
        return self.__dict

    def get_translation_helper(self):
        return self.__helper