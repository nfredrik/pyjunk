
# http://www.yr.no/place/Sweden/Stockholm/Stockholm/

from BeautifulSoup import BeautifulSoup
import urllib2
url="http://www.yr.no/place/Sweden/Stockholm/Stockholm/"
page=urllib2.urlopen(url)
#print page.read()
page = page.read()
soup = BeautifulSoup(page)
txt =soup.findAll(text="Sunrise")
print  'number one:', txt
#print soup.prettify()
sunset=soup.findAll('td',{'class':'txt-left yr-table-cell-border-left'})
#print 'sunset', sunset
#print 'type', type(sunset)

sunrise=soup.findAll('td',{'class':'txt-left'})
#for n in sunrise:
#    print "###", n

 

nsata = soup.findAll(lambda tag: len(tag.attrs) == 0)
#print "nsata:", nsata
    
import re
#nisse = soup.findAll(re.compile('Sunset[\s]+[\d]+\:[\d]+'))
nisse = soup.findAll(re.compile('Sunset'))
#print nisse
print 'the end'

print soup.head.title

sunrise = re.search('Sunrise[\s]+([\d]+\:[\d]+)', page)

if sunrise != None:
    print sunrise.group(1)
    


janne = re.search('Sunset[\s]+([\d]+\:[\d]+)', page)

if janne != None:
    print janne.group(1)
    