__author__ = 'aliHitawala'
import urlparse
import mechanize
from DataModels.webcrawler.Crawler import Crawler
from DataModels.webcrawler.bikewale.ReaderHelper import Helper
from bs4 import BeautifulSoup
import re


class BikeWaleCrawler (Crawler):
    def __init__(self, url, subUrl):
        super(BikeWaleCrawler, self).__init__(url, subUrl)
        self.url = url
        self.subUrl = subUrl
        self._readerHelper = Helper()
        self._urls_file_name = 'urls'

    def crawlforhtml(self):
        br = mechanize.Browser()
        urls = [self.url]
        visited = [self.url]
        times = 0
        url_file = open(self._readerHelper.getAbsoluteUrl(self._urls_file_name), 'w')
        while len(urls)>0:
            if times > 10:
                break
            try:
                br.open(urls[0])
                urls.pop(0)
                for link in br.links():
                    newurl = urlparse.urljoin(link.base_url,link.url)
                    if newurl not in visited and self.subUrl in newurl and ('#' not in newurl or '#city' in newurl):
                        visited.append(newurl)
                        urls.append(newurl)
                        url_file.write(newurl + "\n")
                        print newurl
                        times = times + 1
            except:
                print "error"
                urls.pop(0)
            finally:
                url_file.close()
        self.populateHtmlPages()

    def populateHtmlPages(self):
        url_file = open(self._readerHelper.getAbsoluteUrl(self._urls_file_name), 'r')
        for line in url_file:
            try:
                line = line.strip()
                search = re.search(r"S\d{5}", line)
                if search is None:
                    print "WARNING: URL to html stopped for ", line
                    continue
                html_file_name = line.strip().replace("/", "@") + '.html'
                content = self._readerHelper.readContentFromUrl(line)
                soup = BeautifulSoup(content, 'html.parser')
                html_file = open(self._readerHelper.getHtmlFileHandle(html_file_name), 'w+')
                html_file.write(str(soup))
            except SystemError:
                print "ERROR: in url to html file url : " + line.strip()
        url_file.close()

