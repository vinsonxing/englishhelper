import re

from model.dict.translation_helper import TranslationHelper


class HaiCiTranslationHelper(TranslationHelper):
    def get_pronounce_selector(self):
        return '.word .phonetic bdo'

    def get_pronounce_strip_pattern(self):
        """
        example: [<bdo lang="EN-US">[hʌmp]</bdo>, <bdo lang="EN-US">[hʌmp]</bdo>]

        :return:
        """
        return '(<bdo lang="EN-US">)(.*?)(</bdo>)'

    def get_meaning_selector(self):
        return '.word .dict-basic-ul li'

    def get_meaning_strip_pattern(self):
        """
        example: [<li><span>n.</span><strong>驼背；圆形隆起物；土墩；肿块；碰撞；恼火</strong></li>, ]

        :return:
        """
        return '(<li><span>(.*?)</span><strong>)(.*?)(</strong></li>)'

    def text(self, pattern, html):
        """
        extract text from the last html tags, such as <li>content</li>, in this case content will be returned

        :param pattern:
        :return: content in html
        """
        try:
            m = re.search(pattern, str(html))
            if len(m.groups()) == 4:
                return m.group(2) + m.group(3)
            else:
                return m.group(2)
        except Exception as e:
            return ""
