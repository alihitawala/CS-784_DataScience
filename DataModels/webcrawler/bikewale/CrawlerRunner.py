__author__ = 'aliHitawala'
from BikewaleCrawler import BikeWaleCrawler


if __name__ == '__main__':
    url = 'http://www.bikewale.com/used/bikes-in-mumbai/page-1/'
    subUrl = 'http://www.bikewale.com/used/bikes-in-mumbai/'
    instance = BikeWaleCrawler(url, subUrl)
    instance.crawlforhtml()