from BeautifulSoup import BeautifulSoup
import urllib2
import datetime
import json
import os

JSONFILE = 'data.json'

def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]

def std_dev(list):
    def average(s): return sum(s) * 1.0 / len(s)
    
    avg = average(list)
    variance = map(lambda x: (x - avg)**2, list)
    
    import math
    
    return  math.sqrt(average(variance))


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


def get_the_prices():
    hours24 = []
    cntr = 0
    page=urllib2.urlopen('http://www.nordpoolspot.com/Market-data1/Elspot/Area-Prices/ALL1/Hourly/')
    soup = BeautifulSoup(page.read())
    mhw_sek=soup.findAll('td',{'align':'right'})
    for i in mhw_sek:
        if (cntr % 10 == 3 and len(hours24) < 24):
            hours24.append(float(i.renderContents().replace(',','.'))) 
        cntr+=1    
    return hours24

page=urllib2.urlopen('http://www.nordpoolspot.com/Market-data1/Elspot/Area-Prices/ALL1/Hourly/')
soup = BeautifulSoup(page.read())
mhw_sek=soup.findAll('td',{'align':'right'})

print "Captured from www.nordpoolspot.com"
#print "Spot price:", mhw_sek[1].renderContents(), "SEK/MWh"
cntr = 0
hours24 = []
for i in mhw_sek:
    if cntr % 10 == 3 and len(hours24) < 24:
        hours24.append(i.renderContents())
    cntr+=1 

updated=soup.findAll('span')
print updated[-3].renderContents()

print 'Selected SE3 column:' 
cntr = 0   
for h in hours24:
    print 'hour',cntr, ':',  h
    cntr+= 1    
    
print 'max:', max(hours24)  
print 'min:', min(hours24) 
print 'mean:%.2f'% (sum([float(x.replace(',','.')) for x in hours24]) / float(len(hours24)))  
print 'median:', median([float(x.replace(',','.')) for x in hours24] )

nisse = get_the_prices()

print nisse

int_list = [float(x.replace(',','.')) for x in hours24]

print 'stddev:%.2f'% std_dev(int_list)

