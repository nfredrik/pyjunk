
# - 150502161930  
#   1284101485
import datetime

def dump(obj):
  for attr in dir(obj):
    print ("obj.{} = {}".format(attr, getattr(obj, attr)))


first = datetime.datetime.fromtimestamp(int("1284101485"))
second = first.strftime('%Y-%m-%dT%H:%M:%SZ')
print(second)
print(first.isoformat())
#print(datetime.datetime.fromtimestamp("150502161930").strftime('%Y-%m-%dT%H:%M:%SZ'))

from dateutil.parser import *

hwlog_ts = "150502161930"

if not hwlog_ts.startswith("20"):
    hwlog_ts = "20" + hwlog_ts

nisse = parse(hwlog_ts)
today = nisse.strftime('%Y-%m-%dT%H:%M:%SZ')
print(today)

print(dump(today))

