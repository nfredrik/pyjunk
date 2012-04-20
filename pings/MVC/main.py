#!/usr/bin/python

from altview import PlotObject
from control import Control

import sys

OK,ERROR = 0,1
WAIT= 42


def main(args):


  control = Control()
  control.get_list()

  print 'test alternative'
  altview = PlotObject()
  control1 = Control(view=altview)
  control1.get_list()

  return OK


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
