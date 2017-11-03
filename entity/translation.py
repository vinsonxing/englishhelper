from util.jsonhelper import Jsonable

class Translation(Jsonable):

    def __init__(self):
        self.__pronounces = []
        self.__meanings = []

    @property
    def pronounces(self):
        return self.__pronounces

    @pronounces.setter
    def pronounces(self, p):
        self.__pronounces = p

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
        j['meanings'] = self.meanings
        j['pronounces'] = self.pronounces
        return j