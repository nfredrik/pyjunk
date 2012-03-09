import re
import urllib
import time
from threading import Thread


class URLer(object):
    def __init__(self, numbers):
        for number in range(numbers):
            pa = URLAgent('http://dn.se')
            pa.start()

class URLAgent(Thread):
    def __init__(self, host):
        Thread.__init__(self)        
        self.host = host
        self.dict = {}

    def run(self):
        self.url = urllib.urlopen(self.host)
        print time.clock(), self.url.getcode()
#        if self.url.getcode() not in self.dict:
#            self.dict[self.url.getcode] = 1
#        else:
#            self.dict[self.url.getcode]+= 1


if __name__ == '__main__':
    hosts = 25
    URLer(hosts)
