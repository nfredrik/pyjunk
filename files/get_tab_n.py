
# :/srv/home/cm/svn/lyftetrepos/trunk/LYFTET-FLMU-S>

#    1      1   TKOD                     I/O-'X'        4        4     1/S  NO    1.1    IO=Y,SECT=S,SECL=1,TDEP=N,F=N,TAB=N,
#                                                                                       UC=Y,REPN=N,VWID=N,VPOS=Y,SECF=N,NJ=Y,
#                                                                                       PRO=N,MOD=N,CON=S,FI=N,HI=N,BC=E,FC=W,
#                                                                                       EMP=N,FONT=N
#                                                                                       ---------------------------------------------

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




def main(args):

    if not args:
        print 'usage: <directory>'
        sys.exit(1)

    
    for file in enumeratepaths(args[0]):
#        print file
        too_late = 0
        line_cntr = 0
        for string in  open(file, 'r'):
#            print string
            if string.find('NO    1.1') != -1:
                too_late = 1
                hit = line_cntr
#                print 'ett' 
            if string.find('TAB=N') != -1 and too_late == 1:
                print file,
                if line_cntr != hit : 
                    print line_cntr, hit
                else:
                    print ' '
#                print 'tva' 

            if string.find('---------') != -1:
                too_late = 2
#                print 'tre'
            line_cntr+= 1
#x        fh.close()
#        sys.exit(29)

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

