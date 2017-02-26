import zipfile
import os
import sys
from os import walk
from os.path import join


def extract_files(zipf = "./volvo.zip", destdir ='./nuda'):

  if not os.path.isfile(zipf):
    raise Exception("Error: no zipfile:" + zipf)
  
  with zipfile.ZipFile(zipf) as myzip:
    if myzip.testzip() != None:
      raise Exception("Error: invalid zipfile:" + myzip)
    
    myzip.extractall(destdir)


  root = destdir + '/tests'  

  if not os.path.isdir(root):
    raise Exception("Error: not directory:" + root)

  return [join(root,f) for root,dirs,files in walk(root) for f in files]  


def main():

  the_dir = 'mydir'  
  the_files = extract_files(zipf = "./volvo.zip", destdir = the_dir)

  for file in the_files:
    print "opening:" + file
    with open(file) as fh:
      print fh.read()
    

if __name__ == '__main__':
    sys.exit(main())


    
