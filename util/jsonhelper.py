import json


class JsonHelper():
    @staticmethod
    def to_json(j):
        return json.dumps(j, ensure_ascii=False, default=lambda x: x.__dict__)
