#!/usr/bin/python -tt


import sys

def main(args):

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  print args

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  print 'todir:', todir

  if todir:
      print 'We got something on todir'
  else:
      print 'nothing found'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))
