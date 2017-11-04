from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from service.translation_service import TranslationSerivce
from util.jsonhelper import JsonHelper

app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False, default=lambda x: x.__dict__))

api = Api(app, prefix="/api/v1")
trans_service = TranslationSerivce()


# subscriber_request_parser = RequestParser(bundle_errors=True)
# subscriber_request_parser.add_argument("name", type=str, required=True, help="Name has to be valid string")
# subscriber_request_parser.add_argument("email", required=True)
# subscriber_request_parser.add_argument("id", type=int, required=True, help="Please enter valid integer as ID")


class Translation(Resource):
    def get(self, word):
        t = trans_service.query(word)
        r = JsonHelper.to_json(t)
        return t, 200


api.add_resource(Translation, '/trans/<string:word>')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
