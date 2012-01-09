#!/usr/bin/python
import sys
import re  
import csv
data1= """
Compiling FS400T.cob -> FS400T.o
       INPUT-OUTPUT SECTION.                                                                                      56
*1014-E************                                                          **                                   56
**    Period missing. Period assumed.                                                                             56
---
Compiling FS400T.o -> FS400T.so
--
"""




def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: logfile '
    sys.exit(1)

  fh = open(args[0], 'r')
  data = fh.read()
#  print 'got', args[0]

  regex = re.compile(r"""Compiling[ ](\S+).cob.*\n.*\n\*([\d]{4}\-E)[^\d]*([\d]+)\n[\*]+\s+([a-zA-Z\.\ ]+)\s+""", re.MULTILINE) 
  print regex.search(data).groups() 
#  sys.exit(42)

  csv_writer = csv.writer(open('errors.csv', 'wb'), delimiter = ',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

  for x in regex.finditer(data):
#      print x.groups() 
      print x.group(1),
      print x.group(2),
      print x.group(3),
      print x.group(4)
      csv_writer.writerow([x.group(1), x.group(2) , x.group(3) , x.group(4)])

  
if __name__ == '__main__':
  main()
