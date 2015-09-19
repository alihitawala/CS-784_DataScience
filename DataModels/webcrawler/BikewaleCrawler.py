__author__ = 'aliHitawala'
import urlparse
import mechanize
import Crawler


class BikeWaleCrawler (Crawler):
    def __init__(self, url, subUrl):
        self.url = url
        self.subUrl = subUrl

    def crawlforhtml(self):
        br = mechanize.Browser()
        urls = [self.url]
        visited = [self.url]
        times = 100
        while len(urls)>0:
            if times < 0:
                break
            try:
                br.open(urls[0])
                urls.pop(0)
                for link in br.links():
                    newurl = urlparse.urljoin(link.base_url,link.url)
                    if newurl not in visited and self.subUrl in newurl and '#' not in newurl:
                        visited.append(newurl)
                        urls.append(newurl)
                        print newurl
            except:
                print "error"
                urls.pop(0)
        print visited
