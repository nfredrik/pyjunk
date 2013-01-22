from BeautifulSoup import BeautifulSoup
import urllib2
url="http://kaj63.se"
page=urllib2.urlopen(url)
#print page.read()
soup = BeautifulSoup(page.read())

print soup.title
print soup.head

universities=soup.findAll('a',{'class':'institution'})
for eachuniversity in universities:
    print eachuniversity['href']+","+eachuniversity.string
