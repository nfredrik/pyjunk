#!/usr/bin/python
import re
from netstat import Netstat

#discard         9/tcp           sink null
#discard         9/udp           sink null


def set_colour(status):
    if status == 'LISTEN':
        print "<td bgcolor=#00FF00 >" + status + "</td>"
    else:
        print "<td bgcolor=#FF0000 >" + status + "</td>"

dict = {}
for line in open("/etc/services"):
    test = re.search('(^[a-zA-Z\-\_\d]+)\s*(\d+)', line)
    if test != None:
#        print test.group(1), test.group(2)
        dict[test.group(1)] = test.group(2)



#for key, value in dict.items():
#    print key, value
#    pass


users = ['-ns', '-dgm', '-ssn']
services= ['netbios']

sum =[ 'netbios'+ x for x in users]


netstat = Netstat()                                                                            

#print "Content-Type: text/plain\n\n"
             
#print  netstat.get_port_status(631)
#print  netstat.get_port_status(50022)
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

print "<TITLE>CGI script output</TITLE>"
#print "<H1>This is my first CGI script</H1>"

print '<table border="1">'
print "<tr>"
print "<td><b>Service:</b></td>"
print "<td><b>Status:</b></td>"
print "</tr>"
print "<tr>"
print "<td>631</td>"
#print "<td bgcolor=#00FF00 >" + netstat.get_port_status(631) + "</td>"
set_colour(netstat.get_port_status(631))
print "</tr>"

for m in sum:
    print "<tr>"
    print "<td>" + m + "</td>"
#    print "<td>" + netstat.get_port_status(str(dict[m])) + " </td>"
    set_colour(netstat.get_port_status(str(dict[m])))
    print "</tr>"
print "</table>" 

#exit(2)

