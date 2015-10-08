__author__ = 'aliHitawala'
from BikewaleCrawler import BikeWaleCrawler


if __name__ == '__main__':
    url = 'http://www.bikewale.com/used/bikes-in-newdelhi/page-145/'
    subUrl = 'http://www.bikewale.com/used/bikes-in-newdelhi/'
    instance = BikeWaleCrawler(url, subUrl)
    instance.crawlforhtml()