__author__ = 'aliHitawala'
import urlparse
import mechanize


url = "http://www.bikewale.com/used/bikes-in-bangalore/"
sub_url = "http://www.bikewale.com/used/bikes-in-bangalore"
br = mechanize.Browser()
urls = [url]
visited = [url]
times = 100
while len(urls)>0:
    if times < 0:
        break
    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl = urlparse.urljoin(link.base_url,link.url)
            if newurl not in visited and sub_url in newurl and '#' not in newurl and 'page' not in newurl:
                visited.append(newurl)
                urls.append(newurl)
                print newurl
    except:
        print "error"
        urls.pop(0)

print visited