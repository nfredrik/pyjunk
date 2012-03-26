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


def is_binary(filename):
    return os.system("file -b " + filename + " | grep text > /dev/null")


def main(args):

  if not args:
    print 'usage: <directory to search> <token to search>'
    sys.exit(1)

  filenames = enumeratepaths(args[0])
  token = args[1]
  print token, hex(int(token,16))

  dict = []
  for filename in filenames: 

      #if not is_binary(filename): continue

      fh = open(filename, 'r')
      string = fh.read()
      fh.close()

      for line in string.split():
          for words in line.split():
              for stoken in words:
#                  print hex(ord(stoken))
                  if hex(ord(stoken)) == hex(int(token, 16)):
                      dict.append(filename)


  print dict
  return OK

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
