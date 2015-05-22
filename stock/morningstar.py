from stockStuff import stockStuff
from dictionary import dict
import re
#import urllib.request  as request
import requests
"""
#title="Senaste NAV" style="width: 40%"><span class="va\
#lue" style="width: 100%">  268,53 SEK</span></span><div style="clear: both;" class="section_separator"></div><h6 class="label" style="width: 50%" title="NAV\
#http://morningstar.se/Funds/Quicktake/Overview.aspx?perfid=0P0000IWH7&programid=0000000000c-datum">NAV-datum<div class="helpbutton" style="display:inline;">
"""

class Morningstar(object):
    def __init__(self,  dname={}):
        #stockStuff.__init__(self)
        self.name = self.nisse(dname.keys())
        self.url = self.nisse(dname.values())
        #print ("HejHej", self.url)

    def nisse(self, v):
        for i in v:
            return i

    def __str__(self):
        return "%s" % self.name


    def geturl(self, url):
        #self.sock = request.urlopen(url)
        self.sock = requests.get(url)
        self.html = self.sock.text
        self.sock.close()
#        self.test = readline()
        return self.html

    def senasteNAV(self):
        self.result = self.geturl(self.url)
        #print(self.result)
        self.nav = re.search('Senaste NAV.*\ ([\d]*\,[\d]*)\ SEK[.]*',  self.result)
        return self.nav.group(1).replace(",",".")

    def getLatest(self):
        source = self.getDataSource()
        self.senasteNAV(source)
        self.store()
