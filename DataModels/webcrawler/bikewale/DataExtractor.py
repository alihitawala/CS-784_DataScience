__author__ = 'aliHitawala'
from DataModels.webcrawler.bikewale.ReaderHelper import Helper
from DataModels.webcrawler.bikewale.Validator import Validator
from DataModels.webcrawler.bikewale.Parser import Parser


class Extractor(object):

    def __init__(self):
        self._readerHelper = Helper()
        self._parser = Parser()
        self._validator = Validator()

    def extract(self, url):
        if self._validator.urlValidator(url):
            return self.extractData(url)
        print "ERROR:: Validation error!! URL: ", url
        return None

    def extractData(self, url):
        content = self._readerHelper.readContentFromUrl(url)
        return self._parser.parse(content, url)
