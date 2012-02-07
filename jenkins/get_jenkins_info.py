import urllib
import sys
 
#obj = eval(urllib.urlopen("http://127.0.0.1:8080/api/python").read());

#obj = eval(urllib.urlopen("http://127.0.0.1:8080/job/remote-behor/8/console/api/python").read());

# obj = eval(urllib.urlopen("http://127.0.0.1:8080/job/remote-behor/8/console/api/python").read());

obj = urllib.urlopen("http://127.0.0.1:8080/job/remote-behor/8/console/")

nisse = obj.read()

# print obj

sys.exit(2)

for job in obj['jobs']:
   print job['url']
   print job['name']
