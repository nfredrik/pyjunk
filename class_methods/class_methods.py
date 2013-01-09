#!/usr/bin/env python

import sys

class ClassMethods(object):

    def __new__(cls):
        print 'new'
        return super(ClassMethods,cls).__new__(cls)

    def __init__(self):
        print 'init'
        self.x = 1
        self.y = 2

    def __del__(self):
        print 'del'
    def __repr__(self):
        print 'repr'
        return '<%s>' % self.__class__.__name__
        
    def __str__(self):
        print 'str'
    def __cmp__(self,other):
        print 'cmp'
    def __index__(self):
        print 'index'
    def __hash__(self):
        print 'hash'
    def __getattr__(self,name):
        print 'getattr'
    def __getattribute__(self,name):
        print 'getattribute'
    def __setattr__(self,name,attr):
        print 'setattr'
    def __delattr__(self,name):
        print 'delattr'
    def __call__(self,args, kwargs):
        print 'call'
    def __lt__(self,other):
        print 'lt'
    def __le__(self,other):
        print 'le'
    def __lt__(self,other):
        print 'lt'
    def __gt__(self,other):
        print 'gt'
    def __ge__(self,other):
        print 'ge'
    def __eq__(self,other):
        print 'eq'
    def __ne__(self,other):
        print 'ne'
    def __nonzero__(self):
        print 'nonzero'


def main(args):

    a = ClassMethods()
    # get repr working
    a

if __name__ == '__main__':
    sys.exit(main(sys.argv))








