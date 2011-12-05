import sys
import re
from collections import defaultdict

#from regexp import RegExp

def main():
  args = sys.argv[1:]

  if len(args) != 1:
    print 'usage: <file from compilation>'
    sys.exit(1)
      
  print args[0]


  fh = open(args[0], 'rb')

  string = fh.read()

  olle =' #*1014-E************                                                          **                                   37\
         **    Period missing. Period assumed.                                                                             37\
        *1026-E****************************                                          **                                 3756\
        **    Source literal is non-numeric - substituting zero                                                         3756'
#PCB-S-00576, PLS-0: SQL Statement ignored
#Error at line 280, column 13 in file /srv/systest/us/data//PROD/KGBULB/KG1000.pc


  first  = re.findall('\*([\d]{4}\-E)[*\s\d]+([A-Za-z\s.-]+)', string)
  second  = re.findall('(PLS-[\d]{1,4}):[\s]+([A-Za-z\ ]+)', string)


#  print second
#  for s in second:
#     print s
#  sys.exit(1)

  err_c_dict = {}

  for f, s  in first:
      f += ' ' + s.strip()
      if f not in err_c_dict:
          err_c_dict[f] = 1 
      else:
          err_c_dict[f] += 1 

  for f, s  in second:
      f += ' ' + s.strip()
      if f not in err_c_dict:
          err_c_dict[f] = 1 
      else:
          err_c_dict[f] += 1 


  for k, v in err_c_dict.items():
      print v, ':', k

if __name__ == '__main__':
  main()
