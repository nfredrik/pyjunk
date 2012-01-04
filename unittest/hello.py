#!/usr/bin/python


import sys

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: yes or no '
    sys.exit(1)

  if args[0] == 'yes':
    sys.exit(0)

  sys.exit(1)

  
if __name__ == '__main__':
  main()
