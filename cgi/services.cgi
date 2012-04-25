#!/usr/bin/python
import re
import cgi
import sys
import socket
from netstat import Netstat
import os
import re

from subprocess import Popen, PIPE

ORACLE_ENV='/srv/utv/conf/oracle.env'

class OracleEnv(object):
    def __init__(self, file):
        self.fh = open(file, 'r')
        self.string = self.fh.read()

        self.user = self.pwd = self.db = ' '

        self.u = re.search('USER_ORACLE=(.*)', self.string)
        if self.u != None:
            self.user = self.u.group(1)

        self.u = re.search('PASS_ORACLE=(.*)', self.string)
        if self.u != None:
            self.pwd = self.u.group(1)

        self.u = re.search('DB_ORACLE=(.*)', self.string)
        if self.u != None:
            self.db = self.u.group(1)

    def get_user(self):
        return self.user

    def get_pwd(self):
        return self.pwd

    def get_db(self):
        return self.db

class Oracle(object):

    def __init__(self,user, pwd, db):
        self.session = Popen(['/u01/app/oracle/product/11.2.0/client/bin/sqlplus', '-S', user + '/' + pwd + '@' + db], stdin=PIPE, stdout=PIPE, stderr=PIPE)

    # Retuns the output and error string (if any)
    def runSqlQuery(self, sqlCommand):
        self.session.stdin.write(sqlCommand)
        return self.session.communicate()


def tryQuery():

    # sqlplus needs ORACLE_HOME to be set
    os.putenv('ORACLE_HOME', '/u01/app/oracle/product/11.2.0/client')

    oraceleenv =OracleEnv(ORACLE_ENV)
    oracle = Oracle(oraceleenv.get_user(), oraceleenv.get_pwd(), oraceleenv.get_db())

    # Check available space
    queryResult, errorMessage = oracle.runSqlQuery("select * from user_tablespaces where TABLESPACE_NAME='RDMS_DATA';")

    # Check if this query worked ...
    if re.search('ERROR', queryResult, re.IGNORECASE) != None:
        return 'DOWN'

    return 'LISTEN'


