import urllib
import urllib2
#socket = urllib2.urlopen('http://byggserver02:8080/job/pytest/build')  # works
socket = urllib2.urlopen('http://byggserver02:8080/job/pytest/buildWithParameters?TAGVALUES=UNIREG_1_7_1')
print 'RESPONSE:*', socket
print 'URL:*', socket.geturl()

#html = socket.read()
#print html
