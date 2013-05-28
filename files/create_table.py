#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os, sys
import re

class tableFile(object):
    def __init__(self, filename):
        self.fh = open(filename, 'w') 

    def write_row(self,row):
        self.fh.write(row)

    def __del__(self):
        self.fh.close()
        
        

def main():        

    print 'start'
    tfile = tableFile('dummy')

    with open('stora.sql') as fileh:

        while True:
            row = fileh.readline()
            if row =='': break

            test = re.search("CREATE TABLE[\s]*PRDSCHEMA\.([\d\w\\_]+)",row)
        
            if test != None:
                del tfile           
                tfile = tableFile('create_table_'+ test.group(1).lower() +'.sql')
                tfile.write_row(row)
            else:
                tfile.write_row(row)
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    sys.exit(main())
