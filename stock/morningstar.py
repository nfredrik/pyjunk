import re
import urllib
"""
#title="Senaste NAV" style="width: 40%"><span class="va\
#lue" style="width: 100%">  268,53 SEK</span></span><div style="clear: both;" class="section_separator"></div><h6 class="label" style="width: 50%" title="NAV\
#http://morningstar.se/Funds/Quicktake/Overview.aspx?perfid=0P0000IWH7&programid=0000000000c-datum">NAV-datum<div class="helpbutton" style="display:inline;">
"""

class Morningstar(object):
    def __init__(self,  url):
        self.url = url

    def geturl(self, url):
        self.sock = urllib.urlopen(url)
        self.html = self.sock.read()
        self.sock.close()
#        self.test = readline()
        return self.html

    def senasteNAV(self):
        self.result = self.geturl(self.url)
        self.nav = re.search('Senaste NAV.*\ ([\d]*\,[\d]*)\ SEK[.]*',  self.result)
        return self.nav.group(1).replace(",",".")

    def getLatest(self):
        source = self.getDataSource()
        self.senasteNAV(source)
        self.store()
