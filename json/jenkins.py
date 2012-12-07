#!/usr/bin/python
#
# author: ajs
# license: bsd
# copyright: re2


import json 
import sys
import urllib2

##jenkinsUrl = "https://http://192.168.1.68:8080/job/"
jenkinsUrl = "http://192.168.1.68:8080/job/"


#if len( sys.argv ) > 1 :
#    jobName = sys.argv[1]
#else :
#    sys.exit(1)

jobName="4th"

try:
    print jenkinsUrl + jobName + "/lastBuild/api/json"
    
    jenkinsStream   = urllib2.urlopen( jenkinsUrl + jobName + "/lastBuild/api/json" )
except urllib2.HTTPError, e:
    print "URL Error: " + str(e.code) 
    print "      (job name [" + jobName + "] probably wrong)"
    sys.exit(2)

try:
    buildStatusJson = json.load( jenkinsStream )
except:
    print "Failed to parse json"
    sys.exit(3)

if buildStatusJson.has_key( "result" ):      
    print "[" + jobName + "] build status: " + buildStatusJson["result"]
    if buildStatusJson["result"] != "SUCCESS" :
        exit(4)
    else:
        print 'Hurra!'     
else:
    sys.exit(5)

sys.exit(0)