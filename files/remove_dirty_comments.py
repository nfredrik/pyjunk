import re
from tempfile import mkstemp
from shutil import move
import os
import sys

def row_2_remove(line):
    if re.match('^(HPC[A-Z\d]{3}\*.*)', line):
        return True
    return False

def main(): 


    args = sys.argv[1:]
#    pco_file = 'PAOB.pco'
    pco_file = args[0]

    if not args:
      print 'usage:<file to convert>'
      sys.exit(1)

    print args

    #Create temp file
    fh, abs_path = mkstemp()

    writefile = open(abs_path,'w')
    readfile = open(pco_file, 'r')
    remove_cntr = 0

    # Check rows with non relevant comments
    for line in readfile:
      if not row_2_remove(line):
        writefile.write(line)
      else:
        remove_cntr +=1  

    #Close temp file
    writefile.close()
    os.close(fh)

    readfile.close()

    #Remove original file
    os.remove(pco_file)

    #Move new file
    move(abs_path, pco_file)

    print 'Number of rows removed:', remove_cntr


if __name__ == '__main__':
  main()
