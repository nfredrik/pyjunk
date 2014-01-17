import sys
from savejson import load_json
from nph import get_the_prices


# Get yesterdays figures from nordpol stored in JSON
yesterday = load_json()

if len(yesterday) == 0:
    print 'no yesterday data to compare with!' 
    sys.exit(1)

# Get todays figures from nordpol
today = get_the_prices()

# Compare yesterdays and todays figures
for t in range(len(today)):
    if today[t] == yesterday[t]:
        print "hour", t, "today == yesterday", today[t]
    elif today[t] < yesterday[t]:
        print "hour",t, "today < yesterday", today[t],  yesterday[t]
    else:
       print "hour",t, "today > yesterday", today[t], yesterday[t]
       
 