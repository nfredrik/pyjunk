import logging
import zipfile
import os
import sys
from os import walk
from os.path import join

class ExtractZipError(Exception): pass


class FileExtract:

  @classmethod

  # TODO: Possible to do in same maner as ruby?
  def default(self):
    print 'hej'
    return {'zipf': "./volvo.zip", 'destdir':'./mydir', 'apidir' : 'tests' }

  @classmethod
  def extract_files(self, zipf = "./volvo.zip", destdir ='./mydir', apidir = 'tests'):
#  def extract_files(self, args = {}):

    #tmp = self.default()
    #self.args = tmp.update(args)
  
    if not os.path.isfile(zipf):
      raise ExtractZipError("Error: no zipfile:" + zipf)
  
    with zipfile.ZipFile(zipf) as myzip:
      if myzip.testzip() != None:
        raise ExtractZipError("Error: invalid zipfile:" + myzip)
    
      myzip.extractall(destdir)


    # Nota bene: This is hardcoded  
    root = destdir + '/' + apidir  

    if not os.path.isdir(root):
      raise Exception("Error: Could not find the direcory:" + root)

    return [join(root,f) for root,dirs,files in walk(root) for f in files]  


def main():

  print "--- Start log everything in wrapping log file ..."

  print "--- Find relevant zipfile ..."
  base = "./"
  binfiles = [ os.path.join(base,f) for base, _, files in os.walk(base) 
            for f in files if f.endswith("volvo.zip") ] 


  print "--- Extract file  ..."
  the_files = FileExtract.extract_files(zipf= binfiles.pop())



  print "--- Generate a api request based on  ..."  
  
  for file in the_files:
    print "opening:" + file
    with open(file) as fh:
      print fh.read()

  print "--- Store in file structure according to return codes  ..."  

  print "--- Use invariants for validation??  ..."    

  return 0


if __name__ == '__main__':
  
  sys.exit(main())


    
