import rrdtool
import sys
import os 
import time
from ftplib import FTP


class myFTP(object):
    
    def __init__(self, site, usr, pwd):
        self.ftp =  FTP(site)
        self.ftp.login(user=usr, passwd=pwd)

    def upload(self, file):
        self.ftp.storbinary('STOR ' + file, open(file, 'rb'))
        
    def __del__(self):
        self.ftp.quit()
        

class bahnHof(object):
    def __init__(self):
        self.bahnhof = myFTP('privat.bahnhof.se', 'wb177225', '94e6a11d6')        

    def upload(self,file):
        self.bahnhof.upload(file)
        

def main(args):
    netpng ="net.png"
    # Check if a hour has past
    now = time.time()
    one_hour_ago = now - 60*60
    
    if True == True:       
        ret = rrdtool.graph( net.png, "--start", "-1d", "--vertical-label=milliseconds",
                                 "DEF:inoctets=test1.rrd:input:AVERAGE",
                                 "DEF:outoctets=test1.rrd:output:AVERAGE",
                                 "AREA:inoctets#00FF00:In traffic",
                                 "LINE1:outoctets#0000FF:Out traffic\\r",
                                 "CDEF:inbits=inoctets,8,*",
                                 "CDEF:outbits=outoctets,8,*",
                                 "COMMENT:\\n",
                                 "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",
                                 "COMMENT:  ",
                                 "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps\\r",
                                 "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
                                 "COMMENT: ",
                                 "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps\\r")
            
        if ret:
               print rrdtool.error()
               sys.exit(42)
               
        
        # Put the files in my new site
        try:
            bahnhof = bahnHof()
            bahnhof.upload(netpng)
        except:
            pass


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))
