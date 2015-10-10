__author__ = 'aliHitawala'
from DataModels.persistence.bikewale.BikeWaleDaoImpl import Dao
from DataModels.webcrawler.bikewale.ReaderHelper import Helper
from bs4 import BeautifulSoup
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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


class Parser(object):
    def parse(self, html, fileName):
        dict = {}
        try:
            soup = BeautifulSoup(html, 'html.parser')
            parentDiv = soup.findAll("div", {"class": "grey-bg content-block margin-top15 border-light"})
            dict['BikeName'] = self.getBikeName(soup)
            dict['City'] = self.getCityName(parentDiv)
            dict['StateCode'] = self.getStateCode(parentDiv)
            dict['URL'] = os.path.splitext(list(os.path.split(fileName))[1])[0].replace("@", "/")
            for div in parentDiv:
                trElements = div.find_all('tr')
                for t in trElements:
                    thElements = t.find_all('th')
                    tdElements = t.find_all('td')
                    if len(tdElements) == 2 and len(thElements) :
                        for i in range(len(thElements)) :
                            th = self.getStringFromSoupElement(thElements[i])
                            td = self.getStringFromSoupElement(tdElements[i])
                            dict[th] = td
        except:
            dict = {}
            logger.error("Parsing failed for file : " + fileName)
        return dict

    def getCityName(self, parentDiv):
        divCityName = parentDiv[0].findAll("div", {"class": "text-highlight"})
        cityStateText = self.getStringFromSoupElement(divCityName[0])
        #this to remove 'For Sale at ' and the last ', ##' state code
        city = cityStateText[11:-4]
        return city

    def getStateCode(self, parentDiv):
        divCityName = parentDiv[0].findAll("div", {"class": "text-highlight"})
        cityStateText = self.getStringFromSoupElement(divCityName[0])
        #this is to extract the state code '##'
        state = cityStateText[-2:]
        return state

    def getBikeName(self, soup):
        bikeNameDiv = soup.find_all("div", class_='grid_8 margin-top10')
        bikeName = self.getStringFromSoupElement(bikeNameDiv[0].h1)
        bikeName = bikeName.replace('Used, ', '')
        return bikeName

    def unicodeToString(self, unicode):
        if unicode is None:
            return unicode
        else:
            return unicode.encode('ascii','ignore')

    def getStringFromSoupElement(self, element):
        str = self.unicodeToString(element.get_text())
        if str is not None:
            str = " ".join(str.split())
        return str

if __name__ == '__main__':
    instance = Extractor()
    daoInstance = Dao()
    readerHelper = Helper()
    for fileName in readerHelper.getAllHtmlFileNames():
        dict = instance.extract(fileName)
        if bool(dict):
            daoInstance.populateAndExecute(dict)
