from DataModels.webcrawler.quickr import QuickerCrawler, QuickrService
from DataModels.webcrawler.quickr import Parser
__author__ = 'shaleen'


if __name__ == "__main__":
    service = QuickrService.QuickrService()
    print service.readEvalLoop()
