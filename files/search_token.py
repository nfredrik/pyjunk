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
    return os.system("file -b" + filename + " | grep text > /dev/null")


def main(args):

  if not args:
    print 'usage: <directory to search> <token to search>'
    sys.exit(1)

#  print args

#  print filenames
#  return 0
 
#  for dirpath, dirnames, fname in os.walk(args[0]):
#      filenames.append()

  filenames = enumeratepaths(args[0])
  token = args[1]
  print token, hex(int(token,16))

  dict = []
  for filename in filenames: 

#      if not is_binary(filename): continue

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


  new = {}
  #  for key, value in  dict.items():
  for key, value in  sorted(dict.iteritems(), key=lambda(k,v):(v,k),reverse=True):
#      print key,'  :  ', hex(ord(key)),'  :  ',  value
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

  return 0

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
