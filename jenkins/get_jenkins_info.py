import urllib
 
obj = eval(urllib.urlopen("http://byggserver02/api/python").read());
for job in obj['jobs']:
   print job['name']
