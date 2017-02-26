import zipfile
import os
import sys
from os import walk
from os.path import join


def extract_files(zipf = "./volvo.zip", destdir ='./nuda'):

  if not os.path.isfile(zipf):
    raise Exception("Error filen finns inte")

  with zipfile.ZipFile(zipf) as myzip:
    nille = myzip.extractall(destdir)

  root = destdir + '/tests'  
  if not os.path.isdir(root):
    raise Exception("Error mappen finns inte")

  return [join(root,f) for root,dirs,files in walk(root) for f in files]  
    
def main():

  # Verify that we have a zipfile
  # Extract it to defined directory
  # Verify that we have a tests directory
  # with files ...
  # return array of files  
  the_dir = 'mydir'  
  the_files = extract_files(destdir = the_dir)
  for file in the_files:
    print file
  
    

if __name__ == '__main__':
    sys.exit(main())


    
