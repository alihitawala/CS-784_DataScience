__author__ = 'shaleen'
import urlparse
import mechanize
from DataModels.webcrawler.Crawler import Crawler
from DataModels.webcrawler.Crawler import CONST


class QuikrCrawler (Crawler):

    setOfUrls = set()

    def __init__(self):
        self.urlList = [CONST.QUIKRSEED()]

    #crawl for urls actually
    def crawlforhtml(self):
        try:
            browser = mechanize.Browser()
            url = self.getNextUrl()
            print url
        except:
            print "Error in generating HTML for url", url
        return browser.open(url).read()

    def generateAllUrls(self):
        browser = mechanize.Browser()
        self.processMechanizeObject(browser)
        urlToParse = self.urlList.pop(0)
        try:
            browser.open(urlToParse)
            for link in browser.links():
                if 'used-bikes-detail' in link.url:
                    self.setOfUrls.add(urlparse.urljoin(CONST.QUIKRBASE(),link.url))
        except:
            print "Error generating all urls"
        return

    def getNextUrl(self):
        return self.setOfUrls.pop()

    def processMechanizeObject(self, browser):
        browser.set_handle_robots(False)
        browser.set_handle_equiv(False)
        browser.set_handle_equiv(True)
        browser.set_handle_redirect(True)
        browser.set_handle_robots(False)
        browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        browser.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36')
                              ,('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
                              ,('Accept-Charset','ISO-8859-1,utf-8;q=0.7,*;q=0.3')
                              ,('Accept-Encoding','none')
                              ,('Accept-Language','en-US,en;q=0.8')
                              ,('Connection','keep-alive')]

    @property
    def isURLListEmpty(self):
        return len(self.setOfUrls) == 0