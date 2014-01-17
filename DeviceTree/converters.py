from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())

class Node(object):
    def __init__(self, *args, **kargs):
        pass
    
class Property(object):
    def __init__(self):
        pass
    

if __name__ == '__main__':
    import sys
#    obj = Uppercase(open('trispam.txt'), sys.stdout)
#    obj.process()
    htlmsize = HTMLize()
    obj = Uppercase(open('trispam.txt'), htlmsize)
    obj.process()