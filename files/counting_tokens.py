import os
import sys
from filestatus import FileStatus

def enumeratepaths(path): 
    """Returns the path to all the files in a directory recursively""" 
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file) 
            path_collection.append(fullpath)
    return path_collection




def main(args):

  if not args:
    print 'usage: <file to count>'
    sys.exit(1)

#  print args

#  print filenames
#  return 0
 
#  for dirpath, dirnames, fname in os.walk(args[0]):
#      filenames.append()

  filenames = enumeratepaths(args[0])

  dict = {} 
  for filename in filenames: 

      file = FileStatus(filename)
      if not file.regular_file: continue

      fh = open(filename, 'r')
      string = fh.read()
      fh.close()

      for line in string.split():
          for words in line.split():
              for token in words:
                  if token not in dict:
                      dict[token] = 1
                  else:
                      dict[token] += 1

  new = {}
  #  for key, value in  dict.items():
  for key, value in  sorted(dict.iteritems(), key=lambda(k,v):(v,k),reverse=True):
#      print key,'  :  ', hex(ord(key)),'  :  ',  value
      new[hex(ord(key))] = value
  
  for key, val in sorted(dict.iteritems()):
      print key, hex(ord(key)), val

  return 0

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
