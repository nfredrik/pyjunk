from BeautifulSoup import BeautifulSoup
import urllib2

def get_the_prices():
    hours24 = []
    cntr = 0
    page=urllib2.urlopen('http://www.nordpoolspot.com/Market-data1/Elspot/Area-Prices/ALL1/Hourly/')
    soup = BeautifulSoup(page.read())
    mhw_sek=soup.findAll('td',{'align':'right'})
    
    timme24 = [(cntr, float(i.renderContents().replace(',','.'))) for (cntr,i) in enumerate(mhw_sek)
               (cntr % 10 == 3 and len(hours24) < 24)]
    
    print 'timme24', timme24
    
    for i in mhw_sek:
        if (cntr % 10 == 3 and len(hours24) < 24):
            hours24.append(float(i.renderContents().replace(',','.'))) 
        cntr+=1    
    return hours24