#!/usr/bin/python -tt

import tarfile
import sys
import os
from  memberfile import *

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: <directory with tar files> '
    sys.exit(1)

  list_of_files = [file for file in os.listdir(args[0]) if file.endswith('tar.gz')]

#  print list_of_files

  dict = {}
  for f in list_of_files:
      tar = tarfile.open(f, "r:gz")
      for tarinfo in tar:
          if tarinfo.isdir():  continue
      
          newfile = MemberFile(tar, tarinfo.name)
          if newfile.get_md5() not in dict:
              dict[newfile.get_md5()] = tarinfo.name
          else:
              print 'file:', tarinfo.name, ' with same md5',  dict[newfile.get_md5()]

if __name__ == '__main__':
  main()
