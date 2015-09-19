__author__ = 'aliHitawala'


class Validator(object) :
    def urlValidator(self, url):
        return 'http://www.bikewale.com/used/bikes-in-bangalore/' in url and '#' not in url