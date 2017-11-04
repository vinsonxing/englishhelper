from model.formatter.output_formatter import OutputFormatter
from entity.translation import Translation

class DefaultOutputFormatter(OutputFormatter):
    def __init__(self):
        pass

    def format(self, translations):
        if isinstance(translations, list):
            for t in translations:
                self._format_one(t)
        elif isinstance(translations, Translation):
            self._format_one(translations)

    def _format_one(self, translation):
        if len(translation.pronounces) == 2:
            pronounce = translation.pronounces[1]
        else:
            pronounce = ""

        print("%s  %s" % (translation.word, pronounce))

        if len(translation.meanings) > 0:
            for m in translation.meanings:
                print(m)
        print("") # print a separated line
