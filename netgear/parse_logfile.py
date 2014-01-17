
import re


import re
import urllib2

def getIP():
    ip_checker_url = "http://checkip.dyndns.org/"
    address_regexp = re.compile ('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    response = urllib2.urlopen(ip_checker_url).read()
    result = address_regexp.search(response)

    if result:
            return result.group()
    else:
            return None
        

PATTERN1='(\[[\w\d\s\(\)\:\.\]]+\]).*'
PATTERN2='(\[[\w\d\s\(\)\:\.\]]+\])[\s]+from[\s]+([\d\.]+)*'
PATTERN3='(\[[\w\d\s\(\)\:\.\]]+\])[\s]+from[\s]+([\d\.]+)[\:\d]+[\s]+to[\s]+([\d\. ]+)\:([\d]+).*'


#[LAN access from remote] from 81.13.90.74:2701 to 10.0.0.101:445, Monday, Jan 06,2014 17:33:57

from_ip_addr = {}

to_port_addr = {}

with open('log.txt') as fh:
    whole = fh.readlines()
    for line in whole:
        test = re.search(PATTERN1,line)
        if test != None:
            pass
            #print test.group(1)
        test = re.search(PATTERN3,line)
        if test != None:
            pass
            #print 'to:', test.group(3), test.group(4)

            if test.group(4) not in to_port_addr:
                to_port_addr[test.group(4)] = 1
            else:
                to_port_addr[test.group(4)] += 1
                      
            if test.group(2) not in from_ip_addr:
                from_ip_addr[test.group(2)] = 1
            else:
                from_ip_addr[test.group(2)] += 1
                

#for ip, times in from_ip_addr.items():
for ip in sorted(from_ip_addr, key=from_ip_addr.get, reverse =True):
    print ip,':', from_ip_addr[ip]
    
for ip in sorted(to_port_addr, key=to_port_addr.get, reverse =True):
    print ip,':', to_port_addr[ip]
    
            