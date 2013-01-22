#!/usr/bin/python
#
# author: fredrik
# license: bsd
# copyright: re2


import json 
import sys
import urllib2



# {"jobs":[{"name":"any_python"},{"name":"create_textfile"}],"name":"nisse"}

# 

jenkinsUrl = 'http://localhost:8080/api/json?tree=views[name,jobs[name]]'

#http://localhost:8080/api/json?tree=views[name]
json_query='json?tree=views[name]'

#if len( sys.argv ) > 1 :
#    jobName = sys.argv[1]
#else :
#    sys.exit(1)


try:
    print jenkinsUrl
    
    jenkinsStream   = urllib2.urlopen( jenkinsUrl )
except urllib2.HTTPError, e:
    print "URL Error: " + str(e.code) 
    print "      (URL [" + jenkinsUrl + "] probably wrong)"
    sys.exit(2)

try:
    print 'before'
    buildStatusJson = json.load( jenkinsStream )
    print 'after'
except:
    print "Failed to parse json"
    sys.exit(3)

#print buildStatusJson

#if buildStatusJson['views'][4]['name'] == 'nisse':
#    print 'Julle Julle'
#    print buildStatusJson['views'][4]['jobs'][0]['name']

for tlist in buildStatusJson['views']:
    if tlist['name'] == 'nisse':
        print 'jobs in nisse view:'
        for job in tlist['jobs']:
            print job['name']       
  

