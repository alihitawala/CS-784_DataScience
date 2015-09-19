__author__ = 'aliHitawala'
import abc


class Crawler (object):
    def __init__(self, url, subPart):
        self.url = url
        self.subPart = subPart

    @abc.abstractmethod
    def crawlforhtml(self):
        return