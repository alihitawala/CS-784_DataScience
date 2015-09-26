__author__ = 'aliHitawala'
from DataModels.webcrawler.bikewale.ReaderHelper import Helper
from DataModels.webcrawler.bikewale.Validator import Validator
from DataModels.webcrawler.bikewale.Parser import Parser


class Extractor(object):

    def __init__(self):
        self._readerHelper = Helper()
        self._parser = Parser()
        self._validator = Validator()

    def extract(self, fileName):
        return self.extractData(fileName)

    def extractData(self, fileName):
        content = self._readerHelper.readContentFromFile(fileName)
        return self._parser.parse(content, fileName)
