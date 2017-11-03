import urllib.request as u_request
import urllib.parse

class DictProvider:

    def __init__(self, baseurl):
        self.__base_url = baseurl

    def get_translation_selector(self):
        pass

    def query(self, word):
        url = self.__base_url + word
        url = urllib.parse.quote(url, '~@#$&()*!+=:;,.?/\'')
        content = u_request.urlopen(url).read()
        return content

    def get_pronounce_selector(self):
        """
        each dict provider should have its own css selector for pronounce
        :return:
        """
        pass

    def get_meaning_selector(self):
        """
        each dict provider should have its own css selector for translation
        :return:
        """
        pass
