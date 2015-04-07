import sys
from db import PingDB
from regexp import RegExp

def main():
  args = sys.argv[1:]

#  print 'arg length', len(args)
  if (not args): # or len(args) != 1 or len(args) != 2:
    print ('usage: [ttl][response][time] [object]')
    sys.exit(1)

  option = ''
  if args[0] == 'ttl' or args[0] == 'response' or args[0] == 'time':
    option = args[0]
  else:
    print ('no valid option:', args[0])
    sys.exit(1)

#  print 'argg1:',  args[1], ':'

  if len(args) == 1:
    dest = '*' 
  elif len(args) == 2:
    pattern = "^[a-z]+(\.[a-z]+)+$"
    valid_addr = RegExp(pattern, args[1])
    if valid_addr():
        dest = args[1]
    else:
        print ('no valid object:', args[1])
        sys.exit(1)
  
  print ('result:', option, 'and:', dest)

  print ('time                object   ttl    response')
  db = PingDB()
  if dest == '*':
      if option == 'ttl':
          list =  db.read_ttl_order()
          for i in list:
              (time, obj, ttl, response) = i
              print (time, obj, ttl, response)
  else:
      list = db.read_date_4_object(args[1])
      for i in list:
          (time, ttl, response) = i
          print (time,  ttl, response)
      
  

if __name__ == '__main__':
  main()
