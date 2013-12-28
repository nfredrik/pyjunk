
import datetime
import urllib2
import re
url="http://www.yr.no/place/Sweden/Stockholm/S%C3%B6dert%C3%A4lje/"
p=urllib2.urlopen(url)
page = p.read()

sunrise = re.search('Sunrise[\s]+([\d]+\:[\d]+)', page)


print "Date:%15s" % datetime.date.today()

if sunrise != None:
    print "Sunrise:%12s"% sunrise.group(1)
    


sunset = re.search('Sunset[\s]+([\d]+\:[\d]+)', page)

if sunset != None:
    print "Sunset:%13s"% sunset.group(1)