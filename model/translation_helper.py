import re

class TranslationHelper:

    def get_pronounce_selector(self):
        pass

    def get_pronounce_strip_pattern(self):
        pass

    def get_meaning_selector(self):
        pass

    def get_meaning_strip_pattern(self):
        pass

    def pronounce_text(self, html):
        return TranslationHelper.text(self.get_pronounce_strip_pattern(), html)

    def meaning_text(self, html):
        return TranslationHelper.text(self.get_meaning_strip_pattern(), html)

    @staticmethod
    def text(pattern, html):
        """
        extract text from the last html tags, such as <li>content</li>, in this case content will be returned

        :param pattern:
        :return: content in html
        """
        m = re.search(pattern, str(html))
        return m.group(2)
