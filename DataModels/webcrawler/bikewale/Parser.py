__author__ = 'aliHitawala'
from bs4 import BeautifulSoup

class Parser (object):
    def parse(self, html, url):
        dict = {}
        try:
            soup = BeautifulSoup(html, 'html.parser')
            parentDiv = soup.findAll("div", {"class": "grey-bg content-block margin-top15 border-light"})
            for div in parentDiv:
                trElements = div.find_all('tr')
                for t in trElements:
                    thElements = t.find_all('th')
                    tdElements = t.find_all('td')
                    if len(tdElements) == 2 and len(thElements) :
                        for i in range(len(thElements)) :
                            th = thElements[i].string
                            td = tdElements[i].string
                            if td is not None and th is not None:
                                th = th.encode('ascii','ignore')
                                td = td.encode('ascii','ignore')
                            elif th is not None:
                                th = th.encode('ascii','ignore')
                            elif td is not None:
                                td = td.encode('ascii','ignore')
                            dict[th] = td
        except:
                print "Failed for ", url
        return dict
