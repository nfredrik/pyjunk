#!/usr/bin/python

import datetime
import os
import sys
# Import modules for CGI handling 
import cgi, cgitb 



POC='/program/POC-Leveranser'
TEST='/program/Test-Leveranser'
PROD='/program/Arkiv-Leveranser'
OLLE='/srv/www/htdocs/olle'
the_archive = { 'POC':POC, 'Test':TEST, 'Prod':PROD, 'Olle': OLLE}

def splitpath(path, maxdepth=20):
     ( head, tail ) = os.path.split(path)
     return splitpath(head, maxdepth - 1) + [ tail ] \
         if maxdepth and head and head != path \
         else [ head or tail ]


class Deploy(object):
    def __init__(self, file):
        self.filepath= file[16:]
        self.file= file
        tmp = os.path.basename(file)
        self.link_name = tmp[:-19]
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
        self.created = ctime

    def get_deployed_created(self):
        return self.get_link_name()[1:9]

    def get_file_created(self):
        return self.created

    def get_file_path(self):
        return self.filepath

    def get_link_name(self):
        return self.link_name

    def get_content(self):
        self.fh= open(self.file, 'r')
        self.data = self.fh.read()
        self.fh.close()
        return self.data


def calc_time(period):
    now = datetime.datetime.now()

    #print 'period:', period
    if period == 'week':
        t = datetime.timedelta(days=7)
    elif period == 'month':
        t = datetime.timedelta(days=31)
    elif period == 'all':
        t = datetime.timedelta(days=365)
    else:
        print 'ERROR!!!!'

    then = now - t

    return int("%s"%then.strftime("%Y%m%d"))  

def find_type(typ, filename):

    if typ == 'all':
        return True

    if typ == 'full':
        if filename.find('PATCH') == -1:
            return True

    if typ == 'patch':
        if filename.find('PATCH') != -1:
            return True

    return False


# TODO: Filter on type of deploy and period

def get_html_list(archive, type, period ):

    list_of_deploys = []
    for root, dirs, files in os.walk(archive):
        for file in files:
#            if file.endswith('.html'):
#            if file.endswith('release_notes.html'):
            if file.endswith('.txt'):
#                print 'file:', file 
                deploy =  Deploy(os.path.join(root, file))

                if find_type(type, deploy.get_link_name()):
#                if True:
#                    print 'GOT:' ,calc_time(period), int(deploy.get_deployed_created())
#                    print
                    if calc_time(period) <= int(deploy.get_deployed_created()):
#                    if True:
#                        print 'added' 
                        list_of_deploys.append(deploy)

#    print 'in list:', len(list_of_deploys)
    return list_of_deploys


def main(args):
    # Create instance of FieldStorage 
    form = cgi.FieldStorage() 

    # Get data from fields
    if form.getvalue('archive'):
       archive = form.getvalue('archive')
    else:
       archive = "Not set"

    if form.getvalue('deploy'):
      deploy = form.getvalue('deploy')
    else:
      deploy = "Not set"

    if form.getvalue('period'):
       period = form.getvalue('period')
    else:
       period = "Not set"


#    print "Content-type:text/html\r\n\r\n"
    print "Content-type:text/plain\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>Lista deployments</title>"
    print "</head>"
    print "<body>"
    for item in get_html_list(the_archive[archive], deploy, period):
        print "<h3>%s</h3>"% item.get_link_name()
        print "<p>%s</p>"%item.get_content()
        print "<hr>"
    print "</body>"
    print "</html>"

if __name__ == '__main__': sys.exit(main(args=sys.argv[1:]))
