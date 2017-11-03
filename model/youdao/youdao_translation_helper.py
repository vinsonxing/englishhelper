from model.translation_helper import TranslationHelper


class YouDaoTranslationHelper(TranslationHelper):

    def get_pronounce_selector(self):
        return '#phrsListTab div.baav .pronounce .phonetic'

    def get_pronounce_strip_pattern(self):
        """
        example: [<span class="phonetic">[hʌmp]</span>, <span class="phonetic">[hʌmp]</span>]

        :return:
        """
        return '(<span class="phonetic">)(.*?)(</span>)'

    def get_meaning_selector(self):
        return '#phrsListTab div.trans-container ul li'

    def get_meaning_strip_pattern(self):
        """
        example: [<li>n. 驼峰；驼背；圆形隆起物</li>, <li>vi. 隆起；弓起；努力；急速行进</li>, <li>vt. 使隆起；使烦恼</li>]

        :return:
        """
        return '(<li>)(.*?)(</li>)'