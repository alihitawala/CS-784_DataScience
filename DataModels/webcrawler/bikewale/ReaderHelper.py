__author__ = 'aliHitawala'
import urllib

class Helper(object):
    def readContentFromUrl(self, url):
        f = urllib.urlopen(url)
        return f