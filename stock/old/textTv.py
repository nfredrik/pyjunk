#!/usr/bin/python
from optparse import OptionGroup, OptionParser
import csv
import urllib
import re
from time import gmtime, strftime

version='1'


#
#  TODO:
#
#  how to save? csv, SQLite?, 
# how to present? http://matplotlib.sourceforge.net/examples/api/date_index_formatter.html
# http://stackoverflow.com/questions/1596684/python-library-to-plot-graph
#
# define main() function in a proper way...
# save to file ala log4cxx?  timestamp file, i.e filename.log_timestamp???
# 
# check with cron-job, howto to it...
#
#
# python lint, beatifier???
#
# save index  555, didner 334, lannebo  435, osv i dict or list?   
#
# put something in to handle exceptions ....
#
#
 

#---------------------------------------------------------------------------

class Logger:

    """Logger class with automatic verbosity checking"""
    OFF   = 0
    # to status console and file
    FATAL = 1
    ERROR = 2
    WARN  = 3
    INFO  = 4
    # to log file only
    DEBUG = 5
    TRACE = 6
    def __init__(self, verbose):
        self.__verbose = verbose
        self.__fh = open( __file__.rstrip('.py').lstrip('./') +'.log', 'awb')

    def int2string(self,level):
        return {self.DEBUG:  'DEBUG',
                  self.TRACE:'TRACE',
                  self.INFO: 'INFO ',
                  self.WARN: 'WARN ',
                  self.ERROR:'ERROR',
                  self.FATAL:'FATAL'
                 }[level]

    def __call__(self, level, msg):
        if level <= self.__verbose:
            if level < self.DEBUG:
               print strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + self.int2string(level) +':   ' +  msg
        self.__fh.write(strftime("%a, %d %b %Y %H:%M:%S ", gmtime()) + self.int2string(level) +':   ' +  msg + '\r\n')

#---------------------------------------------------------------------------

def generate_parser():

  """Generate a command line option parser"""

  description = 'Hi'
  usage = 'usage: %prog [options] version'
  parser = OptionParser(description=description, usage=usage,
                        version='%prog ' + version)

  parser.set_defaults(verbose=0)
  parser.add_option('-v', '--verbose',
                    type='int', dest='verbose',
                    help='enable additional output, specify several times '\
                         'for more information')
  return parser


#---------------------------------------------------------------------------

# 'OMX STOCKHOLM           359.39  -1.45'

class Bors:

    def __init__(self):
        i = 0
    def get_texttv(self):
        self.sock = urllib.urlopen("http://svt.se/svttext/web/pages/202.html")
        return self.sock.read()


    def filter_out(self, html):
        return re.search('OMX STOCKHOLM \(\d\d\:\d\d\)[ \t]*([\d]*\.[\d]*)[ \t]*([+-][\d]*\.[\d]*)', html)

    def getindex(self):
        self.html = self.get_texttv()
        self.irma = self.filter_out(self.html)
        return self.irma.group(1)
    def getdeviation(self):
        self.html = self.get_texttv()
        self.irma2 = self.filter_out(self.html)
        return self.irma2.group(2)

#---------------------------------------------------------------------------

# 'OMX STOCKHOLM           359.39  -1.45'
#title="Senaste NAV" style="width: 40%"><span class="va\
#lue" style="width: 100%">  268,53 SEK</span></span><div style="clear: both;" class="section_separator"></div><h6 class="label" style="width: 50%" title="NAV\
#http://morningstar.se/Funds/Quicktake/Overview.aspx?perfid=0P0000IWH7&programid=0000000000c-datum">NAV-datum<div class="helpbutton" style="display:inline;">

def readline():
    print 'hej'

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

 
#---------------------------------------------------------------------------       
class Log:
   def __init__(self):
       log(Logger.INFO, '%s constructor ' % self.__class__.__name__)
       self.fh = csv.writer(open('eggs.csv', 'awb'), delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)

   def save_index(self, idx):
       log(Logger.DEBUG, '%s save_index() ' % self.__class__.__name__)
       # print strftime("%a, %d %b %Y %H:%M:%S :", gmtime()) , idx
       self.fh.writerow([strftime("%a, %d %b %Y %H:%M:%S :", gmtime()) , idx])
   def __del__(self):
       log(Logger.INFO, '%s destructor ' % self.__class__.__name__)
       

#---------------------------------------------------------------------------
        
# main

