#!/usr/bin/python -tt

import tarfile
import sys
import os

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
      
          filename = os.path.basename(tarinfo.name)
          if filename not in dict:
              dict[filename] = tarinfo.name
          else:
              print 'file:', filename, ' with same in', tarinfo.name, 'and', dict[filename]

if __name__ == '__main__':
  main()
