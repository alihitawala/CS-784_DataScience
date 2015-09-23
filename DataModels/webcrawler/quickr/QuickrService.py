__author__ = 'shaleen'
from DataModels.webcrawler.quickr import QuickerCrawler
from DataModels.webcrawler.quickr import Parser


class QuickrService:
    _list = []

    def __init__(self):
        self.parser = Parser.Parser()
        self.crawler = QuickerCrawler.QuikrCrawler()

    def readEvalLoop(self):
        self.crawler.generateAllUrls()
        #while not self.crawler.isURLListEmpty:
        self._list.append(self.parser.getAttributesFromHTMLPage(self.crawler.crawlforhtml(), "test"))
        return self._list
