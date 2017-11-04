from util.jsonhelper import Jsonable

class Translation(Jsonable):

    def __init__(self):
        self.__pronounces = []
        self.__meanings = []
        self.__word = ""

    @property
    def pronounces(self):
        return self.__pronounces

    @pronounces.setter
    def pronounces(self, p):
        self.__pronounces = p

    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, w):
        self.__word = w

    @property
    def meanings(self):
        return self.__meanings

    @meanings.setter
    def meanings(self, m):
        self.__meanings = m

    def append_meaning(self, m):
        self.meanings().append(m)

    def to_json(self):
        j = {}
        j['word'] = self.__word
        j['meanings'] = list(filter(None, self.meanings))
        j['pronounces'] = list(filter(None, self.pronounces))
        return j