__author__ = 'aliHitawala'
import urlparse
import mechanize
from DataModels.webcrawler.Crawler import Crawler
from DataModels.webcrawler.bikewale.ReaderHelper import Helper
from bs4 import BeautifulSoup
import re
from time import sleep
import logging
import Constants as C
import os.path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Started the crawler...')


class BikeWaleCrawler (Crawler):
    def __init__(self, url, subUrl):
        super(BikeWaleCrawler, self).__init__(url, subUrl)
        self.url = url
        self.subUrl = subUrl
        self._readerHelper = Helper()

    def crawlforhtml(self):
        br = mechanize.Browser()
        urls = [self.url]
        visited = [self.url]
        parent_url = self.url
        count = 1
        url_file = open(self._readerHelper.getAbsoluteUrl(C._urls_file_name), 'w')
        while len(urls)>0:
            br.open(urls[0])
            parent_url = urls[0]
            urls.pop(0)
            for link in br.links():
                if count % 10 == 0:
                    sleep(1)
                    count += 1
                try:
                    new_url = urlparse.urljoin(link.base_url,link.url)
                except:
                    logger.error("URL parse exception for parent URL : " + parent_url)
                try:
                    if type(new_url) is str and new_url not in visited and self.subUrl in new_url and ('#' not in new_url or '#city' in new_url):
                        visited.append(new_url)
                        if 'page-' in new_url and 'page-143/' not in new_url and 'page-144/' not in new_url:
                            urls.append(new_url)
                        url_file.write(new_url + "\n")
                        self.populate_html_page_for_url(new_url)
                except:
                    logger.error("Crawling failed for a URL : " + new_url)
                    urls.pop(0)
            logger.info("Page scan completed :: " + parent_url)
        url_file.close()

    def populate_html_pages_for_all_urls(self):
        url_file = open(self._readerHelper.getAbsoluteUrl(C._urls_file_name), 'r')
        for line in url_file:
            self.populate_html_page_for_url(line)
        url_file.close()

    def populate_html_page_for_url(self, url):
        try:
            url = url.strip()
            search = re.search(r"S\d{2}", url)
            if search is None:
                logger.error("URL to html stopped for " + url)
                return
            html_file_name = url.strip().replace("/", "@") + '.html'
            html_file_name = self._readerHelper.getHtmlFileHandle(html_file_name)
            if os.path.isfile(html_file_name):
                logger.info("File exists for " + url.strip())
                return
            content = self._readerHelper.readContentFromUrl(url)
            soup = BeautifulSoup(content, 'html.parser')
            html_file = open(html_file_name, 'w+')
            html_file.write(str(soup))
            html_file.close()
            logger.info("File created for " + url.strip())
        except SystemError:
            logger.error("Exception raised in parsing html for url: " + url.strip())
