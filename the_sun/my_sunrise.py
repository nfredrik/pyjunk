import datetime 
from sunrise import *
s = sun(lat=59.2,long=17.6)  
print 'sunrise at:', s.sunrise(when=datetime.now(tz=LocalTimezone()))  
print 'sunset at:', s.sunset(when=datetime.now(tz=LocalTimezone()))  