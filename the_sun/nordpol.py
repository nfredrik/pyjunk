from BeautifulSoup import BeautifulSoup
import urllib2
import datetime
import json
import os

JSONFILE = 'data.json'

def load_json(file):
    data = []
    if not os.path.exists(file):
        return data
    
    with open(file, 'rb') as fp:
        data = json.load(fp)
    return data


def save_json(file, data):
    with open(file, 'wb') as fp:    
        json.dump(data, fp)


page=urllib2.urlopen("http://www.nordpoolspot.com")
soup = BeautifulSoup(page.read())
mhw_sek=soup.findAll('td',{'class':'preliminary'})
#print mhw_sek[1]['title']
print "Captured from www.nordpoolspot.com"
print "Spot price:", mhw_sek[1].renderContents(), "SEK/MWh"

data = load_json(JSONFILE)

# Log date and price for SEK/MWh    
data.append({str(datetime.date.today()): str(mhw_sek[1].renderContents())})  

save_json(JSONFILE, data)
 