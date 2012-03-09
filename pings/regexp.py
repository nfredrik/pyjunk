import re

class RegExp(object):

    def __init__(self, pattern, match):
        self.bool = False
        m = re.match( pattern, match)
        
        if m != None:
            self.bool = True 

    def __call__(self):
        return self.bool

    def matching(self):
        return False
