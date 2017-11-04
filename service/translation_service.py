from model.querier.youdao.youdao_querier import YouDaoQuerier


class TranslationSerivce():
    def get_querier(self):
        return YouDaoQuerier()

    def query(self, word):
        return self.get_querier().query(word)

    def queryall(self, words):
        return self.get_querier().query(words)
