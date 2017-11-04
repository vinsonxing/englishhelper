from entity.translation import Translation


class OutputFormatter:
    def format(self, translations):
        if len(translations) == 0:
            return ""

        if not isinstance(translations[0], Translation):
            raise TypeError

        pass
