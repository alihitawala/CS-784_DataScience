__author__ = 'aliHitawala'
from BikewaleCrawler import BikeWaleCrawler


if __name__ == '__main__':
    url = 'http://www.bikewale.com/used/bikes-in-bangalore/#city=2&dist=500'
    subUrl = 'http://www.bikewale.com/used/bikes-in-bangalore/'
    instance = BikeWaleCrawler(url, subUrl)
    instance.crawlforhtml()