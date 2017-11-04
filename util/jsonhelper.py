import json

class JsonHelper():
    @staticmethod
    def to_json(j):
        if not isinstance(j, Jsonable):
            raise TypeError
        return json.dumps(j.to_json(), ensure_ascii=False)


class Jsonable(object):

    def __init__(self):
        pass

    """
    Interface, the subclass can must implement the to_json method
    """
    def to_json(self):
        pass