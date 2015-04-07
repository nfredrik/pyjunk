import urllib.request  as request
import requests
import re

index, deviation = 1,2

class Bors(object):



    def __init__(self):
        pass

    def get_texttv(self):
        """
        Fetch information from text-tv's excellent webpage
        """
        self.sock = requests.get("http://svt.se/svttext/web/pages/202.html")
        return self.sock.text


    def filter_out(self, html):
        """
        Catch two groups in the stream, first index, then deviation
        """
        return re.search('OMX STOCKHOLM \(\d\d\:\d\d\)[ \t]*([\d]*\.[\d]*)[ \t]*([+-][\d]*\.[\d]*)', html)

    def getindex(self):
        """
        Get the index of the grouping
        """
        self.html = self.get_texttv()
        #print (self.html)
        self.irma = self.filter_out(self.html)
        return self.irma.group(index)
    def getdeviation(self):
        """
        Get the devation of the grouping
        """
        self.html = self.get_texttv()
        self.irma2 = self.filter_out(self.html)
        return self.irma2.group(deviation)
