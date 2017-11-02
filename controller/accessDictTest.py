import urllib.request
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
# install Scrapy : pip install Scrapy

YOUDAO_ULR = "http://dict.youdao.com/w/"
word = "turn out"
url = YOUDAO_ULR + word
content = urllib.request.urlopen(url).read()
print(content)
sel = Selector(text=html)
rawCont = sel.xpath("//div[@class='c-abstract']")
