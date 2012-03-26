import os
import sys
from filestatus import FileStatus

OK, ERROR = 0, 1

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


  # Get files including path
  filenames = enumeratepaths(args[0])

  dict = {} 


  # For every file, split in rows, words, finally tokens
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
  for key, value in  sorted(dict.iteritems(), key=lambda(k,v):(v,k),reverse=True):
      new[hex(ord(key))] = value
  
  ascii_ext = False

  for key, val in sorted(dict.iteritems()):

      if hex(ord(key)) == '0x0':
          print "============ Non printable chars =========="
      elif hex(ord(key))== '0x21':
          print "============ ASCII tokens ============"
      elif ord(key) > 0x7e and not ascii_ext:
          print "============ ASCII extended tokens ============"
          ascii_ext = True

      print key, hex(ord(key)), val

  return OK

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
