__author__ = 'aliHitawala'
from DataModels.webcrawler.bikewale.DataExtractor import Extractor
from DataModels.persistence.bikewale.BikeWaleDaoImpl import Dao
from DataModels.webcrawler.bikewale.ReaderHelper import Helper

if __name__ == '__main__':
    instance = Extractor()
    daoInstance = Dao()
    readerHelper = Helper()
    for fileName in readerHelper.getAllHtmlFileNames():
        dict = instance.extract(fileName)
        if bool(dict):
            print dict
            daoInstance.populateAndExecute(dict)