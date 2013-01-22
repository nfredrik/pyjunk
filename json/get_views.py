#!/usr/bin/python
#
# author: fredrik
# license: bsd
# copyright: re2


import json 
import sys
import urllib2

jenkinsUrl = 'http://localhost:8080/api/json?tree=views[name]'

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

if buildStatusJson.has_key( "views" ):
    listan = buildStatusJson['views']
    for item in listan:
        
        print 'view:' + item['name']
        
    print 'yes'
    print 'test:' + buildStatusJson['views'][4]['name']

print 'the end'          
  

