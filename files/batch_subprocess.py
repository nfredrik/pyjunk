import time
import sys
import os
import re
#import commands
import subprocess

OK, ERROR = 0, 1

class Batch(object):

#REDIRECTING  DEFAULT  OUTPUT  TO: /srv/utv/devenvs/fsv/us/log/runstreams/PR/LK1000.20120327154442
# 27/03/2012 15:44:43, [INFO]  Return code for program [LK1000] is [0], LK1000, 23112

    def __init__(self, ecl):
        self.filename = ecl
        self.res = (False,  1000)
        self.t0 = time.time()
#        (self.status, self.output) = commands.getstatusoutput(ecl)
        self.output = subprocess.Popen(ecl, shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

        self.output.wait()

        if self.output.returncode != 0:
            print "There were some errors"
        stdout_value =  self.output.communicate()[0]
        self.out = repr(stdout_value) 
#        print self.out
#        sys.exit(42)
#        print self.filename, 'started...'
        # find output file in stdout
#        print ecl
        self.etime = time.time() - self.t0
        self.file = re.search('REDIRECTING  DEFAULT  OUTPUT  TO: (.*)', self.out)
#        print self.output

        # Return if the outfile not is found
        if self.file == None: 
            return
      
         # open output file and search for return code from execution 
        self.logfile = self.file.group(1).rstrip('\\n\'')
#        print self.filename
#        sys.exit(42)
        self.fh = open(self.logfile, 'r')
        self.string = self.fh.read()
        self.fh.close()

        # Search for return code in ecl log
#        self.name = re.search('Return code for program \[LK1000\] is \[([\d]+)\]', self.string)
        self.name = re.search('Return code for program \[.*\] is \[([\d]+)\]', self.string)
        if self.name != None and self.name.group(1) == '0': 
            self.res = (True, 0)
            return

        if self.name != None and self.name.group(1) == '0': 
            self.res = (False,  self.name.group(1))

        return

    def get_filename(self):
       return self.filename
     
    def get_etime(self):
       return self.etime

    def result(self):
       """
       Return tuple if test failed or not, boolean and than return code 
       """
       return self.res


def enumeratepaths(path):
    """Returns the path to all the files in a directory recursively"""
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):

        if dirpath.find('.svn') != -1: continue
#            print dirpath
#            sys.exit(42)

        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            path_collection.append(fullpath)
#    sys.exit(42)
    return path_collection

def ecl_file(file):
    # #!/usr/bin/env execute.sh
    fh = open(file, 'r')
    string = fh.readline()
#    print 'string:', string
    if string.find('execute.sh') == -1 :
        return False
    return True

def main(args):

    if not args:
        print 'usage: <dir of ecls>'
        sys.exit(1)

    # Get files 
    filenames = enumeratepaths(args[0])

    ecls = []

    # Lets traverse through
    for filename in filenames:

        # Check every file
        if ecl_file(filename):
#            print 'filename:', filename
            ecls.append(Batch(filename))


    summary = True
    for ecl in ecls:
        print ecl.get_filename(), 'got:', ecl.result()[0], 'time:',
        print "%.2f" % ecl.get_etime()
        summary = summary and  ecl.result()[0]

    if summary:
        return OK
    else:
        return ERROR    

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
