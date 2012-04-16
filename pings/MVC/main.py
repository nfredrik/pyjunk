#!/usr/bin/python

from control import Control
import sys

OK,ERROR = 0,1


def main(args):


  control = Control()

  control.get_list()

  return OK


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
