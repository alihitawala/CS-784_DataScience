__author__ = 'aliHitawala'
import urllib
import os
import glob

class Helper(object):
    def __init__(self):
        self._html_directory = 'htmls_delhi/'

    def readContentFromFile(self, fileName):
        f = open(fileName, 'r')
        return f

    def readContentFromUrl(self, url):
        f = urllib.urlopen(url)
        return f

    def getAbsoluteUrl(self, fileName):
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, fileName)
        return abs_file_path

    def getHtmlFileHandle(self, name):
        script_dir = os.path.dirname(__file__)
        rel_path = self._html_directory + name
        abs_file_path = os.path.join(script_dir, rel_path)
        return abs_file_path

    def getAllHtmlFileNames(self):
        return glob.glob(self.getAbsoluteUrl(self._html_directory) + "*.html")

if __name__ == '__main__':
    helper = Helper()
    helper.getAllHtmlFileNames()

