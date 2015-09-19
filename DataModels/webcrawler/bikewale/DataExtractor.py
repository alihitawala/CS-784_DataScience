__author__ = 'aliHitawala'
from DataModels.webcrawler.bikewale.ReaderHelper import Helper
from DataModels.webcrawler.bikewale.Validator import Validator
from DataModels.webcrawler.bikewale.Parser import Parser


class Extractor(object) :
    __filename = 'html_pages_url'
    __list = []
    def __init__(self):
        self.readAllUrls()
        self._readerHelper = Helper()
        self._parser = Parser()


    def extract(self):
        v = Validator()
        for url in self._urls:
            url = url.strip()
            if v.urlValidator(url):
                self.__list.append(self.extractData(url))
        return self.__list

    def readAllUrls(self):
        f = open(self.__filename, 'r')
        self._urls = f.readlines()

    def extractData(self, url):
        content = self._readerHelper.readContentFromUrl(url)
        return self._parser.parse(content, url)

if __name__ == '__main__':
    instance = Extractor()
    variable = instance.extract()
    print variable