#!/usr/bin/python -tt

import tarfile
import sys
import os
import re

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: <directory with tar files> '
    sys.exit(1)

  list_of_files = [file for file in os.listdir(args[0]) if file.endswith('tar.gz')]

#  print list_of_files

  dict = {}
  for f in list_of_files:
      tar = tarfile.open(args[0]+ '/' +f, "r:gz")
      for tarinfo in tar:

          filename = os.path.basename(tarinfo.name)

          # Check name for directories
          if tarinfo.isdir():
              if re.match('^[a-zA-Z]{1}[a-zA-Z0-9\_]+$', filename) == None:
                  print 'directory:', filename, ' path', tarinfo.name, ' and ', f
              continue      

          # Check name for files
          if re.match('^[a-zA-Z0-9]{1}[a-zA-Z0-9_\-\.]+$', filename) == None:
              print 'file:', filename, ' path', tarinfo.name, ' and ', f

if __name__ == '__main__':
  main()
