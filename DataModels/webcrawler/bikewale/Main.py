__author__ = 'aliHitawala'
from DataModels.webcrawler.bikewale.DataExtractor import Extractor
from DataModels.persistence.bikewale.BikeWaleDaoImpl import Dao

if __name__ == '__main__':
    filename = 'html_pages_url'
    __list = []
    urls = []

    def readAllUrls():
        global urls
        f = open(filename, 'r')
        urls = f.readlines()

    readAllUrls()
    instance = Extractor()
    daoInstance = Dao()
    for url in urls:
        dict = instance.extract(url)
        if bool(dict):
            print dict
            daoInstance.populateAndExecute(dict)