__author__ = 'aliHitawala'
import abc


class Crawler (object):
    def __init__(self, url, subPart):
        self.url = url
        self.subPart = subPart

    @abc.abstractmethod
    def crawlforhtml(self):
        return


class Const(object):
    def QUIKRSEED(self):
        return "http://www.bikedekho.com/used-bikes-in-india?page=10"
    def QUIKRBASE(self):
        return "http://www.bikedekho.com/"

CONST = Const()