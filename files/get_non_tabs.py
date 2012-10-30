
# :/srv/home/cm/svn/lyftetrepos/trunk/LYFTET-FLMU-S>

#    1      1   TKOD                     I/O-'X'        4        4     1/S  NO    1.1    IO=Y,SECT=S,SECL=1,TDEP=N,F=N,TAB=N,
#                                                                                       UC=Y,REPN=N,VWID=N,VPOS=Y,SECF=N,NJ=Y,
#                                                                                       PRO=N,MOD=N,CON=S,FI=N,HI=N,BC=E,FC=W,
#                                                                                       EMP=N,FONT=N
#                                                                                       ---------------------------------------------

#

import re
import os
import sys

def enumeratepaths(path):
    """Returns the path to all the files in a directory recursively"""
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):

        for file in filenames:
            if not file.endswith('._SYM'): continue
            fullpath = os.path.join(dirpath, file)
            path_collection.append(fullpath)
    return path_collection


# FORM NAME:             PRIA1

def main(args):

    if not args:
        print 'usage: <directory>'
        sys.exit(1)

#    1      1   TKOD                     I/O-'X'        4        4     1/S  NO    1.1    IO=Y,SECT=S,SECL=1,TDEP=N,F=N,TAB=N,
#  1      1   TKOD                     I/O-'X'       41       41     1/S  NO    1.1    IO=Y,SECT=S,SECL=1,TDEP=N,F=N,TAB=Y,
#    regexp =  re.compile("[\s]+[\d]+[\s]+[\d]+[\s]+TKOD+[\s]+[\w\/\-\']*[\s]+([\d]+)[\s]+([\d]+)[\s]+[\w//]*[\s]+NO[\s]+1\.1[\s]+([\w\=\,]+)+(?=TAB=Y)")
#    regexp =  re.compile("NO[\s]+1\.1[\s]+([\w\=\,]+)+(?=TAB=Y)")
#    regexp =  re.compile("NO[\s]+1\.1[\s]+([\w\=\]+){1}([\w\=\,]+)+")
    regexp =  re.compile("[\s]+[\d]+[\s]+[\d]+[\s]+TKOD+[\s]+[\w\/\-\']*[\s]+([\d]+)[\s]+([\d]+)[\s]+[\w//]*[\s]+NO[\s]+1\.1[\s]+([\w]+\=[\w]\,)+(?=TAB=Y)")
#    regexp = re.compile("NO[\s]+1\.1[\s]+([\w]+\=[\w]\,)+(?=TAB=Y)")
    formname = re.compile("FORM NAME\:[\s]+([\w\d]+)")
    for file in enumeratepaths(args[0]):
        fh = open(file, 'r')
        string = fh.read()
        fh.close()
        hit = regexp.search(string)

        if hit != None and hit.group(1) == '4':
             name = formname.search(string)
             print name.group(1), ',',
#             print '1:', hit.group(1)
#             print '2:', hit.group(2)
#             print hit.group(3)
             print os.path.basename(file)

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

