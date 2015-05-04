

import sys

class ExampleErr(Exception): pass


class Example(object):
    def __init__(self):
        raise ExampleErr('wrong')


try:
    example = Example()
    print ('Hej') 
    raise Exception('Aj')

except:
    (exc_class, exc_object, exc_traceback) = sys.exc_info()
    print("""internal and completely unexpected problem,
    manifested as %s""" % str(exc_class))