def isOpen(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


def listening():
    if isOpen('utv-oradb100.bolagsverket.se', '1581'):
        return 'LISTEN'
    else:
         return 'DOWN'


def set_colour(status):
    if status == 'LISTEN':
        print "<td bgcolor=#00FF00 >" + status + "</td>"
    else:
        print "<td bgcolor=#FF0000 >" + status + "</td>"


dict = {}
for line in open("/etc/services"):
    test = re.search('(^[a-zA-Z\-\_\d]+)\s*(\d+)', line)
    if test != None:
        dict[test.group(1)] = test.group(2)



netstat = Netstat()                                                                            


print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers


users = [ 'sbo', 'mth', 'pil', 'mad', 'plp', 'boe', 'lah', 'kln', 'jel', 'fsv', 'law' , 'olk', 'jje']

long_users = { 'sbo':'Stefan', 'mth':'Mattias', 'pil':'Pia', 'mad':'Maria', 'plp':'Pirkko', 'boe':'Bosse', 'lah':'Laila', 'kln':'Christina', 'jel':'Jens', 'fsv':'Fredrik', 'law':'Lars-Ake' , 'olk':'Olof', 'jje':'Jonas'}


form = cgi.FieldStorage()
user= form.getvalue('user')
if user not in users:
    print 'Sorry user not defined'
    sys.exit(1)

# Services
nscs      = [ 'nscs'+ user]
consoper  = [ 'consoper'+ user]
converter = [ 'converter' + user]
mfd       = [ 'mfd' +  user]
rdo       = [ 'rdo' +  user]
ssl       =  'ssl' +  user
tux       =  'tux' +  user

print "<TITLE>utv1-appsrv100 ports</TITLE>"

print "<h3>Status p&#229; utv1-appsrv100s serverportar f&#246;r:</h3>"

print "<h3> " + long_users[user] + "</h3>"

print '<table border="1">'
print "<tr>"
print "<td><b>Service:</b></td>"
print "<td><b>batchjobb</b></td>"
print "<td><b>TIPjobb</b></td>"
print "<td><b>MF Cobol IDE</b></td>"
print "<td><b>Status:</b></td>"
print "<td><b>Startas om av:</b></td>"
print "</tr>"

for m in nscs:
    print "<tr>"
    print "<td>Supercentinela, Fillasningsserver for batchjobb</td>"
    print "<td><b>x</b></td>"
    print "<td><b>x</b></td>"
    print "<td><b> </b></td>"
#    print "<td>" + netstat.get_port_status(str(dict[m])) + " </td>"
    set_colour(netstat.get_port_status(str(dict[m])))
    print "<td> " + long_users[user] + "</td>"
    print "</tr>"

print "<tr>"

for m in consoper:
    print "<tr>"
    print "<td>Console, Presenterar meddelanden genererat av batchjobb</td>"
    print "<td><b>x</b></td>"
    print "<td><b>x</b></td>"
    print "<td><b> </b></td>"
#    print "<td>" + netstat.get_port_status(str(dict[m])) + " </td>"
    set_colour(netstat.get_port_status(str(dict[m])))
    print "<td> " + long_users[user] + "</td>"
    print "</tr>"

print "<tr>"


for m in converter:
    print "<tr>"
    print "<td>Converter, Konverterar UNISYS ECL/IPF scripts in runtime</td>"
    print "<td><b>x</b></td>"
    print "<td><b>x</b></td>"
    print "<td><b> </b></td>"
#    print "<td>" + netstat.get_port_status(str(dict[m])) + " </td>"
    set_colour(netstat.get_port_status(str(dict[m])))
    print "<td> " + long_users[user] + "</td>"
    print "</tr>"

print "<tr>"

for m in mfd:
    print "<tr>"
    print "<td>MFD, server for hantera filkatalog</td>"
    print "<td><b>x</b></td>"
    print "<td><b>x</b></td>"
    print "<td><b> </b></td>"
#    print "<td>" + netstat.get_port_status(str(dict[m])) + " </td>"
    set_colour(netstat.get_port_status(str(dict[m])))
    print "<td> " + long_users[user] + "</td>"
    print "</tr>"

for m in rdo:
    print "<tr>"
    print "<td>RDO, server som kommunicerar med MicroFocus Cobol Eclipse IDE</td>"
    print "<td><b> </b></td>"
    print "<td><b> </b></td>"
    print "<td><b>x</b></td>"
    set_colour(netstat.get_port_status(str(dict[m])))
    print "<td> " + "ngn med rootbehorighet pa utv1" + "</td>"
    print "</tr>"

print "<tr>"
print "<td>Apache server, kommunicerar med HP Terminal</td>"
print "<td><b> </b></td>"
print "<td><b>x</b></td>"
print "<td><b> </b></td>"

set_colour(netstat.get_port_status(str(dict[ssl])))
print "<td> " + "ngn med rootbehorighet pa utv1" + "</td>"

print "</tr>"

print "<tr>"
print "<td>Tuxedo server, kommunicerar apache HP Terminal och ATMI.</td>"
print "<td><b> </b></td>"
print "<td><b>x</b></td>"
print "<td><b> </b></td>"

set_colour(netstat.get_port_status(str(dict[tux])))
print "<td> " + long_users[user] + "</td>"
print "</tr>"


print "<tr>"
print "<td>Oracle database, utvecklingsserverns databas, UTV100</td>"
print "<td><b>x</b></td>"
print "<td><b>x</b></td>"
print "<td><b>x</b></td>"

#set_colour(listening())
set_colour(tryQuery())
print "<td> " + "ngn DBA for UTV100" + "</td>"
print "</tr>"



print "</table>" 


