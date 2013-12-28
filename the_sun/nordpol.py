from BeautifulSoup import BeautifulSoup
import urllib2
page=urllib2.urlopen("http://www.nordpoolspot.com")
soup = BeautifulSoup(page.read())
mhw_sek=soup.findAll('td',{'class':'preliminary'})
#print mhw_sek[1]['title']
print "Captured from www.nordpoolspot.com"
print "Spot price:", mhw_sek[1].renderContents(), "SEK/MWh"
