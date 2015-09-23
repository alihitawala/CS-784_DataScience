__author__ = 'shaleen'
from bs4 import BeautifulSoup
import re

class Parser :

    def getAttributesFromHTMLPage(self,html,url):
        dict = {}
        soup = BeautifulSoup(html, 'html.parser')
        for div in soup.findAll('div', attrs={'class':'indisplay'}):
            #print div.parent.parent.attrs
            self.processTopLevelName(div, dict)
            #print div.text
            self.processDetails(soup.findAll('div', attrs={'class':'usedwbox'}),dict)
        self.processLocation(soup.findAll('div', attrs={'class':'dateused'}), dict)
        self.processPrice(soup.findAll('div', attrs={'class':'usedprice1'}), dict)
        return dict

    def processLocation(self, list, dict):
        #print list[0].text
        str = re.search('^[a-zA-Z]+[^\|]',list[0].text).group()
        #print str
        dict['CityPosted'] = str.encode('ascii','ignore')
        return

    def processPrice(self, list, dict):
        dict['Price'] = list[0].text.encode('ascii','ignore').replace('`','').replace(',','')
        return



    def processDetails(self,list , dict):
        for div in list:
            #print div.findAll('div', attrs={'class':'usedR'})[0].text.encode('ascii','ignore').replace(' ','').replace('\n','').replace('`','')
            dict[div.findAll('div', attrs={'class':'usedl'})[0].text.encode('ascii','ignore').replace(' ','').replace('\n','').replace('`','').replace('*','').replace(',','')] = div.findAll('div', attrs={'class':'usedR'})[0].text.encode('ascii','ignore').replace(' ','').replace(',','').replace('\n','').replace('`','')
        return

    def processTopLevelName(self,div,dict):
        if(div.parent.parent.attrs['class'][0] == 'usedleft'):
            #print div.text.encode('ascii','ignore')
            dict['BikeName'] = div.text.encode('ascii','ignore').replace('\n','')
        if(div.parent.parent.attrs['class'][0] == 'usedaboutleft'):
            #print div.text.encode('ascii','ignore').replace('About ','').replace('\n','')
            dict['BikeCompany'] = div.text.encode('ascii','ignore').replace('About','').replace('\n','')
        if(div.parent.parent.attrs['class'][0] == 'usedaboutleft'):
            #print div.text.encode('ascii','ignore').replace('About ','').replace('\n','')
            dict['BikeCompany'] = div.text.encode('ascii','ignore').replace('About','').replace('\n','')
        return