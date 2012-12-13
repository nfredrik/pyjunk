#!/usr/bin/python

import sys

try:
    jalle = 8/0
    raise Exception('aj')
except:
    (exc_class, exc_object, exc_traceback) = sys.exc_info()
    print"""internal and completely unexpected problem,
    manifested as %s""" % str(exc_class)
