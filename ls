#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

# 1. Print files in direcory,  use os
# 2. Print special files in directory, use re

# ['copyspecial.py', 'solution', 'xyz__hello__.txt', 'zz__something__.jpg']
def get_files(dir):
  files = os.listdir(dir)
  #print files
  string = ' '.join(files)
  special_files = re.findall('[\w]+__[\w]+__\.[\w]+',string)

  # TODO:Check if funny files to copy ...
  
#  print special_files
#  print os.path.abspath(dir)
  abs_list = []
  for file in special_files:
    abs_list.append(os.path.abspath(dir) + '/' + file)

#  print abs_list
  return abs_list
 
  
# 3. Copy files to -todir, use shutil

def to_dir(file_list, to_dir):

  # TODO: check if the to_dir exists ...
  if not os.path.exists(to_dir):
    sys.stderr.write('directory do not exist: ' + str(to_dir) + '\n')
    sys.exit(42)
  for file in file_list:
    shutil.copyfile(file, to_dir +'/' + os.path.basename(file))
  
# 4. Zip files with zip-command, use commands

def to_zip(file_list, zipfile):

  cmd = 'zip -j ' + zipfile + ' '
  # Check if the command exists ...

  cmd = cmd  + ' '.join(file_list)

  print 'I want to execute:', cmd
  # I'm going to run following command, print ...
#  sys.exit(42)
  # Do it !
  (status, output) = commands.getstatusoutput(cmd)

  if status:
    sys.stderr.write('bzip failed: ' + output + '\n')
    sys.exit(42)
    
    
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  dir_copy = False
  if args[0] == '--todir':
    todir = args[1]
    dir_copy = True
    del args[0:2]

  tozip = ''
  zipping = False
  if args[0] == '--tozip':
    tozip = args[1]
    zipping = True
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for dir in args:
    file_list = get_files(dir)

  if dir_copy:
    to_dir(file_list, todir)


  if zipping:
    to_zip(file_list, tozip)
if __name__ == "__main__":
  main()
